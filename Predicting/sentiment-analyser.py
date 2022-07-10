from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np
def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    # print("Overall sentiment: ", sentiment_dict)
    # print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    # print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    # print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    # print("Sentence Overall Rated As", end = " ")
    final_result = 0
    if sentiment_dict['compound'] >= 0.05 :
        final_result = 1
    elif sentiment_dict['compound'] <= - 0.05 :
        final_result = -1
    return [sentiment_dict['neg']*100, sentiment_dict['neu']*100, sentiment_dict['pos']*100, final_result]

if __name__ == "__main__" :
    CLEANED_DATA_FILE = "../Preprocessing/pre-processed-data.csv"
    RESULTANT_FILE = "pre-processed-data_sentiments.csv"
    tweets = pd.read_csv(CLEANED_DATA_FILE)
    # tweets = tweets.head(5)
    result = []
    # print(tweets['text'][0])
    i = 0
    for tweet in tweets['text']:
        try:
            # print(tweet)
            print(i)
            sentiment = sentiment_scores(tweet)
            result.append(sentiment)
            i = i+1
        except:
            result.append([np.nan,np.nan,np.nan, np.nan])
    # print(result)
    tweets[['neg', 'neu','pos', 'polarity']] = result
    tweets.to_csv(RESULTANT_FILE, index=False)