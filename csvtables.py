from pymongo import MongoClient
import json
import csv
client = MongoClient("mongodb://SallyHabib1:Jesus2016@ds119810.mlab.com:19810/mylife")
db = client['mylife']
coll = db['facebook']
posts= db.posts.find()
out= csv.writer(open('user_posts.csv', 'wb'),delimiter=(','))
b=[]
a=[]
for items in posts:
    a.append(items['message'].encode('utf-8'))
    a.append(items['story'].encode("utf-8"))
    a.append(items['_id'].encode("utf-8"))
    a.append(items['tags'])
    a.append(items['created_time'])
    b.append(a)
    out.writerows(b)
    a=[]
    b=[]
likes= db.likes.find()
out= csv.writer(open('user_likes.csv', 'wb'),delimiter=(','))
b=[]
a=[]
for items in likes:
    a.append(items['name'].encode("utf-8"))
    a.append(items['about'].encode("utf-8"))
    a.append(items['category'].encode("utf-8"))
    b.append(a)
    out.writerows(b)
    a=[]
    b=[]

events= db.events.find()
out= csv.writer(open('user_events.csv', 'wb'),delimiter=(','))
b=[]
a=[]
for items in events:
    a.append(items['name'].encode("utf-8"))
    a.append(items['desc'].encode("utf-8"))
    a.append(items['status'].encode("utf-8"))
    b.append(a)
    out.writerows(b)
    a=[]
    b=[]