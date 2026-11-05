from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, SubmitField, EmailField, StringField
from wtforms.validators import InputRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField("Username: ", validators=[InputRequired(), Length(min=3, max=32)])
    email = EmailField("Email: ", validators=[InputRequired(), Email()])
    password = PasswordField("Password: ", 
        validators=[InputRequired(), Length(min=8, max=128)])
    confirm_password = PasswordField("Confirm Password: ", 
        validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = EmailField("Email: ", validators=[InputRequired(), Email()])
    password = PasswordField("Password: ", 
        validators=[InputRequired(), Length(min=8, max=128)])
    submit = SubmitField("Login")
