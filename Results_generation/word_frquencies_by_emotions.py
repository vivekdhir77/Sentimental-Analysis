import nltk
import pandas as pd
import json
nltk.download('stopwords')

data= pd.read_csv("Predicting\emotion_data.csv")

tweets = data

main_dict = {}

for index, row in tweets.iterrows():
    try:
        main_dict[tweets.Emotion[index]] = f"{str(main_dict[tweets.Emotion[index]])} " + tweets.Text[index]
    except:
        main_dict[tweets.Emotion[index]] = str(tweets.Text[index])


def mostCommon(text):
    allWords = nltk.tokenize.word_tokenize(text)
    allWordDist = nltk.FreqDist(w.lower() for w in allWords)

    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append("zelensky")
    stopwords.append("zelenskyy")
    allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)

    mostCommon = allWordExceptStopDist.most_common(100000000)

    return mostCommon

for emotion in main_dict:
    main_dict[emotion] = mostCommon(main_dict[emotion])

json_object = json.dumps(main_dict)
  
with open("word_frequencies_by_emotion.json", "w") as outfile:
    outfile.write(json_object)






