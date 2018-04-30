import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from datetime import datetime

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


with open('user_posts_10156140722734774.csv') as File:     
    tfidfReader = csv.reader(File)     
    for row in tfidfReader:
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


out= csv.writer(open('good.csv', 'wb'),delimiter=(','))
b=[]
a=[]
a.append("value")
a.append("timing")
a.append("type")
out.writerow(a)
a=[]
a.append(len(sharedMorning))
a.append("morning")
a.append("shared")
out.writerow(a)
a=[]
a.append(len(updatedMorning))
a.append("morning")
a.append("updated")
out.writerow(a)
a=[]
a.append(len(postedMorning))
a.append("morning")
a.append("posted")
out.writerow(a)
a=[]
a.append(len(addedMorning))
a.append("morning")
a.append("added")
out.writerow(a)

a=[]
a.append(len(sharedAft))
a.append("afternoon")
a.append("shared")
out.writerow(a)
a=[]
a.append(len(updatedAft))
a.append("afternoon")
a.append("updated")
out.writerow(a)
a=[]
a.append(len(postedAft))
a.append("afternoon")
a.append("posted")
out.writerow(a)
a=[]
a.append(len(addedAft))
a.append("afternoon")
a.append("added")
out.writerow(a)

a=[]
a.append(len(sharedN))
a.append("night")
a.append("shared")
out.writerow(a)
a=[]
a.append(len(updatedN))
a.append("night")
a.append("updated")
out.writerow(a)
a=[]
a.append(len(postedN))
a.append("night")
a.append("posted")
out.writerow(a)
a=[]
a.append(len(addedN))
a.append("night")
a.append("added")
out.writerow(a)

a=[]
a.append(len(sharedMD))
a.append("midnight")
a.append("shared")
out.writerow(a)
a=[]
a.append(len(updatedMD))
a.append("midnight")
a.append("updated")
out.writerow(a)
a=[]
a.append(len(postedMD))
a.append("midnight")
a.append("posted")
out.writerow(a)
a=[]
a.append(len(addedMD))
a.append("midnight")
a.append("added")
out.writerow(a)