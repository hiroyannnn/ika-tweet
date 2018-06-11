import json,sys
import twitter_tweet

f = open("/vagrant/workspace/ika_result.json", 'r')
#f = sys.stdin.readline()
print(f)
#ココ重要！！
json_data = json.load(f,strict=False) #JSON形式で読み込む
#result = max(json_data['results']['battle_number'])

mode = json_data['results'][0]['game_mode']['name']
wep = json_data['results'][0]['player_result']['player']['weapon']['name']
#print(json_date.get("unique_id"))
#print('json_dict:{}'.format(type(json_data)))

python3.6 /vagrant/workspace/twitter_tweet.py mode wep