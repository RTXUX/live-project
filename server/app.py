from flask import Flask, jsonify
from flask_cors import CORS
import csv
from functools import cmp_to_key
import json
app = Flask(__name__)
CORS(app)
keys=[]
entrys = []
toilet = []

def read_data():
    with open("../data/HaikouRestaurants.csv", "r", encoding="utf8") as f:
        a=csv.reader(f)
        headers = next(a)
        for b in a:
            entry={}
            value_s = b
            for i in range(len(headers)):
                entry[headers[i]]=value_s[i]
            entrys.append(entry)
    with open("../data/fuck.json", "r", encoding="utf8") as f:
        toilet1 = json.loads(f.read())
        for i in toilet1:
            toilet.append(toilet1)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/data/1')
def data1():
    cluster_by_loc = {}
    sorted_by_sold = sorted(entrys, key=lambda i: i["累计售出份数"], reverse=True)
    sorted_by_sold = list(sorted_by_sold)
    for i in range(len(entrys)):
        weight = 10 - int(i / 30)
        key = entrys[i]["所属地区"]

        # pattern1 = re.compile(r"(.*)(/.*)*")
        # p = pattern1.search(key)
        key = key.split('/')[0]
        cluster_by_loc[key] = cluster_by_loc.get(key, 0) + weight
    return jsonify(cluster_by_loc)

def cmp1(a,b):
    p1 = a["评分"]
    p2 = b["评分"]
    c1 = a["平均价格"]
    c2 = b["平均价格"]
    if p1>p2: return 1
    elif p1<p2: return -1
    else:
        if c1<c2: return 1
        elif c1>c2: return -1
        else: return 0

@app.route('/data/2')
def data2():
    t = {}
    t["<50"] = []
    t["50-100"] = []
    t["100-200"] = []
    t[">200"] = []
    for i in entrys:
        price = int(i["平均价格"])
        if price < 50:
            t.get("<50", []).append(i)
        elif 50 <= price and price < 100:
            t.get("50-100", []).append(i)
        elif 100 <= price and price < 200:
            t.get("100-200", []).append(i)
        else:
            t.get(">200", []).append(i)
    for i in t.keys():
        t[i] = list(sorted(t[i], key=cmp_to_key(cmp1), reverse=True))
    return jsonify(t)

@app.route('/data/3')
def data3():
    a = list(map(lambda x: {"lat": x["纬度"], "lng":x["经度"]}, entrys))
    for i in range(len(a)):
        a[i]["count"]=i+1
    return jsonify(a)

@app.route('/data/4')
def data4():
    return jsonify(toilet)

if __name__ == '__main__':
    read_data()
    app.config['JSON_AS_ASCII'] = False
    app.run()
