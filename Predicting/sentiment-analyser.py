from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    # print("Overall sentiment dictionary is : ", sentiment_dict)
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
    CLEANED_DATA_FILE = "YOUR FILE PATH HERE"
    RESULTANT_FILE = "YOUR FILE PATH HERE"
    tweets = pd.read_csv(CLEANED_DATA_FILE)
    # tweets = tweets.head(5)
    result = []
    # print(tweets['Text'])
    for tweet in tweets['Text']:
        sentiment = sentiment_scores(tweet)
        result.append(sentiment)
    # print(result)
    tweets[['neg', 'neu','pos', 'polarity']] = result
    tweets.to_csv(RESULTANT_FILE, index=False)