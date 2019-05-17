from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import current_user, login_user, logout_user

from app.models import db, User
from .forms import LoginForm, SignupForm


module = Blueprint('user', __name__)


@module.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('link.index'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Не валидный email или пароль.')
            return redirect(url_for('user.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('link.index'))
    return render_template('login.html', form=form)


@module.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('link.index'))


@module.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('link.index'))
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('link.index'))
    return render_template('signup.html', form=form)


