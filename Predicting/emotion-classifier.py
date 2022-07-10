from transformers import pipeline
from transformers import RobertaTokenizerFast
from transformers import TFRobertaForSequenceClassification
import json
import csv
import pandas as pd

tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")
emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')
CLEANED_DATA_FILE = "../Preprocessing/pre-processed-data.csv"
data= pd.read_csv(CLEANED_DATA_FILE)
emotion_data = []
i = 0
for text in data.text:
    try:
        emotion_labels = emotion(text.split("https")[0])
        emotion_data.append([text,emotion_labels[0]["label"], emotion_labels[0]["score"]])
        i+=1
        print(f"{i} done")
        # print(f"{emotion_labels[0]['label']} {emotion_labels[0]['score']} = {text}")
    except:
        emotion_data.append([text,"error", "error"])


columns = ["Text", "Emotion", "Percentage"]
df = pd.DataFrame(emotion_data, columns=columns)
df.to_csv('emotion_data.csv')
