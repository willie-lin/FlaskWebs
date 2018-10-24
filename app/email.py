#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : email.py
# @Time      : 2018/10/17 14:53
# @software  : PyCharm
from threading import Thread
from flask_mail import Message
from app import mail
from flask import current_app
from flask import render_template
from flask_babel import _


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # mail.send(msg)
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()


