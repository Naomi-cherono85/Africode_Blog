from flask import Flask, render_template, url_for,flash,redirect
from app.form import RegistrationForm, loginForm
from app import app, bcrypt, db
from app.models import User
from flask_login import login_user, logout_user, current_user




posts=[

    {"author":"Naomi", 
     "title":"the great",
     "content":"this is my first blog", 
     "date_posted":"may 27th"
     },
     {"author":"dolly", 
     "title":"nice",
     "content":"is a second blog", 
     "date_posted":"may 27th"
     },
     {"author":"benz", 
     "title":"nice",
     "content":"this is my second blog", 
     "date_posted":"may 27th"
     },
     {"author":"gladwell", 
     "title":"cool",
     "content":"this is my third blog", 
     "date_posted":"may 27th"
     }
       ]

@app.route("/")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password= bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user=User(username=form.username.data, email=form.email.data, password= hash_password)

        db.session.add(user)
        db.session.commit()

        flash(f'your account has been created. You can login now','success')
        return redirect(url_for("login"))
    return render_template("register.html", title="Register",form=form)


@app.route("/login",methods=['GET','POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(email=form.email.data).first() 
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("home"))
        else:
            flash('Login unsuccessful.Please check username and password!','danger')
    return render_template("login.html", title="Login",form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))