import pandas as pd
df = pd.read_excel('/home/200905224/Desktop/ds/Week5/covid_19_data.xlsx',sheet_name='in',engine='openpyxl')
for i in range(len(df)):
	print('%s\t%s' %(df['Country/Region'][i], df['Confirmed'][i]))