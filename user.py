import csv
from datetime import datetime
import json
import numpy as np
import nltk
from nltk.corpus import stopwords


user_id=[]
with open('users.csv', 'rb') as file:
    user = csv.reader(file)
    for row in user:
        user_id.append(row[2]) 

#intilization
total_posts=0.0
total_posts_per_year=0
shared=0
added=0
posted=0
updated=0 
activityM=0    
activityA=0
activityN=0
activityMN=0 
lang=[]
months=[0]*12
days=[0]*31
daysX_monthsY=np.zeros([12,31])
average_nbr_posts_month=0
sharedRatio=0
updateRatio=0
addRatio=0
postRatio=0
path='user_posts_'+user_id[0]+'.csv'
#print(path)
with open(path, 'rb') as f:
    posts = csv.reader(f)
    for items in posts:
        #print(path)
        # total number of posts
        total_posts+=1

        # which type they use most shre/add/update/post
        if(items[4]=='added'):
            added+=1
        elif(items[4]=='updated'):
            updated+=1
        elif(items[4]=='posted'):
            posted+=1
        else:
            shared+=1

        # check activity time
        datetime_object = datetime.strptime(items[3][:-4],"%Y-%m-%dT%H:%M:%S+")    
        hour=datetime_object.hour
        month=datetime_object.month
        year=datetime_object.year
        day=datetime_object.day
        if(hour>=6 and hour<12):
            activityM+=1
        elif(hour>=12 and hour <18):
            activityA+=1
        elif(hour>=18 and hour <24):
            activityN+=1
        elif(hour >=0 and hour <6):
            activityMN+=1
        
        # nbr of posts/month posts/day
        
        if(year==2017):
            total_posts_per_year+=1
            months[month-1]+=1
            daysX_monthsY[month-1][day-1]+=1
        
print(activityA)
print(activityM)
print(activityMN)
print(activityN)
print(float(activityA/365.0))
average_nbr_posts_month=sum(months)/12.0
average_nbr_posts_week=max(months)/4.0
print(average_nbr_posts_week)
print(average_nbr_posts_month)
print(months)
print(months[4])

sharedRatio=shared/total_posts
updateRatio=updated/total_posts
addRatio=added/total_posts
postRatio=posted/total_posts

