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



morning=[]
afternoon=[]
night=[]
midnight=[]

with open('user_posts_10214280493341748.csv') as File:     
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


sns.set_style("darkgrid")
bar_plot = sns.barplot(x=["shared","posted","updated","added"],
y=[len(sharedN),len(postedN),len(updatedN),len(addedN)],
                        palette="muted",
                      ).set_title("Night Behavior for the user")
#plt.xticks(rotation=90)
plt.show()


print(len(updatedAft))
print(len(updatedMD))
print(len(sharedAft))
print(len(sharedMD))
print(len(sharedMorning))
print(len(sharedN))
print(len(updatedMorning))
print(len(updatedN))
print(len(postedAft))
print(len(postedMD))
print(len(postedMorning))
print(len(postedN))
print(len(addedAft))
print(len(addedMorning))
print(len(addedMD))
print(len(addedN))




