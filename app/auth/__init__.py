#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : __init__.py.py
# @Time      : 2018/10/24 15:51
# @software  : PyCharm

from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes