
# import pandas as pd
# df = pd.read_excel('./covid_19_data.xlsx',sheet_name='in',engine='openpyxl')
# for country in df['Country/Region']:
# 	#country = country.strip("(),'")
# 	print('%s\t%d' %(country, 1))


# import pandas as pd
# df = pd.read_excel('./heart_disease_data.xlsx',sheet_name='in',engine='openpyxl')
# for age in df['age']:
# 	#country = country.strip("(),'")
# 	print('%s\t%d' %(age, 1))

# import pandas as pd
# df = pd.read_excel('./German Credit.xlsx',engine='openpyxl')
# for dur in df['DurationOfCreditInMonths']:
# 	#country = country.strip("(),'")
# 	print('%s\t%d' %(dur, 1))
	

import fileinput
for line in fileinput.input():
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, location, item, cost, payment = data
        print ("{0}\t{1}".format(location, cost))