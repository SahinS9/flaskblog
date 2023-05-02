from flask import Flask, render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm




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
        flash(f'Account Created for{form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == 'password':    
            flash('Welcome HEY!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title = 'Login', form = form)
