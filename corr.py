import pandas as pd
mapp=pd.read_csv('heatmapp.csv')
df = pd.DataFrame(data=mapp)
print(df['A'].corr(df['B']))