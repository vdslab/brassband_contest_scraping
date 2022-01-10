import json
import csv
from os import name

json_open_school = open('schoolNameId.json', 'r')
json_load_school = json.load(json_open_school)

json_open_prefecture = open('prefectureNameId.json', 'r')
json_load_prefecture = json.load(json_open_prefecture)

json_open_brass = open('fullBrassBand.json', 'r')
json_load_brass = json.load(json_open_brass)

nameList = set()


data = []

for item in json_load_brass:
    # print(item)
    print(item["name"])
    data.append({"schoolId": json_load_school[item["name"]], "prefectureId": json_load_prefecture[item["prefecture"]], "year": item["year"],
                 "prize": item["prize"], "last": item["last"], "representative": item["representative"]})

"""
with open('brassBandIdData.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)
"""


field_name = ['schoolId', 'prefectureId', 'year', 'prize',
              'last', 'representative']
with open(r'brass_test.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_name)
    writer.writeheader()
    writer.writerows(data)
