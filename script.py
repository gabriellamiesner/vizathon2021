import pandas as pd
data = pd.read_csv('data.csv')

year = data['year']
title = data['title']
bechdel_test = data['binary']
budget = data['budget']
domestic_gross = data['domgross']
intl_gross = data['intgross']
decade = data['decade_code']

years = []
years_test = []
years_count = []
num_passed = []
total_budget = []
avg_budget =[]
percent_passed = []

for i in data['year']: 

    if i not in years:
        years.append(i)
        years_count.append(1)

    else: 
        index = years.index(i, 0, len(years))
        years_count[index] += 1 

count = -1

# 
for i in data['binary']:
        count += 1
        yearS = data['year'][count]
        if yearS not in years_test:
            years_test.append(yearS)
            if i.__eq__("PASS"): 
                num_passed.append(1)
            else: 
                num_passed.append(0)
        else: 
            index_test = years_test.index(yearS, 0, len(years_test))
            if i.__eq__("PASS"): 
                num_passed[index_test] += 1 



print(num_passed)
