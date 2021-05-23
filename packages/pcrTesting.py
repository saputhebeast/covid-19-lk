import requests
import csv
import pandas as pd
import plotly.express as px

api = "https://www.hpb.health.gov.lk/api/get-current-statistical"
daily_pcr_testing = (requests.get(api).json())['data']['daily_pcr_testing_data']
keys = daily_pcr_testing[0].keys()

with open('./data/dailyPCRTesting.csv', 'w', newline='')  as output_file:
    dataWritter = csv.DictWriter(output_file, keys)
    dataWritter.writeheader()
    dataWritter.writerows(daily_pcr_testing)

def pcrTesting():
    ds = pd.read_csv('./data/dailyPCRTesting.csv')
    ds = ds.sort_values(by=["date"], ascending=True)
    fig = px.line(ds, x = 'date', y = 'count', title='PCR Testing Count')
    fig.show()
