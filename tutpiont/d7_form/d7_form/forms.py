from flask_wtf import Form
from wtforms import StringField, IntegerField, SelectField, RadioField, TextAreaField, SubmitField, EmailField
from wtforms import validators, ValidationError


class ContactForm(Form):
    name = StringField('Name of student ', [validators.DataRequired("Name is required.")])
    gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
    address = TextAreaField("Address")
    email = EmailField("Email",[validators.DataRequired("Please enter your email")])
    age = IntegerField("age")
    language = SelectField('Languages', choices = [('cpp', 'C++'),('py', 'Python')])
    submit = SubmitField("Send")