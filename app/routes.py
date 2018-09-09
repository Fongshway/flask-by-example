from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {
                'username': 'John'
            },
            'body': 'Beautiful day in Seattle!'
        }, {
            'author': {
                'username': 'Viola'
            },
            'body': 'The Avengers movie was so cool!'
        }, {
            'author': {
                'username': 'Test'
            },
            'body': 'This is a test'
        }
    ]
    return render_template("index.html", title="Home", posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

        # If the login URL does not have a next argument or includes a
        # next argument that is set to a full URL that includes a domain
        # name, then redirect the user to the index page.
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
