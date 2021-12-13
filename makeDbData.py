import json
from collections import OrderedDict

ken = ['函館地区', '日胆地区', '札幌地区', '空知地区', '旭川地区', '名寄地区', '北見地区', '釧路地区', '帯広地区', '留萌地区', '稚内地区', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県', '栃木県', '茨城県', '千葉県', '神奈川県', '新潟県', '群馬県', '山梨県', '埼玉県', '東京都', '愛知県',
       '三重県', '岐阜県', '長野県', '静岡県', '福井県', '石川県', '富山県', '大阪府', '京都府', '兵庫県', '滋賀県', '奈良県', '和歌山県', '広島県', '岡山県', '山口県', '鳥取県', '島根県', '香川県', '高知県', '愛媛県', '徳島県', '福岡県', '佐賀県', '長崎県', '熊本県', '鹿児島県', '宮崎県', '大分県', '沖縄県']

shibu = ['北海道', '東北', '東関東', '西関東', '東京', '北陸', '東海', '関西', '中国', '四国', '九州']

zenkoku = ["全国"]

with open("zenkoku_ken_contest/brassBand/2013-2017_zenkoku_shibu_ken.json") as f:
    shibuData = json.load(f)

with open("contest/2013-2017_chiku.json") as f:
    chikuData = json.load(f)

allData = shibuData+chikuData

divideYearData = {"2013": [], "2014": [], "2015": [], "2016": [], "2017": []}

allShortData = {}

for item in allData:
    if item["school"] == None:
        continue

    s = item["school"]+item["year"]

    if not s in allShortData:
        last = "地区"
        if item["consertArea"] in zenkoku:
            last = "全国"
        elif item["consertArea"] in shibu:
            last = "支部"
        elif item["consertArea"] in ken:
            last = "都道府県"

        if item["consertArea"] in ken and (item["consertArea"] != "北海道" or item["consertArea"] != "東京"):
            prefecture = item["consertArea"]
        elif item["consertArea"] == "北海道":
            prefecture = "北海道"
        elif item["consertArea"] == "東京":
            prefecture = "東京"

        d = {"name": item["school"], "prize": item["prize"],
             "prefecture": prefecture, "last": last, "representative": item["representative"], "year": item["year"]}

        allShortData[s] = d

    else:
        prefecture = ""
        if item["consertArea"] in ken and (item["consertArea"] != "北海道" or item["consertArea"] != "東京"):
            allShortData[s]["prefecture"] = item["consertArea"]
        elif item["consertArea"] == "北海道":
            allShortData[s]["prefecture"] = "北海道"
        elif item["consertArea"] == "東京":
            allShortData[s]["prefecture"] = "東京"

        if item["consertArea"] == "全国":
            allShortData[s]["last"] = "全国"
            allShortData[s]["prize"] = item["prize"]
            allShortData[s]["representative"] = item["representative"]
        elif (allShortData[s]["last"] == "地区" or allShortData[s]["last"] == "都道府県") and item["consertArea"] in shibu:
            allShortData[s]["last"] = "支部"
            allShortData[s]["prize"] = item["prize"]
            allShortData[s]["representative"] = item["representative"]
        elif allShortData[s]["last"] == "地区" and item["consertArea"] in ken:
            allShortData[s]["last"] = "都道府県"
            allShortData[s]["prize"] = item["prize"]
            allShortData[s]["representative"] = item["representative"]


with open("dbData2.json", "w") as f:
    json.dump(allShortData, f, indent=2, ensure_ascii=False)
