from flask_wtf import FlaskForm,CSRFProtect
from wtforms import StringField,PasswordField,SubmitField,BooleanField, TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from app.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


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
    def validate_email(self, email):
        user= User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("the  email you entered is taken choose a different one")

class LoginForm(FlaskForm):
    email =StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
    
class UpdateAccountForm (FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(max=20,min=2)])
    email =StringField('Email',validators=[DataRequired(),Email()])
    picture=FileField('picture', validators=[FileAllowed(['jpeg', 'jpg', 'png'])])
    submit = SubmitField('update')
    
    def validate_username(self, username):
        if username.data != current_user.username :
            user= User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("the username you entered is taken choose a different one")
            
    def validate_email(self, email):
        if email.data != current_user.email :
            user= User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("the email you entered is taken choose a different one")

class PostForm(FlaskForm):
       title=StringField('Title', validators=[DataRequired()])
       content= TextAreaField('Content', validators=[DataRequired()])
       submit=SubmitField('Post')



class RequestResetForm(FlaskForm):
        email =StringField('Email',validators=[DataRequired(),Email()])
        submit = SubmitField('request password reset')
        def validate_email(self, email):
                user= User.query.filter_by(email=email.data).first()
                if user is None:
                    raise ValidationError("There is no account with that email")


class ResetPasswordForm(FlaskForm):   
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')]) 
    submit = SubmitField('reset password')      
    











