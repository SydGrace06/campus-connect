from __future__ import annotations

from pathlib import Path
import sys
from typing import cast

#Import cryptography and hash
from cryptography.fernet import Fernet
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher
from pwdlib.hashers.argon2 import Argon2Hasher

#Flask imports
from flask import Flask, render_template, url_for, redirect
from flask import request, flash
from flask_login import (
    LoginManager, login_required, login_user, logout_user, current_user
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from forms import RegisterForm, LoginForm

scriptdir: Path = Path(__name__).resolve().parent

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


dbfile:  Path = scriptdir / "users.db"
pepfile: Path = scriptdir / "pepper.bin"

#Load in the pepper and give it to the Hasher function
with open(pepfile, 'rb') as fin:
  pepper_key = fin.read()

pwd_hasher = UpdatedHasher(pepper_key)

# Configure the Flask Application
app = Flask(__name__)

#TODO : Ensure this is in the correct location
# NOTE: in a practical solution, this would be in an .appenv file as shown
app.config['SECRET_KEY'] = 'correcthorsebatterystaple'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbfile}"


db = SQLAlchemy(app)

from models import User

# Prepare and connect the LoginManager to this app
login_manager = LoginManager()
login_manager.init_app(app)

# function name of the route that has the login form (so it can redirect users)
login_manager.login_view = 'get_login' # type: ignore
login_manager.session_protection = "strong"

# function that takes a user id and as a string and returns that user
@login_manager.user_loader
def load_user(uid: str) -> User|None:
    return get_user(uid=int(uid))

# define a helper function that loads uses based on id or email
def get_user(uid: int|None = None, email: str|None = None) -> User|None:
    if uid is not None:
        return db.session.get(User, uid)
    else:
        return db.session.scalar(db.select(User).filter_by(email=email))

###############################################################################
# Database Setup
###############################################################################

# remember that all database operations must occur within an app context
with app.app_context():
    # this is only needed if the database doesn't already exist
    db.create_all()

###############################################################################
# Route Handlers
###############################################################################

@app.get('/register/')
def get_register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.post('/register/')
def post_register():
    form = RegisterForm()
    if form.validate():
        try:
            # load the email and password from the form
            email: str = cast(str, form.email.data)
            password: str = cast(str, form.password.data)
            user = User(email=email, password=password) # type:ignore
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

@app.get('/login/')
def get_login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.post('/login/')
def post_login():
    form = LoginForm()
    if form.validate():
        # try to get the user associated with this email address
        user: User|None = get_user(email=form.email.data)
        # if this user exists and the password matches
        if user is not None and user.verify_password(str(form.password.data)):
            # log this user in through the login_manager
            login_user(user)
            # redirect the user to the page they wanted or the home page
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('index')
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

@app.get('/')
def index():
    return render_template('home.html')

@app.get('/logout/')
@login_required
def get_logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('index'))
