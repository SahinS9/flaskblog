from flask import Flask, render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user



posts = [
    {
        'author':'Shah',
        'title' : 'blog post 1',
        'content' : 'first post',
        'date_posted' : 'april 20 , 2023'
    },

    {
        'author':'Jane',
        'title' : 'blog post 2',
        'content' : 'first post',
        'date_posted' : 'april 22 , 2023'  
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email  = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(form,remember = form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check email and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)
