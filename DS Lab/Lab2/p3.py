import pandas as pd 
import numpy as np
df1 =  pd.DataFrame(np.zeros((10, 5)))
df2 = pd.DataFrame(np.zeros((10,3)))
Df_new= pd.concat ((df1, df2), axis=1)
print(Df_new.shape)

A =  pd.DataFrame(np.zeros((10, 5)))
B = pd.DataFrame(np.zeros((15,5)))

D= pd.concat ((A, B), axis=0)
print(D.shape)

data = {'Name':['Kavitha', 'Sudha', 'Raju','Vignesh'],'Age':[28,34,29,42]}
A = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(A.sort_values(by = 'Age'))