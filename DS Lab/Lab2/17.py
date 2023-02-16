import pandas as pd

df1=pd.DataFrame({
    'Name':['Ram','Diya', 'Chandan','James','Alice']
}, index=range(1,6))

df2=pd.DataFrame({
    'Maths':[80,90,77,87,86],
    'Physics':[81,94,77,83,82],
    'Chemistry':[91,86,85,90,91],
    'Biology':[82,83,84,85,93]
}, index=range(1,6))

print(df1)
print(df2)

df3=df1.join(df2)
df3['total']=0
for i in range(len(df3)):
    df3['total'][i+1]=sum(df3.iloc[i][1:])
print(df3)