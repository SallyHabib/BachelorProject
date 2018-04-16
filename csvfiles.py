from pymongo import MongoClient
import json
import csv
client = MongoClient("mongodb://SallyHabib1:Jesus2016@ds119810.mlab.com:19810/mylife")
db = client['mylife']
coll = db['facebook']
kinds=[]

with open('users.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        faceID=row[2]
        export= db.posts.find({"users_id":faceID})
        out= csv.writer(open('user_posts_'+faceID+'.csv', 'wb'),delimiter=(','))
        b=[]
        a=[]
        for items in export:
            a.append(items['message'].encode("utf-8"))
            a.append(items['story'].encode("utf-8"))
            a.append(items['_id'].encode("utf-8"))
            a.append(items['created_time'])
            if(not(items['message']=="below")):
                if(items['story'].__contains__("updated")):
                    a.append("updated")
                    kinds.append("updated")
                else:
                    if(items['story'].__contains__("shared")):
                        a.append("shared")
                        kinds.append("shared")
                    else:
                        if(items['story'].__contains__("added")):
                            a.append("added")
                            kinds.append("added")
                        else:
                            if(items['story'].__contains__("celebrating")):
                                a.append("shared")
                                kinds.append("shared")
                            else:
                                a.append("posted")
                                kinds.append("posted")
            else:
                if(items['story'].__contains__("shared")):
                    a.append("shared")
                    kinds.append("shared")
                else:
                    if(items['story'].__contains__("updated")):
                        a.append("updated")
                        kinds.append("updated")
                    else:
                        if(items['story'].__contains__("added")):
                            a.append("added")
                            kinds.append("added")
            b.append(a)
            out.writerows(b)
            a=[]
            b=[]
        likes= db.likes.find({"user_id":faceID})
        out= csv.writer(open('user_likes_'+faceID+'.csv', 'wb'),delimiter=(','))
        c=[]
        d=[]
        for items in likes:
            c.append(items['name'].encode("utf-8"))
            c.append(items['about'].encode("utf-8"))
            c.append(items['category'].encode("utf-8"))
            d.append(c)
            out.writerows(d)
            c=[]
            d=[]
        events= db.events.find({"user_id":faceID})
        out= csv.writer(open('user_events_'+faceID+'.csv', 'wb'),delimiter=(','))
        e=[]
        f=[]
        for items in events:
            e.append(items['name'].encode("utf-8"))
            e.append(items['desc'].encode("utf-8"))
            e.append(items['status'].encode("utf-8"))
            f.append(e)
            out.writerows(f)
            e=[]
            f=[]
    #print(kinds)
     
     
