import pandas as pd
import plotly.express as px
import csv
import requests

api = "https://pomber.github.io/covid19/timeseries.json"
srilanka = (requests.get(api).json())['Sri Lanka']
keys = srilanka[0].keys()

with open('./data/covidSriLanka.csv', 'w', newline='')  as output_file:
    dataWritter = csv.DictWriter(output_file, keys)
    dataWritter.writeheader()
    dataWritter.writerows(srilanka)

df = pd.read_csv('./data/covidSriLanka.csv')

def confirmedCases():
    fig = px.line(df, x = 'date', y = 'confirmed', title='Confirmed Cases')
    fig.show()

def recovered():
    fig = px.line(df, x = 'date', y = 'recovered', title='Recovered')
    fig.show()