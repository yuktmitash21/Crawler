import json

with open('wallstreetbets_submission.json') as f:
  data = json.load(f)

for d in data:
    if 'aapl' in data.selftext.i or 'aapl' in data.title:
        print(data.selftext, data.title)