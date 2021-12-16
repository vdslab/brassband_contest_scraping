import json

json_open = open('baseball.json', 'r')
json_load = json.load(json_open)

for item in json_load:
    if item['fullName'][:2] == "県立":
        print(item['fullName'][:2])
        item['fullName'] = item['prefecture'] + item['fullName']

with open('nameFixed.json', 'w') as f:
    json.dump(json_load, f, ensure_ascii=False)
