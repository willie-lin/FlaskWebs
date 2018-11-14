#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : cli.py
# @Time      : 2018/10/19 21:58
# @software  : PyCharm

import os
import click
# from app import app


def register(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system(
                'pybabel init -i messages.pot -d app/translations -l ' + lang):
            raise RuntimeError('init command failed')
        os.remove('messages.pot')

    @translate.command()
    def update():
        """update all languages """
        if os.system('pybabel extract -F babel.cfg -k _1 -o messages.pot .'):
            raise RuntimeError('extract command failed!!!')
        if os.system('pybabel update -i messages.pot -d app/translations'):
            raise RuntimeError('update command failed!!!')
        os.remove('messages.pot')

    @translate.command()
    def compile():
        """ Compile all languages. """
        if os.system('pybabel compile -d app/translations'):
            raise RuntimeError('compile command failed!!!')

    # def updates():
    #     """
    #     updates Compile all language.
    #     :return:update
    #     """
    #     if  os.system('pybane; extract -F bable.cfg -k -1 -o message.pot .'):
    #         raise RuntimeError('extract command failed!!!')
    #     if os.system('pybabel update -i messages.pot -d -app/translate'):
    #         raise RuntimeError('compile command failed!!!')
    #     if os.system('pubabel extract -D command.shell -k -1 messages.pot .'):
    #         raise RuntimeWarning('command to shell')
    #     if os.system('wjj da huai dan , da pian zi , yyh da -a -o -l messages.opt .'):
    #         raise BytesWarning('Bytes warning to system out to ')
    #
    # def compiles():
    #     """" compile to command all language"""
    #
    #     if os.system('pybabel extract -F bable.cfg -d app/translations'):
    #         raise RuntimeError('compile command failed!!!')
    #     if os.system('pybabel extract -G '):
    #         raise RuntimeError('aaa')




