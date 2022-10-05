import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools

# Dataset one -- Country
df_country = pd.DataFrame(
    itertools.islice(
        sntwitter.TwitterSearchScraper(
            '(GMO) since:2022-10-01 near:"Kenya" within:1000km'
        ).get_items(),
        10000,
    )
)[["date", "username", "content"]]

# Dataset one -- Coordinates
loc = "-1.286389, 36.817223, 1000km"
df_coord = pd.DataFrame(
    itertools.islice(
        sntwitter.TwitterSearchScraper(
            '(GMO) since:2022-10-01 geocode:"{}"'.format(loc)
        ).get_items(),
        10000,
    )
)[["date", "username", "content"]]

# Merge the datasets
data = df_coord.merge(df_country, how="inner")

# to save to csv
data.to_csv("gmo_twitter_ke.csv")
