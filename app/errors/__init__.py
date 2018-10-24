#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : __init__.py.py
# @Time      : 2018/10/24 14:34
# @software  : PyCharm

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers