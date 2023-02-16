import pandas as pd

d={
    'Name':['Suryaansh','John Doe'],
    'Age':[20, 30],
    'Qualification':['BTech CSE', 'Nothing']
}

df=pd.DataFrame.from_dict(d)

print(df)

l=['Mumbai', 'Manipal']
df['Address']=l

print(df)
