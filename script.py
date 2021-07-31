import matplotlib
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt 
import dash_core_components as dcc
import dash_html_components as html
# from matplotlib.animation import FuncAnimation 

data = pd.read_csv('data.csv')
cpi = pd.read_csv('inflation.csv')
# twentytwenty = pd.read('2020.csv')

years = []
years_count = []
num_passed = []
avg_budget = []
percent_passed = []
total_budget = []
total_income = []
inflation_avg_budget =[]

for i in data['year']: 
    if i not in years:
        years.append(i)
        years_count.append(1)
        num_passed.append(0)
        total_budget.append(0)
        percent_passed.append(0)
        total_income.append(0)
        avg_budget.append(0)
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

# 1970 Price x (2011 CPI / 1970 CPI) = 2011 Price
count_avg = -1
cpi_2020 = len(cpi['cpi']) -1 
for dollar in total_budget:
    count_avg +=1
    avg_budget[count_avg] = dollar / years_count[count_avg]

count_cpi = -1 
for cost in avg_budget: 
    count_cpi += 1
    t = float(cpi['cpi'][cpi_2020] / cpi['cpi'][count_cpi])
    inflation_avg_budget.append(cost * t)

avg_budget = [int(round(dummy, 0)) for dummy in avg_budget]
inflation_avg_budget = [int(round(dumb, 0)) for dumb in inflation_avg_budget]

