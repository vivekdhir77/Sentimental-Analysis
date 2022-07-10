import pandas as pd
import matplotlib.pyplot as plt
df_emotion_data = pd.read_csv('../Predicting/emotion_data.csv')
frequency = df_emotion_data['Emotion'].value_counts().T
# frequency = frequency.rename(columns = {"error": "can't be calssified"})
print(type(frequency ))
print(frequency)
# print(frequency['error'])
frequency.drop(['neutral'], inplace = True)

frequency.plot(kind = 'bar',
        x = 'Emotions',
        y = 'Frequency',
        color = 'green')
  
# set the title
plt.title('Emotions-frequency')
  
# show the plot
plt.savefig('Emotions_frequency')
plt.show()