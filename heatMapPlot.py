import numpy as np; 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
np.random.seed(0)
sns.set()
# uniform_data = np.random.rand(10, 12)
# ax = sns.heatmap(uniform_data)
# flights = sns.load_dataset("flights")
flights=pd.read_csv("heatmapp2.csv")
# flights = flights.pivot("X", "Y")
ax = sns.heatmap(flights)
plt.show()