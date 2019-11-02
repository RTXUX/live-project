import json
import csv
import re
from functools import cmp_to_key
keys=[]
entrys = []
cluster_by_loc = {}
  
def read_data():
    with open("meituanRestaurantsInfos/HaikouRestaurants - 副本.csv", "r", encoding="utf8") as f:
        a=csv.reader(f)
        headers = next(a)
        for b in a:
            entry={}
            value_s = b
            for i in range(len(headers)):
                entry[headers[i]]=value_s[i]
            entrys.append(entry)

def data1():
    sorted_by_sold = sorted(entrys, key=lambda i: i["累计售出份数"], reverse=True)
    sorted_by_sold = list(sorted_by_sold)
    for i in range(len(entrys)):
        weight = 10 - int(i / 30)
        key = entrys[i]["所属地区"]

        # pattern1 = re.compile(r"(.*)(/.*)*")
        # p = pattern1.search(key)
        key = key.split('/')[0]
        cluster_by_loc[key] = cluster_by_loc.get(key, 0) + weight

    with open('data1.json', "w", encoding="utf8") as fd:
        fd.write(json.dumps(cluster_by_loc, ensure_ascii=False))

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

def data2():
    t = {}
    t["<50"]=[]
    t["50-100"]=[]
    t["100-200"]=[]
    t[">200"]=[]
    for i in entrys:
        price = int(i["平均价格"])
        if price<50:
            t.get("<50",[]).append(i)
        elif 50<=price and price<100:
            t.get("50-100",[]).append(i)
        elif 100<=price and price<200:
            t.get("100-200",[]).append(i)
        else:
            t.get(">200",[]).append(i)
    for i in t.keys():
        t[i] = list(sorted(t[i], key = cmp_to_key(cmp1),reverse=True))
    with open('data2.json', "w", encoding="utf8") as fd:
        fd.write(json.dumps(t, ensure_ascii=False))
    pass



if __name__=="__main__":
    read_data()
    data1()
    data2()


    pass