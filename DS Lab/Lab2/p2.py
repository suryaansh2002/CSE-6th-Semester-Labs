import pandas as pd 
import numpy as np

dates=pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100,4), index=dates, columns=list('ABCD'))

print(df.head())
print(df.tail())
print(df.index, df.columns)
print(df.T)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by='B'))
print(df[0:3])


print(df['20130105':'20130110'])
print(df.iloc[0])
print(df.iloc[0,:2])
print(df.iloc[0,0])
print(df['A'])
print(df[['A','B']])
print(df[['A','B']][:5])
print(df.loc['20130101':'20130105',['A','B']][:5])


print(df[df.A>0])
df['F']=['Male','Female','Female','Male','Female']*20
df.loc[:,'D']=np.array([5]*len(df))
print(df)
df.drop ('D', axis =1, inplace=True)
print(df)