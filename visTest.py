import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from datetime import datetime

tips=pd.read_csv("test.csv")

ax = sns.barplot(x="timing", y="value", hue="type", data=tips)

plt.show()