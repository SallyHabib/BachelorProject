from pymongo import MongoClient
import json
import csv
client = MongoClient("mongodb://SallyHabib1:Jesus2016@ds119810.mlab.com:19810/mylife")
db = client['mylife']
coll = db['facebook']
export= db.facebook.find()
out= csv.writer(open('users.csv', 'wb'),delimiter=(','))
b=[]
a=[]
for items in export:
    a.append(items['name'])
    a.append(items['email'])
    a.append(items['_id'])
    a.append(items['birthday'])
    b.append(a)
    out.writerows(b)
    a=[]
    b=[]