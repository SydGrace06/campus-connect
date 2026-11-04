from __future__ import annotations

from flask import Flask, request, session
from flask import redirect, url_for, render_template, flash
from routes.events import register_event_routes

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Enum as SQLEnum, Select, Integer, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from wtforms.fields import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired, NumberRange, Length

from collections.abc import Sequence
from pathlib import Path
from enum import Enum

from flask_login import login_required

from extensions import db, login_manager


app = Flask(__name__)

# Application configuration
scriptdir = Path(__file__).resolve().parent
dbfile = scriptdir / "users.db"

app.config['SECRET_KEY'] = 'batteryhorsestapler'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbfile}"

# Initialize extensions
db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = 'auth.get_login'
login_manager.session_protection = 'strong'

# Register authentication routes
from routes.auth import auth
app.register_blueprint(auth)

# Register event routes
from routes.events import register_event_routes
register_event_routes(app)

register_event_routes(app)

@app.route("/")
@login_required
def home():
    return render_template("index.html")

from models import User

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)