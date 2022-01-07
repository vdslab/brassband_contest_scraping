
"""
名前の修正
都道府県が空のところを埋める
"""
import json

json_open_brass = open('barassBand.json', 'r')
json_load_brass = json.load(json_open_brass)

json_open_name = open('schoolNameKey.json', 'r')
json_load_name = json.load(json_open_name)

json_open_sorted_name = open('doubleNameSorted.json', 'r')
json_load_sorted_name = json.load(json_open_sorted_name)

for year in json_load_brass:
    for item in year["data"]:
        if len(json_load_name[item["name"]]["name"]) > 1:
            item["name"] = json_load_sorted_name[item["name"]]["name"][0]
        item["prefecture"] = json_load_name[item["name"]]["prefecture"]


with open('fullBrassBand.json', 'w') as f:
    json.dump(json_load_brass, f, ensure_ascii=False)
