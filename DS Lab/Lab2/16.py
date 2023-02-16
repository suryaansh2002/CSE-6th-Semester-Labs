import pandas as pd

d={
    'Name':['Suryaansh','John Doe'],
    'Age':[20, 30],
    'Qualification':['BTech CSE', 'Nothing']
}

df=pd.DataFrame.from_dict(d)

print(df)

address=['Mumbai', 'Manipal']
df.insert(3,'Address',address)

print(df)
                                                                                                                  