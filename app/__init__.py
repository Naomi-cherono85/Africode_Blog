from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)

# Configuration
app.config["SECRET_KEY"] = '12bce8a09268cb808a497caeff4d450e'


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'naomicherono892@gmail.com'
app.config['MAIL_PASSWORD'] = 'alvn vgbc tmgz pwjg'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
mail = Mail(app)


# Avoid circular imports
from app import route
