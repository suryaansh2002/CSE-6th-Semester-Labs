import pandas as pd

df=pd.read_excel('heart_disease_data.xlsx',  engine='openpyxl')

for i in df['age']:
    print(i)
