#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : errors.py
# @Time      : 2018/6/20 20:24
# @software  : PyCharm

from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500