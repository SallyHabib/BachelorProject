import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from datetime import datetime

tips=pd.read_csv("user_likes_10216219222701096.csv")

#ax = sns.barplot(x="category", y="name", data=tips).set_title("productivity of the user on facebook through a day"+"("+"Categorized"+")")
plt.figure(figsize=(30,15))
for ax in plt.gcf().axes:
    l = ax.get_xlabel()
    ax.set_xlabel(l, fontsize=5)
ax2 = sns.countplot(x="category", data=tips)
plt.xticks(rotation=90)

plt.show()