import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime

total_posts=0.0
total_posts_per_year=0
weekActivity=0
months=[0]*12
daysX_monthsY=np.zeros([12,31])
average_nbr_posts_month=0

sharedRatio=0.0
updateRatio=0.0
addRatio=0.0
postRatio=0.0

sharedMorning=[] 
updatedMorning=[] 
postedMorning=[] 
addedMorning=[]

sharedAft=[] 
updatedAft=[] 
postedAft=[] 
addedAft=[]

sharedN=[] 
updatedN=[] 
postedN=[] 
addedN=[]

sharedMD=[] 
updatedMD=[] 
postedMD=[] 
addedMD=[]

postsWeekendShared=[]
postsWeekendPosted=[]
postsWeekendUpdated=[]
postsWeekendAdded=[]

postsWorkdaysShared=[]
postsWorkdaysPosted=[]
postsWorkdaysUpdated=[]
postsWorkdaysAdded=[]

user_id=[]
with open('users.csv', 'rb') as zozoFile:
    user = csv.reader(zozoFile)
    for row in user:
        user_id.append(row[2]) 

#path='user_posts_'+user_id[0]+'.csv'
i=0
while i < len(user_id):
    path='user_posts_'+user_id[i]+'.csv'
    print(path)
    with open(path) as File:     
        tfidfReader = csv.reader(File)     
        for row in tfidfReader:
            total_posts+=1
            datetime_object = datetime.strptime(row[3][:-4],"%Y-%m-%dT%H:%M:%S+")
            hour = datetime_object.hour
            #print(hour)
            if(hour>=6 and hour <12):     
                #print("gh M")        
                if(row[4]=='posted'):
                    postedMorning.append(1)                
                elif(row[4]=='added'):        
                    addedMorning.append(1)                 
                elif(row[4]=='shared'):        
                    sharedMorning.append(1)         
                elif(row[4]=='updated'):
                    updatedMorning.append(1)    
            elif(hour>=12 and hour <18):
                #print("gh Aft")  
                if(row[4]=='posted'):
                    postedAft.append(1)                
                elif(row[4]=='added'):        
                    addedAft.append(1)                 
                elif(row[4]=='shared'):        
                    sharedAft.append(1)         
                elif(row[4]=='updated'):
                    updatedAft.append(1)  
            elif(hour>=18 and hour <24):
                #print("gh N")
                if(row[4]=='posted'):
                    postedN.append(1)                
                elif(row[4]=='added'):        
                    addedN.append(1)                 
                elif(row[4]=='shared'):        
                    sharedN.append(1)         
                elif(row[4]=='updated'):
                    updatedN.append(1)
            elif(hour>=0 and hour <6):
                #print("gh Md")
                if(row[4]=='posted'):
                    postedMD.append(1)                
                elif(row[4]=='added'):        
                    addedMD.append(1)                 
                elif(row[4]=='shared'):        
                    sharedMD.append(1)         
                elif(row[4]=='updated'):
                    updatedMD.append(1) 

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
            if(year==2017):
                total_posts_per_year+=1
                months[month-1]+=1
                daysX_monthsY[month-1][day-1]+=1
            if(year==2017 and month == 7 and day>=1 and day<8):
                weekActivity+=1
                #print(weekActivity)

    morning=len(sharedMorning)+len(postedMorning)+len(updatedMorning)+len(addedMorning)
    aft=len(sharedAft)+len(postedAft)+len(updatedAft)+len(addedAft)
    night=len(sharedN)+len(postedN)+len(updatedN)+len(addedN)
    md=len(sharedMD)+len(postedMD)+len(updatedMD)+len(addedMD)
    posted=len(postedAft)+len(postedMD)+len(postedMorning)+len(postedN)
    shared=len(sharedAft)+len(sharedMD)+len(sharedMorning)+len(sharedN)
    # print(shared)
    # print(total_posts)
    updated=len(updatedAft)+len(updatedMorning)+len(updatedN)+len(updatedMD)
    added=len(addedAft)+len(addedMD)+len(addedMorning)+len(addedN)
    difference=morning-md
    totalWorks=len(postsWorkdaysAdded)+len(postsWorkdaysShared)+len(postsWorkdaysUpdated)+len(postsWorkdaysPosted)
    totalWeekends=len(postsWeekendAdded)+len(postsWeekendPosted)+len(postsWeekendShared)+len(postsWeekendUpdated)
    average_nbr_posts_month=sum(months)/12.0
    average_nbr_posts_week=max(months)/4.0
    sharedRatio=(shared/total_posts)*100
    updateRatio=(updated/total_posts)*100
    addRatio=(added/total_posts)*100
    postRatio=(posted/total_posts)*100


    out= csv.writer(open('user.csv', 'ab'),delimiter=(','))

    a=[]
    if(i==0):
        a.append("value")
        a.append("timing")
        a.append("type")
        out.writerow(a)
        a=[]
    else:
        a.append(len(sharedMorning))
        # a.append("morning")
        # a.append("shared")
        # out.writerow(a)
        # a=[]
        a.append(len(updatedMorning))
        # a.append("morning")
        # a.append("updated")
        # out.writerow(a)
        # a=[]
        a.append(len(postedMorning))
        # a.append("morning")
        # a.append("posted")
        # out.writerow(a)
        # a=[]
        a.append(len(addedMorning))
        # a.append("morning")
        # a.append("added")
        # out.writerow(a)
        # a=[]
        a.append(len(sharedAft))
        # a.append("afternoon")
        # a.append("shared")
        # out.writerow(a)
        # a=[]
        a.append(len(updatedAft))
        # a.append("afternoon")
        # a.append("updated")
        # out.writerow(a)
        # a=[]
        a.append(len(postedAft))
        # a.append("afternoon")
        # a.append("posted")
        # out.writerow(a)
        # a=[]
        a.append(len(addedAft))
        # a.append("afternoon")
        # a.append("added")
        # out.writerow(a)
        # a=[]
        a.append(len(sharedN))
        # a.append("night")
        # a.append("shared")
        # out.writerow(a)
        # a=[]
        a.append(len(updatedN))
        # a.append("night")
        # a.append("updated")
        # out.writerow(a)
        # a=[]
        a.append(len(postedN))
        # a.append("night")
        # a.append("posted")
        # out.writerow(a)
        # a=[]
        a.append(len(addedN))
        # a.append("night")
        # a.append("added")
        # out.writerow(a)
        # a=[]
        a.append(len(sharedMD))
        # a.append("midnight")
        # a.append("shared")
        # out.writerow(a)
        # a=[]
        a.append(len(updatedMD))
        # a.append("midnight")
        # a.append("updated")
        # out.writerow(a)
        # a=[]
        a.append(len(postedMD))
        # a.append("midnight")
        # a.append("posted")
        # out.writerow(a)
        # a=[]
        a.append(len(addedMD))
        a.append(morning)
        a.append(aft)
        a.append(night)
        a.append(md)
        a.append(difference)
        a.append(len(postsWeekendAdded))
        a.append(len(postsWeekendPosted))
        a.append(len(postsWeekendShared))
        a.append(len(postsWeekendUpdated))
        a.append(len(postsWorkdaysAdded))
        a.append(len(postsWorkdaysPosted))
        a.append(len(postsWorkdaysShared))
        a.append(len(postsWorkdaysUpdated))
        a.append(totalWeekends)
        a.append(totalWorks)
        if(totalWeekends>totalWorks):
            a.append(totalWeekends-totalWorks)
        else:
            a.append(totalWorks-totalWeekends)
        # a.append(months[0])
        # a.append(months[1])
        # a.append(months[2])
        # # a.append(months[3])
        # # a.append(months[4])
        # a.append(months[5])
        # a.append(months[6])
        # # a.append(months[7])
        # a.append(months[8])
        # a.append(months[9])
        # a.append(months[10])
        # a.append(months[11])
        a.append(average_nbr_posts_month)
        a.append(average_nbr_posts_week)
        a.append(sharedRatio)
        a.append(updateRatio)
        a.append(postRatio)
        a.append(addRatio)
        #print(len(postsWeekendShared))
        # a.append("midnight")
        # a.append("added")
        out.writerow(a)
    i+=1


