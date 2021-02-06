import pandas as pd
import requests #Pushshift accesses Reddit via an url so this is needed
import json #JSON manipulation
import csv #To Convert final table into a csv file to save to your machine
import time
import datetime

def getPushshiftData(query, after, before, limit):
    url = 'https://api.pushshift.io/reddit/search/submission/?&before=' + before + '&after=' + after + '&q=' + query + '&sort_type=score&sort=desc&subreddit=wallstreetbets&size=' + limit

    #Print URL to show user
    print(url)
    #Request URL
    r = requests.get(url)
    #Load JSON data from webpage into data variable
    data = json.loads(r.text)
    #return the data element which contains all the submissions data
    return data['data']

tickers = ["GME", "SPY", "AMC", "BB", "TSLA", "PLNTR", "CRSR", "NOK", "AAPL", "SNAP"]

before = datetime.datetime(2021, 1, 5)
later = before + datetime.timedelta(days=1)
map = {}
allData = []

for ticker in tickers:
    for i in range(0, 30):
        data = getPushshiftData(ticker, str(int(before.timestamp())), str(int(later.timestamp())), str(1000))
        print (len(data), ticker)
        for dat in data:
            allData.append({ 'score': dat.get('score') or 0, 'num_comments': dat.get('num_comments') or 0, 'created': dat.get('created_utc') or 0, 'title': dat.get('title') or '', 'body': dat.get('selftext') or '', 'upvote_ratio': dat.get('upvote_ratio') or ''})
        before = later
        later += datetime.timedelta(days=1)
        time.sleep(2)
    map[ticker] = allData
    allData = []
    before = datetime.datetime(2021, 1, 5)
    later = before + datetime.timedelta(days=1)

json_string = json.dumps(map)
with open('data-gme.json', 'w') as f:
    json.dump(json_string, f)





