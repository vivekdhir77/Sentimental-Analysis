import nltk
import pandas as pd
import json
nltk.download('stopwords')

data= pd.read_csv("Predicting\pre-processed-data_sentiments.csv")
tweets = data

negative_text = ""
positive_text = ""
neutral_text = ""

main_dict = {}
for index, row in tweets.iterrows():
    if tweets.polarity[index] == "-1" or tweets.polarity[index] == -1:
        negative_text += str(f"{tweets.text[index]}")
    elif tweets.polarity[index] == "1" or tweets.polarity[index] == 1:
        positive_text += str(f"{tweets.text[index]}")
    else:
        neutral_text += str(f"{tweets.text[index]}")

def mostCommon(text):
    allWords = nltk.tokenize.word_tokenize(text)
    allWordDist = nltk.FreqDist(w.lower() for w in allWords)

    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append("zelensky")
    stopwords.append("zelenskyy")
    allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)

    mostCommon = allWordExceptStopDist.most_common(1000000000)
    return mostCommon

main_dict["pos"] = mostCommon(positive_text)
main_dict["neg"] = mostCommon(negative_text)
main_dict["neu"] = mostCommon(neutral_text)


json_object = json.dumps(main_dict)
  
with open("word_frequencies_by_polarity.json", "w") as outfile:
    outfile.write(json_object)






