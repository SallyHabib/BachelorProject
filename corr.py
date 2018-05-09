import pandas as pd
mapp=pd.read_csv('plot.csv')
df = pd.DataFrame(data=mapp)
print(df['A'].corr(df['B']))