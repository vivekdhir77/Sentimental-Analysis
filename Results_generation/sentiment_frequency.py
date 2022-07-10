import pandas as pd
import matplotlib.pyplot as plt
df_emotion_data = pd.read_csv('../Predicting/pre-processed-data_sentiments.csv')
frequency = df_emotion_data['polarity'].value_counts().T
# frequency = frequency.rename(columns = {"error": "can't be calssified"})
print(type(frequency))
print(frequency)

frequency.plot(kind = 'bar',
        x = 'Sentiments',
        y = 'Frequency',
        color = 'green')
  
# set the title
plt.title('Sentiment-frequency')
  
# show the plot
plt.show()
plt.savefig('Sentiment-frequency.png')