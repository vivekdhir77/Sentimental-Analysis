import nltk
import pandas as pd
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


data= pd.read_csv("Preprocessing\pre-processed-data.csv")
tweets = data

full_Text = ""
for index, row in tweets.iterrows():
    if index != 0:
        full_Text += " "
    full_Text += str(f"{tweets.text[index]}")

print(full_Text)

raw = full_Text
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

tokens_l = [w.lower() for w in tokens]

### removing nouns
only_nn = [x for (x,y) in tokens_l if y in ('NN')]

freq = nltk.FreqDist(only_nn)


print(freq.most_common(3))

