#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : translate.py
# @Time      : 2018/10/23 11:23
# @software  : PyCharm
from app import app
from flask_babel import _
import json, random, hashlib, http.client
from flask_babel import _
from app import app
from urllib import parse

# def translate(text, source_language, dest_language):


def translate(q, fromLang, toLang):
    if 'APP_ID' not in app.config or \
            not app.config['APP_ID']:
        return _('Error: the translator service is not configured')
    if 'BD_TRANSLATOR_KEY' not in app.config or \
            not app.config['BD_TRANSLATOR_KEY']:
        return _('Error: the translator service is not configured')
    # auth = {'BD_TRANSLATOR_KEY': app.config['BD_TRANSLATOR_KEY']}
    appid = app.config['APP_ID']
    print(appid)
    secretKey = app.config['BD_TRANSLATOR_KEY']
    print(secretKey)
    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)

    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    print(myurl)

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        response = httpClient.getresponse()  # response是HTTPResponse对象
        r = response.read().decode('utf-8')
        d = json.loads(r)

        l = d['trans_result']
        l1 = l[0]['dst']

        return (l1)
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()


    # httpClient = None
    # myurl = '/api/trans/vip/translate'
    # q = 'apple'
    # fromLang = 'en'
    # toLang = 'zh'
    # salt = random.randint(32768, 65536)
    #
    # sign = appid + q + str(salt) + secretKey
    # m1 = md5.new()
    # m1.update(sign)
    # sign = m1.hexdigest()
    # myurl = myurl + '?appid=' + appid + '&q=' + urllib.quote(
    #     q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    #
    # try:
    #     httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    #     httpClient.request('GET', myurl)
    #
    #     # response是HTTPResponse对象
    #     response = httpClient.getresponse()
    #     print
    #     response.read()
    # except Exception, e:
    #     print
    #     e
    # finally:
    #     if httpClient:
    #         httpClient.close()


