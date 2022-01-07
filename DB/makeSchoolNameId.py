import json
import csv

json_open_baseball = open('result/nameFixedBaseball.json', 'r')
json_load_baseball = json.load(json_open_baseball)

json_open_brass = open('schoolNameKeySorted.json', 'r')
json_load_brass = json.load(json_open_brass)

nameList = set()

for item in json_load_baseball:
    nameList.add(item['fullName'])

for name in json_load_brass:
    if len(json_load_brass[name]['name']) >= 1:
        nameList.add(json_load_brass[name]['name'][0])

"""
data = {}
id = 0
for name in list(nameList):
    if name != "":
        #data.append({"name": name, "id": id})
        data[name] = id
        id += 1

with open('nameTest.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)


"""
data = []
id = 0
for name in list(nameList):
    if name != "":
        data.append({"name": name, "id": id})
        id += 1


field_name = ['name', 'id']
with open(r'dic_test.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_name)
    writer.writeheader()
    writer.writerows(data)
