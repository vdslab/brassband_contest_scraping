import json
import csv
from os import name

json_open_school = open('schoolNameId.json', 'r')
json_load_school = json.load(json_open_school)

json_open_prefecture = open('prefectureNameId.json', 'r')
json_load_prefecture = json.load(json_open_prefecture)

json_open_baseball = open('result/nameFixedBaseball.json', 'r')
json_load_baseball = json.load(json_open_baseball)

nameList = set()


data = []

for item in json_load_baseball:

    prefecture = item["prefecture"]
    if prefecture == "京都" or prefecture == "大阪":
        prefecture += "府"
    elif not(prefecture == "北北海道" or prefecture == "南北海道" or prefecture == "東東京" or prefecture == "西東京"):
        prefecture += "県"

    print(prefecture,
          json_load_prefecture[prefecture], item["fullName"])

    try:
        name = json_load_school[item["fullName"]]
    except KeyError:
        name = item["shortName"]

    data.append({"schoolId": name,
                "prefecture": json_load_prefecture[prefecture], "year": item["year"], "nationalBest": item["nationalBest"], "regionalBest": item["regionalBest"]})

"""
with open('brassBandIdData.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)
"""


field_name = ['schoolId', 'prefecture', 'year', 'nationalBest', 'regionalBest']
with open(r'dic_test.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_name)
    writer.writeheader()
    writer.writerows(data)
