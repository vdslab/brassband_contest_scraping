import csv
import json

prefectureName = [
    "北海道",
    "青森県",
    "岩手県",
    "宮城県",
    "秋田県",
    "山形県",
    "福島県",
    "栃木県",
    "茨城県",
    "千葉県",
    "東京都",
    "神奈川県",
    "新潟県",
    "群馬県",
    "山梨県",
    "埼玉県",
    "愛知県",
    "三重県",
    "岐阜県",
    "長野県",
    "静岡県",
    "福井県",
    "石川県",
    "富山県",
    "大阪府",
    "京都府",
    "兵庫県",
    "滋賀県",
    "奈良県",
    "和歌山県",
    "広島県",
    "岡山県",
    "山口県",
    "鳥取県",
    "島根県",
    "香川県",
    "高知県",
    "愛媛県",
    "徳島県",
    "福岡県",
    "佐賀県",
    "長崎県",
    "熊本県",
    "鹿児島県",
    "宮崎県",
    "大分県",
    "沖縄県",
    "函館地区",
    "日胆地区",
    "札幌地区",
    "空知地区",
    "旭川地区",
    "名寄地区",
    "北見地区",
    "釧路地区",
    "帯広地区",
    "留萌地区",
    "稚内地区",
]


data = {}
id = 0
for name in prefectureName:
    data[name] = id
    id += 1

with open('prefectureNameId.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)


"""
data = []
id = 0
for name in prefectureName:
    data.append({"name": name, "id": id})
    id += 1


field_name = ['name', 'id']
with open(r'prefectureNameId.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_name)
    writer.writeheader()
    writer.writerows(data)
"""
