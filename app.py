# -*- coding: utf-8 -*-
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = pd.read_csv('data.csv')
cpi = pd.read_csv('inflation.csv')
twenty = pd.read_csv('2020.csv')

years = []
years_count = []
num_passed = []
avg_budget = []
percent_passed = []
total_budget = []
total_income = []
domestic = []
colors = []
avg_domestic = []
domestic_inflation = []
inflation_avg_budget =[]

# loops thru year column in csv, appends all unique years to years list 
# sets up years_count list, by adding 1 for every year 
# sets up other lists, by appending a 0, so they are the same length as the years list 
for year in data['year']: 
    if year not in years:
        years.append(year)
        years_count.append(1)
        num_passed.append(0)
        total_budget.append(0)
        percent_passed.append(0)
        total_income.append(0)
        domestic.append(0)
        # finds the index of the current values year, so it can do this: 
        # if year is already in the years list, it adds 1 to the count for that year to the years_count list 
    else: 
        index_year = years.index(year, 0, len(years))
        years_count[index_year] += 1 

# loops thru binary column in csv 
# count_binary is used to keep track of index number
# element_binary keeps track of the year that the current value was released in 
# index_binary keeps track of the index of the year the movie was released in, so that: 
# if the grade == "PASS", 1 is added to the num_passed for that particular year
count_binary = -1
for grade in data['binary']:
  count_binary += 1
  element_binary = data['year'][count_binary]
  index_binary = years.index(element_binary, 0, len(years))
  if grade.__eq__("PASS"): 
        num_passed[index_binary] += 1

# loops thru budget column in csv 
# count_budget is used to keep track of index number
# element_budget keeps track of the year that the current value was released in 
# index_budget keeps track of the index of the year the movie was released in, so that: 
# the amount the budget is added to the total_budget of all movies released that year 
count_budget = -1
for budget in data['budget']:
  count_budget += 1
  element_budget = data['year'][count_budget]
  index_budget = years.index(element_budget, 0, len(years))
  total_budget[index_budget] += budget

# loops thru domestic gross column in csv
# count_domestic is used to keep track of index number
# element_domestic keeps track of the year that the current value was released in 
# index_domestic keeps track of the index of the year the movie was released in, so that: 
# revenue for that particular film can be added to the total revenue for the whole year  
count_domestic = -1
for revenue in data['domgross']:
    count_domestic += 1 
    element_domestic = data['year'][count_domestic]
    index_domestic = years.index(element_domestic, 0, len(years))
    domestic[index_domestic] += revenue

# reverses the values of all the lists so that they are in chronilogical order 
total_budget.reverse()
num_passed.reverse()
years.reverse()
years_count.reverse()
total_income.reverse()
domestic.reverse()

# loops thru percent passed 3 times and 
    # zips the num_passed and years_count together into a tuple, then divides num_passed by years_count to find a percent_passed per year 
    # multiplies by 100 to get a whole number for the percent_passed
    # rounds the value to remove any remaining decimals and then converts it into an int data type
percent_passed = [m / n for m, n in zip(num_passed, years_count)] 
percent_passed = [p * 100 for p in percent_passed]
percent_passed = [int(round(p, 0)) for p in percent_passed]

# loops thru each year's total budget 
# count_avg_budget keeps track of index number
# total_budget is divided by total number of films at the count_avg_budget index and then appended to the avg_budget list
count_avg_budget = -1
for money in total_budget: 
    count_avg_budget += 1 
    avg_budget.append(money/ years_count[count_avg_budget])

# loops thru each year's total revenue 
# count_avg_domestic keeps track of index number
# domestic is divided by total number of films at the count_avg_domestic index and then appended to the avg_domestic list
count_avg_domestic = -1
for money_made in domestic: 
    count_avg_domestic += 1
    avg_domestic.append(money_made/ years_count[count_avg_domestic])

# assigns decade label to each movie, to make classification on charts easier 
for color in years:
    if color > 1969 and color < 1980: 
        colors.append('1970s')
    elif color > 1979 and color < 1990: 
        colors.append('1980s')
    elif color > 1989 and color < 2000: 
        colors.append('1990s')
    elif color > 1999 and color < 2010: 
        colors.append('2000s')
    else: 
        colors.append('2010s')


