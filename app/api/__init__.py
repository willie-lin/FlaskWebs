#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : __init__.py.py
# @Time      : 2018/11/14 17:56
# @software  : PyCharm

from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import users ,errors, tokens
