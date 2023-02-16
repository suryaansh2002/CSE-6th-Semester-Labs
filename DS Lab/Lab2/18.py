import pandas as pd
import numpy as np
df1=pd.DataFrame({
    'Name':['Ram','Diya', 'Chandan','James','Alice']
}, index=range(1,6))

df2=pd.DataFrame({
    'Q1 /10':[8.0,9.0,7.5,8.5,6.5],
    'Insem1/15':[11.0,14.0,14.5,13.0,12.5],
    'Q2 /10':[9.5,6.5,8.5, 9.0,9.0],
    'Insem2/15':[12.5,13.5,14.4,15.0 ,13.0]
}, index=range(1,6))

print(df1)
print(df2)


df2['Total']=0
for i in range(len(df2)):
    df2['Total'][i+1]=float(sum(df2.iloc[i]))
df3=df1.join(df2)
df3.loc['Mean']=0
df3['Name']['Mean']=np.nan
for col in list(df2.columns):
    df3[col]['Mean']=np.mean(list(df3[col])[:-1])
print(list(df2.columns))
print(df3)