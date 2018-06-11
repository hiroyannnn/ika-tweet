
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import settings
from requests_oauthlib import OAuth1Session
import json
import os

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

# ツイート本文
#path = '2018051923315501-C616B031331154665D639EF16DA76BC0.mp4'
#print(os.path.getsize(path)
#dataw = {"command" : "INIT",
#    "media_type" : "video/mp4",
#    "total_bytes" : os.path.getsize(path)
#}l;/
argvs = sys.argv  # コマンドライン引数を格納したリストの取得

text = argvs[0] + argvs[1]
files = {
    "media" : open('85.jpg', 'rb')
}
req_media = twitter.post(url_media, files = data)
# レスポンスを確認
if req_media.status_code != 200:
    print ("画像アップデート失敗: %s", req_media.text)
    exit()

# Media ID を取得
media_id = json.loads(req_media.text)['media_id']
print ("Media ID: %d" % media_id)

# Media ID を付加してテキストを投稿
params = {'status': text, "media_ids": [media_id]}
req_media = twitter.post(url_text, params = params)

# 再びレスポンスを確認
if req_media.status_code != 200:
    print ("テキストアップデート失敗: %s", req_text.text)
    exit()

print ("OK")
