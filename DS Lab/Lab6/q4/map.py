import sys
import pandas as pd
def main(separator='\t'):
# input comes from STDIN (standard input)
    data =  pd.read_excel('/home/200905224/Desktop/ds/Week5/covid_19_data.xlsx',sheet_name='in',engine='openpyxl')
    for age in data['Country/Region']:
            print ('%s%s%d' % (age, separator, 1))

if __name__== "__main__":
    main()