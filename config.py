#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : config.py
# @Time      : 2018/6/19 17:53
# @software  : PyCharm

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SECRET_KEY我作为唯一配置项添加的配置变量是大多数Flask应用程序中的重要组成部分。
    # Flask及其一些扩展使用密钥的值作为加密密钥，用于生成签名或令牌。
    # Flask-WTF扩展使用它来保护网页表单免受名为Cross-Site Request Forgery
    # 或CSRF（发音为“seasurf”）的恶意攻击。顾名思义，秘密密钥应该是秘密的，
    # 因为由它产生的令牌和签名的强度取决于知道它的应用程序的可信维护者之外的任何人。
    #
    # 秘密密钥的值被设置为由两个项组成的表达式，由or操作员加入。
    # 第一个术语查找也称为环境变量的值SECRET_KEY。第二项只是一个硬编码的字符串。
    # 这是一种你会看到我经常重复配置变量的模式。这个想法是首选来自环境变量的值，
    # 但如果环境没有定义变量，那么将使用硬编码字符串。
    # 在开发此应用程序时，安全性要求较低，因此您可以忽略此设置并使用硬编码字符串。
    # 但是，当这个应用程序部署在生产服务器上时，我将在环境中设置一个独特且难以猜测的值，
    # 以便服务器拥有一个别人不知道的安全密钥。
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_SERVER = 'smtp.126.com'
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_PORT = 25
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_USERNAME = 'yyhmmwan@126.com'
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_PASSWORD = '520134yyhmmwan'
    ADMINS = ['yyhmmwan@126.com']
    POSTS_PER_PAGE = 10