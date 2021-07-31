import pandas as pd
data = pd.read_csv('data.csv')
twentytwenty = pd.read('2020.csv')

years = []
years_count = []
num_passed = []
avg_budget = []
percent_passed = []
total_budget = []
total_income = []

for i in data['year']: 
    if i not in years:
        years.append(i)
        years_count.append(1)
        num_passed.append(0)
        total_budget.append(0)
        percent_passed.append(0)
        total_income.append(0)
    else: 
        index = years.index(i, 0, len(years))
        years_count[index] += 1 

count = -1
for j in data['binary']:
  count += 1
  element = data['year'][count]
  index_binary = years.index(element, 0, len(years))
  if j.__eq__("PASS"): 
        num_passed[index_binary] += 1

count_budget = -1
for k in data['budget']:
  count_budget += 1
  element_budget = data['year'][count_budget]
  index_budget = years.index(element_budget, 0, len(years))
  total_budget[index_budget] += k

# count_income = -1
# for q in data['totalgross']:
#   count_income += 1
#   element_income = data['year'][count_income]
#   index_income = years.index(element_income, 0, len(years))
#   q = ast.literal_eval(q)
#   total_income[index_income] += q

total_budget.reverse()
num_passed.reverse()
years.reverse()
years_count.reverse()
total_income.reverse()

percent_passed = [m / n for m, n in zip(num_passed, years_count)] 
percent_passed = [p * 100 for p in percent_passed]
percent_passed = [int(round(p, 0)) for p in percent_passed]


print(num_passed)
print(years_count)
print(percent_passed)
print(total_income)
