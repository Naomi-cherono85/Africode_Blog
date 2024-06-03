from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = '12bce8a09268cb808a497caeff4d450e'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
bcrypt= Bcrypt(app)
login_manager=LoginManager(app)

db = SQLAlchemy(app)
from app import route