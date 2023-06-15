from flask_wtf import Form, BooleanField, StringField, validators, Passwordfield, EqualTo, SubmitField, Email, Length, InputRequir
from flask import Flask


class RegistrationForm(Form):
    username = StringField('Username',
                           [validators.Length(min=2, max=20), validators.InputRequired()])
    email = StringField('Email',
                        [validators.InputRequired(), validators.Email()])
    Password = Passwordfield('Password',
                             [validators.InputRequired()])
    confirm_password = Passwordfield('Confirm Password',
                                     [validators.InputRequired(), EqualTo('password')])
    sumbit = SubmitField('Sign Up')


class LoginForm(Form):
    email = StringField('Email',
                        [validators.InputRequired(), validators.Email()])
    Password = Passwordfield('Password',
                             [validators.InputRequired()])
    remember = BooleanField('Remember Me')
    sumbit = SubmitField('Login')
