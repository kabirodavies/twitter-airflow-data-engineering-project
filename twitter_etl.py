import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import snscrape.modules.twitter as sntwitter

# Coordinates
loc = "-1.286389, 36.817223, 1000km"

# Query by Country
query_country = '(GMO) since:2022-10-01 near:"Kenya" within:1000km'

# Query by Country -- Coordinates
query_coordinates = '(GMO) since:2022-10-01 geocode:"{}"'.format(loc)

tweets = []
limit = 100000

for tweet in sntwitter.TwitterSearchScraper(
    query_country, query_coordinates
).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])

df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])

# drop_duplicates
data = df.drop_duplicates()

# to save to csv
df.to_csv("data/kenya_gmo_tweets.csv")
