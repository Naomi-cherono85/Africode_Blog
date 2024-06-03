from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(max=20,min=2)])
    email =StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user= User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("the username you entered is taken choose a different one")

class loginForm(FlaskForm):
    email =StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
    def validate_email(self, email):
        user= User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("the  email you entered is taken choose a different one")

















