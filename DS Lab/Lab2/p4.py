import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv('prima_indians_diabetes_for_Week2.csv',header=None)
df.columns=['preg','glu','bp','sft','ins','bmi','dpf','age','class']
print(df.head())
plt.scatter(df['bmi'],df['glu'])
plt.xlabel('bmi')
plt.ylabel('Glucose')
plt.show()
df['age'].hist()
plt.show()


W = pd.read_csv('wine_for_Week2.xls',header=None)
print(W.head())

G=pd.read_excel('German Credit_for_Week2.xlsx',sheet_name='Sheet1', engine='openpyxl')
G.head()

H = pd.read_table('HR_for_Week2.txt')
H.head()
f=H['Department'].value_counts()
f.plot(kind='bar')
fa=pd.crosstab(H['Gender'],H['Attrition'])
fa.plot(kind='bar')
