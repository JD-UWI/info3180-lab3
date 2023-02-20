
from flask import render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    fullname = StringField('Full Name', validators=[InputRequired()])
    email = StringField('E-mail', validators=[InputRequired()])
    subject = StringField('Subject', validators=[InputRequired()])
    message = StringField('Message', validators=[InputRequired()])
