import praw
import pandas as pd
import json

tickers = ["GME", "SPY", "AMC", "BB", "TSLA", "PLNTR", "CRSR", "NOK", "AAPL", "SNAP"]

with open('credentials.json') as f:
  data = json.load(f)

reddit = praw.Reddit(client_id=data['client_id'],#my client id
                     client_secret=data['client_secret'],  #your client secret
                     user_agent=data['user_agent'], #user agent name
                     username =data['username'],     # your reddit username
                     password = data['password'])     # your reddit password

subreddit = reddit.subreddit('wallstreetbets')

new = subreddit.search("GME", limit=1000, sort = "hot")
objects = []


for i in new:
    # print(i.selftext)
    # print (dir(i))
    objects.append({'views': i.view_count, 'score': i.score, 'num_comments': i.num_comments, 'created': i.created_utc, 'title': i.title, 'body': i.selftext})

json_string = json.dumps(objects)

with open('data-gme.json', 'w') as f:
    json.dump(json_string, f)

