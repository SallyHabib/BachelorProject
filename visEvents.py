import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from datetime import datetime

attended=[]
unsure=[]


with open('user_events_10216064001413978.csv') as File:     
    tfidfReader = csv.reader(File)     
    for row in tfidfReader:
        if(row[2]=="attending"):
            attended.append(1)
        else:
            unsure.append(1)
        
sns.set_style("darkgrid")
bar_plot = sns.barplot(x=["attended","unsure"],
y=[len(attended),len(unsure)],
                        palette="muted",
                      ).set_title("number of events the user attended compared to unattended")
#plt.xticks(rotation=90)
plt.show()






