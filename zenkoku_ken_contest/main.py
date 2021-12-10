import json
from collections import OrderedDict
import pprint

with open("brassBand/2013-2017_zenkoku_shibu_ken.json") as f:
    df = json.load(f)

pprint.pprint(df)

print(df)
