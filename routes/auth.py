from __future__ import annotations

from pathlib import Path
from typing import cast

from cryptography.fernet import Fernet
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

from flask import Blueprint, render_template, url_for, redirect
from flask import request, flash

from flask_login import (
    login_required, login_user, logout_user
)

from sqlalchemy.exc import IntegrityError

from forms import RegisterForm, LoginForm
from extensions import login_manager, db

from models import Account

auth = Blueprint('auth', __name__)

class UpdatedHasher:
    """Upgrades the Dropbox hasher for modern systems using Argon2 via pwdlib"""
    def __init__(self, pepper_key: bytes):
        self.pepper = Fernet(pepper_key)
        # Configure pwdlib with argon2 (rounds/time_cost can be adjusted via parameters if supported)
        self.pwd_hash = PasswordHash((Argon2Hasher(),))

    def hash(self, pwd: str) -> bytes:
        # hash with argon2
        h: str = self.pwd_hash.hash(pwd)
        # convert this unicode hash string into bytes before encryption
        hashb: bytes = h.encode('utf-8')
        # encrypt this hash using the global pepper
        pep_hash: bytes = self.pepper.encrypt(hashb)
        return pep_hash

    def check(self, pwd: str, pep_hash: bytes) -> bool:
        # decrypt the hash using the global pepper
        hashb: bytes = self.pepper.decrypt(pep_hash)
        # convert this hash back into a unicode string
        h: str = hashb.decode('utf-8')
        # check if the given password matches this hash
        return self.pwd_hash.verify(pwd, h)

    @staticmethod
    def random_pepper() -> bytes:
        return Fernet.generate_key()
    

scriptdir: Path = Path(__file__).resolve().parent.parent

pepfile: Path = scriptdir / "pepper.bin"

with open(pepfile, 'rb') as fin:
    pepper_key = fin.read()

pwd_hasher = UpdatedHasher(pepper_key)

# function that takes a user id and as a string and returns that user
@login_manager.user_loader
def load_user(uid: str) -> Account|None:
    return get_user(uid=int(uid))

# define a helper function that loads uses based on id or email
def get_user(uid: int|None = None, email: str|None = None) -> Account|None:
    if uid is not None:
        return db.session.get(Account, uid)
    else:
        return db.session.scalar(db.select(Account).filter_by(email=email))

###############################################################################
# Route Handlers
###############################################################################

@auth.get('/register/')
def get_register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@auth.post('/register/')
def post_register():
    form = RegisterForm()
    if form.validate():
        try:
            # load the email and password from the form
            email: str = cast(str, form.email.data)
            password: str = cast(str, form.password.data)
            user = Account(email=email, password=password) # type:ignore
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('get_login'))
        except IntegrityError:
            flash('There is already an account with that email address')
            # blank out the password in the form before re-rendering it
            form.password.data = ""
            form.confirm_password.data = ""
            return render_template('register.html', form=form), 422
    # if the form was invalid . . .
    # flash error messages and redirect to get registration form again
    for field, errors in form.errors.items():
        for msg in errors:
            flash(f"{field}: {msg}")
    # blank out the password in the form before re-rendering it
    form.password.data = ""
    form.confirm_password.data = ""
    return render_template('register.html', form=form), 422

@auth.get('/login/')
def get_login():
    form = LoginForm()
    return render_template('login.html', form=form)

@auth.post('/login/')
def post_login():
    form = LoginForm()
    if form.validate():
        # try to get the user associated with this email address
        user: Account|None = get_user(email=form.email.data)
        # if this user exists and the password matches
        if user is not None and user.verify_password(str(form.password.data)):
            # log this user in through the login_manager
            login_user(user)
            # redirect the user to the page they wanted or the home page
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('home')
            return redirect(next)
        # if the user does not exist or the password is incorrect
        else:
            # flash an error message and redirect to login form
            flash('Invalid email address or password')
            # blank out the password in the form before re-rendering it
            form.password.data = ""
            return render_template('login.html', form=form), 422
    # flash error messages and redirect to get login form again
    for field, errors in form.errors.items():
        for msg in errors:
            flash(f"{field}: {msg}")
    # blank out the password in the form before re-rendering it
    form.password.data = ""
    return render_template('login.html', form=form), 422

@auth.get('/')
@login_required
def index():
    return render_template('index.html')

@auth.get('/logout/')
@login_required
def get_logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('index'))
