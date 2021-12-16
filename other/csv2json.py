import json
import csv

json_list = []

# CSV ファイルの読み込み
with open('baseballRowData.csv', 'r', encoding='shift_jis') as f:
    for row in csv.DictReader(f):
        json_list.append(row)

# JSON ファイルへの書き込み
with open('output.json', 'w') as f:
    json.dump(json_list, f, ensure_ascii=False)