# loops through avg_budget 
# count_avg holds the index number during loop 
# divides avg_budget by years_count to find the average budget for each year 
count_avg = -1
for dollar in avg_budget:
    count_avg +=1
    dollar = dollar / years_count[count_avg]

# inflation formula: 1970 Price x (2011 CPI / 1970 CPI) = 2011 Price
# loops thru avg_budget 
# cpi_2020 is equal to the index where the 2020 CPI is 
# count_cpi holds index number during loop 
# assigns t to the 2020 cpi divided by the cpi of the year's avg budget
# multiplies t by the year's average budget, rounds it to a whole number, and then appends it to the inflation_avg_budget list 
cpi_2020 = len(cpi['cpi']) -1 
count_cpi = -1 
for cost in avg_budget: 
    count_cpi += 1
    t = float(cpi['cpi'][cpi_2020] / cpi['cpi'][count_cpi])
    inflation_avg_budget.append(int(round(cost * t, 0)))

# loops thru avg_domestic 
# count_cpi_domestic holds index number during loop 
# i9 is set equal to the cpi divided by the cpi of the year's avg budget
# multiplies i9 by the year's average budget, rounds it to a whole number, and then appends it to the domestic_inflation list 
count_cpi_domestic = -1
for u in avg_domestic: 
    count_cpi_domestic +=1 
    i9 = float(cpi['cpi'][cpi_2020] / cpi['cpi'][count_cpi_domestic])
    domestic_inflation.append(int(round(i9*u, 0)))

#loops thru 2020 binary column 
# count_2020 holds index value during loop 
# if the binary value passes bechdel test, it adds one to 2020's count 
count_2020 = 0
for eight in twenty['binary']:
    if eight == "PASS":
        count_2020 +=1
        
percent_passed_2020 = count_2020/len(twenty['binary'])


# vizzes
df = pd.DataFrame({
    "Year": years,
    "Percent Passed": percent_passed, 
})

df2 = pd.DataFrame({
    "Percent Passed": percent_passed, 
    "Average Budget (in USD), adjusted for inflation": inflation_avg_budget,
    "Year": years,
    " ": colors
})

df3 = pd.DataFrame({
    "Average Domestic Grossing (in USD), adjusted for inflation": domestic_inflation, 
    "Percent Passed": percent_passed,
    " ": colors
})

# web app flask stuff 
fig = px.line(df, x="Year", y="Percent Passed", title = "One Step Forward, Two Steps Back")
fig.update_traces(line_color='pink', hovertemplate = '<b>%{x}</b> <br> Percent Passed: %{y}%')

fig2 = px.scatter(df2, x = "Average Budget (in USD), adjusted for inflation", y = "Percent Passed", title = "How Much Hollywood Values Women", color = " ")
fig2.update_traces(hovertemplate = 'Percent Passed: %{y}% <br> Average Budget: $%{x}')

fig3 = px.scatter(df3, x = "Average Domestic Grossing (in USD), adjusted for inflation", y = "Percent Passed", title = "How Much Society Values Women", color = " ")
fig3.update_traces(hovertemplate = 'Percent Passed: %{y}% <br> Average Grossing: $%{x}')

app.layout = html.Div(children=[
    html.H1(children='Bechdel Test', id = "title", style = {'fontStyle': 'italic', 'fontWeight':'800'}),

    html.Div(children='''
        1) two named women
    '''),
        html.Div(children='''
        2) who talk to each other 
    '''),
        html.Div(children='''
        3) about something besides a man
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.Div(children = '''
    ** There is a clear outlier in 1970 because there was only one movie in the dataset from that year. **
    '''),

    dcc.Graph(
        id = 'example-graph2', 
        figure = fig2, 
    ), 

    dcc.Graph(
        id = 'example-graph3', 
        figure = fig3
    ), 
    html.Div(children = '''
        ** The data is not completely accurate, as the data set we used was missing the domestic grossing for 57 films, which lowered the average. **     ''')
], style = {'color':'black', 'textAlign':'center'})

# run server
if __name__ == '__main__':
    app.run_server(debug=True)