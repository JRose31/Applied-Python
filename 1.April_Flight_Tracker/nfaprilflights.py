import pandas as pd
import csv

df = pd.read_csv('nf20.csv')

msn = df['MSN']
pax = df['PAX']


seen = []
final_pair = {}

#START COUNTER FOR INDEXING
counter = -1

for i in msn:
    counter += 1

    #ADD INSTANCE OF MSN LIST TO SEEN IF IT HASNT BEEN SEEN YET
    if i not in seen:
        seen.append(i)
        final_pair[i] = pax[counter]

    '''IF THAT INSTANCE HAS BEEN SEEN, CHECK IF THE PAX COUNT IS HIGHER
    THAN THE ONE CURRENTLY IN THE DICTIONARY (csv not in date order and
    the trend is for personnel to be added to flights)'''
    elif i in seen:

        '''IF THIS NEW INSTANCE HAS A PAX COUNT HIGHER THAN ONE IN DICTIONARY
        ADD IT AS THE NEW VALUE FOR THAT KEY'''
        if pax[counter] > final_pair.get(i):
            final_pair[i] = pax[counter]

print("Total Flights in April: ", len(final_pair))
print("Total Pax in April: ", sum(final_pair.values()))
