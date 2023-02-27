import pandas as pd
import numpy as np
s=pd.Series([3,9,-2,10,5])

print(s.sum(),s.min(),s.max())

data = [['Dinesh',10],['Nithya',12],['Raji',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

data = {'Name':['Kavitha', 'Sudha', 'Raju','Vignesh'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

df1=pd.DataFrame({'A':pd.Timestamp('20130102'),'B':np.array([3]*4,dtype='int32'),
'C':pd.Categorical(['Male','Female','Male','Female'])})
print(df1, df1.shape, df1.dtypes, df1.describe())
print(df1.head())
print(df1.tail())
print(df.index, df.columns)
print(df.T)
