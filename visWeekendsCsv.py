import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from datetime import datetime

postsWeekendShared=[]
postsWeekendPosted=[]
postsWeekendUpdated=[]
postsWeekendAdded=[]

postsWorkdaysShared=[]
postsWorkdaysPosted=[]
postsWorkdaysUpdated=[]
postsWorkdaysAdded=[]


with open('user_posts_10156305351259583.csv') as File:     
    tfidfReader = csv.reader(File)     
    for row in tfidfReader:
        datetime_object = datetime.strptime(row[3][:-4],"%Y-%m-%dT%H:%M:%S+")
        month=datetime_object.month
        year=datetime_object.year
        day=datetime_object.day
        hour=datetime_object.hour
        zozo=datetime(year, month, day)
        if(zozo.weekday()==4 or zozo.weekday()==5):
            if(row[4]=="posted"):
                postsWeekendPosted.append(1)
            elif(row[4]=="shared"):
                postsWeekendShared.append(1)
            elif(row[4]=="updated"):
                postsWeekendUpdated.append(1)
            elif(row[4]=="added"):
                postsWeekendAdded.append(1)
        else:
            if(row[4]=="posted"):
                postsWorkdaysPosted.append(1)
            elif(row[4]=="shared"):
                postsWorkdaysShared.append(1)
            elif(row[4]=="updated"):
                postsWorkdaysUpdated.append(1)
            elif(row[4]=="added"):
                postsWorkdaysAdded.append(1)


out= csv.writer(open('weekend.csv', 'wb'),delimiter=(','))
b=[]
a=[]
a.append("value")
a.append("daysType")
a.append("type")
out.writerow(a)
a=[]
a.append(len(postsWeekendShared))
a.append("weekends")
a.append("shared")
out.writerow(a)
a=[]
a.append(len(postsWeekendUpdated))
a.append("weekends")
a.append("updated")
out.writerow(a)
a=[]
a.append(len(postsWeekendPosted))
a.append("weekends")
a.append("posted")
out.writerow(a)
a=[]
a.append(len(postsWeekendAdded))
a.append("weekends")
a.append("added")
out.writerow(a)

a=[]
a.append(len(postsWorkdaysShared))
a.append("workDays")
a.append("shared")
out.writerow(a)
a=[]
a.append(len(postsWorkdaysUpdated))
a.append("workDays")
a.append("updated")
out.writerow(a)
a=[]
a.append(len(postsWorkdaysPosted))
a.append("workDays")
a.append("posted")
out.writerow(a)
a=[]
a.append(len(postsWorkdaysAdded))
a.append("workDays")
a.append("added")
out.writerow(a)











