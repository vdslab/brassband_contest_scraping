import json

json_open_name = open('schoolName.json', 'r')
json_load_name = json.load(json_open_name)

data = {}

for item in json_load_name:
    if len(item["name"]) == 0 or len(item["name"]) == 1:
        continue
    for i in range(len(item["name"])):
        data[item["name"][i]] = {
            "prefecture": item["prefecture"], "name": item["name"]}


with open('doubleName.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)
