import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from datetime import datetime

tips=pd.read_csv("weekend.csv")
tips = tips.sort_values('value',ascending=False)

ax = sns.barplot(x="daysType", y="value", hue="type", data=tips).set_title("productivity of the user on facebook through a day"+"("+"Categorized"+")")

plt.show()