from textblob import TextBlob
import tweepy
import pandas as pd
from keys import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth_handler = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth_handler.set_access_token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)
api = tweepy.API(auth_handler, wait_on_rate_limit=True)

tag_list = ['zelensky', 'Zelenskyy']
columns = ['created_at', 'text', 'location', 'description', 'followers_count', 'friends_count', 'favourites_count', 'utc_offset', 'time_zone', 'verified','statuses_count', 'lang', 'retweet_count']
data = []

no_of_data_points = 10000

for word in tag_list:
    tweet_amount = no_of_data_points//len(tag_list)
    search_term = word
    tweets = tweepy.Cursor(api.search_tweets , q = search_term, lang = 'en').items(tweet_amount)
    for tweet in tweets:
        tweet_text = tweet.text
        # if not tweet.truncated:
        #     tweet_text = tweet.text
        # else:
        #     tweet_text = tweet.extended_tweet['full_text']
        data.append([tweet.created_at, tweet_text,  tweet.user.location, tweet.user.description, tweet.user.followers_count, tweet.user.friends_count, tweet.user.favourites_count, tweet.user.utc_offset, tweet.user.time_zone, tweet.user.verified, tweet.user.statuses_count, tweet.user.lang, tweet.retweet_count])

df_new = pd.DataFrame(data,  columns=columns)
# print(df_new)
df_old = pd.read_csv('sentAnalysis_zdata.csv')
df_old = pd.DataFrame(df_old)
df_old = df_old.drop(['Unnamed: 0'], axis=1)
# print(df_old)

res = pd.concat([df_new, df_old], ignore_index=True)

res.to_csv('sentAnalysis_zdata.csv')
print(res.head(5))
print(res.count()[0])

# filename = 'twitter.txt'
# with open(filename, 'w') as f:
#     for tweet in tweets:
#         f.write(str(tweet))

# dict1 = {}
# with open(filename) as fh:
#     for line in fh:
#         # reads each line and trims of extra the spaces 
#         # and gives only the valid words
#         command, description = line.strip().split(None, 1)
  
#         dict1[command] = description.strip()

# out_file = open("test1.json", "w")
# json.dump(dict1, out_file, indent = 4, sort_keys = False)
# out_file.close()