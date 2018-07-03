
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import tweepy
import settings
import sys

# key
CONSUMER_KEY = settings.consumer_key
CONSUMER_SECRET = settings.consumer_secret
ACCESS_TOKEN = settings.token
ACCESS_SECRET = settings.token_secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 
api = tweepy.API(auth)
argvs = sys.argv  # コマンドライン引数を格納したリストの取得

text = "I'm playing " +argvs[1] + " with " + argvs[2]
api.update_with_media(filename='./85.jpg',status=text)

print('Done!')
