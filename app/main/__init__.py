#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : __init__.py.py
# @Time      : 2018/10/24 17:53
# @software  : PyCharm

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes