# coding: utf-8
# json モジュールを使ってみる
 
# json モジュールをインポート
import json
 
# jsonファイルを読み込む
f = open("/vagrant/workspace/ika_result.json")
# jsonデータを読み込んだファイルオブジェクトからPythonデータを作成
data = json.load(f,strict=False)
# ファイルを閉じる
f.close()
 
# 普通に表示
print("普通に表示")
print(data)