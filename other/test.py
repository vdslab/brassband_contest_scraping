import json

json_open_baseball = open('result/nameFixedBaseball.json', 'r')
json_load_baseball = json.load(json_open_baseball)

json_open_brass = open('other/schoolName.json', 'r')
json_load_brass = json.load(json_open_brass)

nameList = set()

for item in json_load_baseball:
    nameList.add(item['fullName'])

for item in json_load_brass:
    if len(item['name']) > 0:
        nameList.add(item['name'][0])


data = {"name": list(nameList)}

with open('nameTest.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)
