import pandas as pd
import json
data = pd.read_csv("toilet.csv")
tar = {}
count ={}
res = {}
area = data.business_area.values
rating = data.biz_ext.values
for i in range(900):
    tar_rating = eval(rating[i])
    if(area[i] == str([]) or tar_rating['rating']  == []):
        continue
    if (area[i] in tar):
        count[area[i]]+=1
        tar[area[i]]+=float(tar_rating['rating'])
    else:
        count[area[i]]=1
        tar[area[i]]=float(tar_rating['rating'])
for i in tar:
    res[i] = [tar[i]/count[i],count[i]]
with open('number.json','w') as A_obj:
    json.dump(res,A_obj, ensure_ascii=False)
    print(res)