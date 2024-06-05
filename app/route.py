from PIL import Image
import os
import secrets
from flask import render_template, url_for,flash,redirect,request
from app.form import RegistrationForm, loginForm, updateAccountForm
from app import app, bcrypt, db
from app.models import User
from flask_login import login_user, logout_user, current_user, login_required




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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = loginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(email=form.email.data).first() 
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page= request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash('Login unsuccessful.Please check username and password!','danger')
    return render_template("login.html", title="Login",form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
    

@app.route("/account", methods=['POST', 'GET'])
@login_required
def account():
    form= updateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file= picture_file
        current_user.username= form.username.data
        current_user.email=form.email.data 
        db.session.commit()
        flash("your account has been successfully  updated", "success")
        return redirect(url_for("account"))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file= url_for('static', filename='profile_pics/' + current_user.image_file)
    
    return render_template("account.html", title="Account", image_file=image_file, form=form)

