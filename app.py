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

# update for our forms:
# from forms import AuthorForm, BookForm
# from models import db, Author, Book

app = Flask(__name__)

register_event_routes(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)