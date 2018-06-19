#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : routes.py
# @Time      : 2018/6/19 17:08
# @software  : PyCharm

from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    post = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Protland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=post)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.password.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
