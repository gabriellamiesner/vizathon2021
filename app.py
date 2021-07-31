# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['style.css', 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server 
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
data = pd.read_csv('data.csv')
cpi = pd.read_csv('inflation.csv')

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
for i in data['year']: 
    if i not in years:
        years.append(i)
        years_count.append(1)
        num_passed.append(0)
        total_budget.append(0)
        percent_passed.append(0)
        total_income.append(0)
        domestic.append(0)
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

count_domestic = -1
for nine in data['domgross']:
    count_domestic += 1 
    element_domestic = data['year'][count_domestic]
    index_domestic = years.index(element_domestic, 0, len(years))
    domestic[index_domestic] += nine

total_budget.reverse()
num_passed.reverse()
years.reverse()
years_count.reverse()
total_income.reverse()
domestic.reverse()
count_avg_budget = -1
for y in total_budget: 
    count_avg_budget += 1 
    avg_budget.append(y/ years_count[count_avg_budget])

count_avg_domestic = -1
for o in domestic: 
    count_avg_domestic += 1
    avg_domestic.append(o/ years_count[count_avg_domestic])

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

percent_passed = [m / n for m, n in zip(num_passed, years_count)] 
percent_passed = [p * 100 for p in percent_passed]
percent_passed = [int(round(p, 0)) for p in percent_passed]

# 1970 Price x (2011 CPI / 1970 CPI) = 2011 Price
count_avg = -1
cpi_2020 = len(cpi['cpi']) -1 
for dollar in avg_budget:
    count_avg +=1
    dollar = dollar / years_count[count_avg]

count_cpi = -1 
for cost in avg_budget: 
    count_cpi += 1
    t = float(cpi['cpi'][cpi_2020] / cpi['cpi'][count_cpi])
    inflation_avg_budget.append(int(round(cost * t, 0)))

count_cpi_domestic = -1
for u in avg_domestic: 
    count_cpi_domestic +=1 
    i9 = float(cpi['cpi'][cpi_2020] / cpi['cpi'][count_cpi_domestic])
    domestic_inflation.append(int(round(i9*u, 0)))

# print(inflation_avg_budget[0])
# avg_budget = [int(round(dummy, 0)) for dummy in avg_budget]

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

fig = px.line(df, x="Year", y="Percent Passed", title = "Percent of Movies that Passed the Bechdel Test by Year")
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

if __name__ == '__main__':
    app.run_server(debug=True)