
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import settings
from lib/requests_oauthlib import OAuth1Session
import json

# key
CK = settings.consumer_key
CS = settings.consumer_secret
AT = settings.token
AS = settings.token_secret
# ツイート投稿用のURL
url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"
# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)

def postTweetWithPicture():
    # ツイート本文
    files = {"media" : open('1.jpg', 'rb')}
    req_media = twitter.post(url_media, files = files)

    # レスポンスを確認
    if req_media.status_code != 200:
        print ("画像アップデート失敗: %s", req_media.text)
        exit()

    # Media ID を取得
    media_id = json.loads(req_media.text)['media_id']
    print ("Media ID: %d" % media_id)

    # Media ID を付加してテキストを投稿
    params = {'status': '画像投稿テスト', "media_ids": [media_id]}
    req_media = twitter.post(url_text, params = params)

    # 再びレスポンスを確認
    if req_media.status_code != 200:
        print ("テキストアップデート失敗: %s", req_text.text)
        exit()

    print ("OK")

def postTweetText(text):
    # ツイート本文
    params = {"status": text}
    req = twitter.post(url_text, params = params)

    # レスポンスを確認
    if req.status_code == 200:
        print ("OK")
    else:
        print ("Error: %d" % req.status_code)

def getTimeLine():
    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
    params = {'count': 100}

    # ツイート本文
    req = twitter.get(url, params = params)
    # レスポンスを確認
    if req.status_code == 200:
        print ("OK")
    else:
        print ("Error: %d" % req.status_code)
    tweets = json.loads(req.text)

### Functions                                                                                                                                                     
def main():
    tweets = getTimeLine()
    for tweet in tweets["statuses"]:
        tweet_id = tweet[u'id_str']
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']
        user_description = tweet[u'user'][u'description']
        screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']
        #print ("tweet_id:", tweet_id)
        print ("text:", text)
        print ("created_at:", created_at)
        #print ("user_id:", user_id)
        #print ("user_desc:", user_description)
        #print ("screen_name:", screen_name)
        print ("user_name:", user_name)
    return
### Execute                                                                                                                                                       
if __name__ == "__main__":
    main()