import pandas as pd
import requests #Pushshift accesses Reddit via an url so this is needed
import json #JSON manipulation
import csv #To Convert final table into a csv file to save to your machine
import time
import datetime

tickers = ["GME", "SPY", "AMC", "BB", "TSLA", "PLNTR", "CRSR", "NOK", "AAPL", "SNAP"]
# tickers = ["GME"]

mapOfDates = {}

for ticker in tickers:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&apikey=GKZ3KECUBD35TO97'
    print(url)
    r = requests.get(url)
    #Load JSON data from webpage into data variable
    data = json.loads(r.text)

    if not data.get('Time Series (Daily)'):
        continue

    daily = data['Time Series (Daily)']
    keys = list(daily.keys())

    keys.sort()

    mapOfDates[ticker] = {}

    for i in range(0, len(keys)):
        next_day = i + 3 if (i + 3) < len(keys) else (i + 1)

        if i + 1 >= len(keys):
            break

        today_price = float(daily[keys[i]]['1. open'])
        tomorrow_price = float(daily[keys[next_day]]['4. close'])

        percentChange = (tomorrow_price - today_price) / today_price

        mapOfDates[ticker][keys[i]] = percentChange

with open('stockIncreasesByDate.json', 'w') as fp:
    json.dump(mapOfDates, fp)



