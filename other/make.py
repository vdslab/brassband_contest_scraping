import json

json_open = open('dbData.json', 'r')
json_load = json.load(json_open)

data = []

for name in json_load:
    data.append(json_load[name])

with open('data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)
