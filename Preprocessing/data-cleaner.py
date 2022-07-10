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

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

### for stemming
stemmer = nltk.stem.SnowballStemmer('english')

### for lemmatizing
lemma = nltk.wordnet.WordNetLemmatizer()

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

# Stop Words
stop_Words = ['he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they',
'them', 'their', 'theirs', 'only', 'other', 'some', 'such', 'no', 'nor', 'not', 'own', 'same', 'so',
'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd',
'll', 'm', 'o', 're', 've', 'y', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why',
'how', 'all', 'any', 'both', 'each', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',
"that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'hadn', "hadn't", 'hasn', "hasn't", 'be',
'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'from', 'up', 'down', 'in',
'out', 'on', 'off', 'over', 'under', 'few', 'more', 'most' , 'with', 'about', 'against', 'between',
'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'ain', 'aren', "aren't",
'couldn', "couldn't", 'didn', "didn't",'doesn', "doesn't", 'haven', "haven't", 'isn', "isn't",
'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't",
'shouldn', "shouldn't",'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn',
"wouldn't", 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",
"you'll", "you'd", 'your', 'yours', 'yours elf', 'yourselves']

print(tweets.text[1])


for index, row in tweets.iterrows():
    tweets.text[index] = str(rt(remove_rt(tweets.text[index]))).lower()
    try:
        if detect(tweets.text[index]) != "en":
            tweets.drop(index)
    except Exception as e:
        # print(e)
        tweets.drop(index)

    
    query = tweets.text[index]
    querywords = word_tokenize(query)
    ###### Removing stop words ######
    print(f"{i}) CLEANED: {tweets.text[index]}")
    #resultwords  = [word for word in querywords if word.lower() not in stop_Words] # removing stop words
    #resultwords  = [stemmer.stem(word) for word in resultwords] # stemming
    #resultwords  = [lemma.lemmatize(word) for word in resultwords] # lemmatizing
    #result = ' '.join(resultwords)
    #print(f"{i}) REMOVED STOP WORDS, STEMMED AND LEMMATIZED: {result}")
    resultwords  = [word for word in querywords if word.lower() not in stop_Words]
    resultwords  = [lemma.lemmatize(word) for word in resultwords]
    result = ' '.join(resultwords)
    print(f"{i}) REMOVED STOP WORDS AND LEMMATIZED: {result}\n")
    result = ' '.join(resultwords)
    tweets.text[index] = result
    print(i,index)
    
    # print()
    i+=1


print("After pre-processing the tweets") 

print(tweets.text)
tweets.to_csv('pre-processed-data.csv')


tweets = tweets.text.map(remove_rt).map(rt)
tweets = tweets.str.lower()










