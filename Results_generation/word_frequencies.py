import nltk
import pandas as pd
import json
nltk.download('stopwords')

data= pd.read_csv("Preprocessing\pre-processed-data.csv")

tweets = data

main_dict = {}

whole_text = ""

for index, row in tweets.iterrows():
    whole_text += f" {str(tweets.text[index])}"


def mostCommon(text):
    allWords = nltk.tokenize.word_tokenize(text)
    allWordDist = nltk.FreqDist(w.lower() for w in allWords)

    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append("zelensky")
    stopwords.append("zelenskyy")
    allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)

    mostCommon = allWordExceptStopDist.most_common(100000000)

    return mostCommon

main_dict["words"] = mostCommon(whole_text)

json_object = json.dumps(main_dict)
  
with open("word_frequencies.json", "w") as outfile:
    outfile.write(json_object)






