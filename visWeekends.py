import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from datetime import datetime

postsWeekend=[]
postsWorkdays=[]


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
            postsWeekend.append(1)
        else:
            postsWorkdays.append(1)


sns.set_style("darkgrid")
bar_plot = sns.barplot(x=["weekendPosts","workdaysPosts"],
y=[len(postsWeekend),len(postsWorkdays)],
                        palette="muted",
                      ).set_title("productivity of the user on facebook through weekends VS through Workdays")
#plt.xticks(rotation=90)
plt.show()






