from textblob import TextBlob
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import re
import string
import seaborn as sns
from langdetect import detect

from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
# Removing RT, Punctuation etc
def remove_rt(x): return re.sub('RT @\w+: ', " ", x)

def rt(x): return re.sub(
  "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x)

data= pd.read_csv("sentAnalysis_zdata.csv")
tweets = data
tweets.drop_duplicates(inplace=True)
# removing the time portion
tweets['created_at'] = tweets.created_at.str.slice(0, 10)


# before removing the non-english tweets
print(tweets.shape)

# removing all the tweets expect the
# non-english tweets
i = 0
print(type(tweets))

print(tweets.text[1])
for index, row in tweets.iterrows():
    tweets.text[index] = str(rt(remove_rt(tweets.text[index]))).lower()
    try:
        if detect(tweets.text[index]) != "en":
            tweets.drop(index)
    except Exception as e:
        # print(e)
        tweets.drop(index)
    # print(i,index)
    # print(tweets.text[index])
    # print()
    i+=1

print("After removing non-english Tweets") 

print(tweets.text)
tweets.to_csv('cleaned_data.csv')


tweets = tweets.text.map(remove_rt).map(rt)
tweets = tweets.str.lower()










