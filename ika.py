#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
import http
from http.cookiejar import CookieJar
import codecs
import settings

def printJson(url): # Jsonを取得してprint
    cookie = "iksm_session=" + settings.iksm_session
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    opener.addheaders.append(("Cookie", cookie))
    res = opener.open(url)
    print (codecs.decode(res.read(), 'unicode-escape'))

#printJson("https://app.splatoon2.nintendo.net/api/data/stages") # 今のステージの取得
#printJson("https://app.splatoon2.nintendo.net/api/festivals/active") # フェスの情報の取得？
#printJson("https://app.splatoon2.nintendo.net/api/schedules") # スケジュールの取得
#printJson("https://app.splatoon2.nintendo.net/api/records") # 今の装備や塗った面積等の取得
#printJson("https://app.splatoon2.nintendo.net/api/timeline") # フレンドの状況？
#printJson("https://app.splatoon2.nintendo.net/api/onlineshop/merchandises") # ギアショップの情報

def getResult():
    printJson("https://app.splatoon2.nintendo.net/api/results") # 各バトルのデータ
