import pandas as pd
df = pd.read_excel('/home/200905224/Desktop/ds/Week5/German Credit_for_Week2.xlsx',sheet_name='Sheet1',engine='openpyxl')
for i in range(len(df)):
	print('%s\t%s' %(df['DurationOfCreditInMonths'][i], df['CreditAmount'][i]))