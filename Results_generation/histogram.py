from collections import Counter
from matplotlib.ft2font import VERTICAL
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data= pd.read_csv("Results_generation\word_frequencies.csv")

tweets = data


words = tweets.word.tolist()

count = tweets.word_count.tolist()

counts = {}

for i in range(len(words)):
    counts[words[i]] = count[i]

word_list = words


labels, values = zip(*counts.items())

# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0.1


plt.bar(indexes, values, width=1)

# add labels
plt.xticks(indexes + bar_width, labels, rotation=VERTICAL)
plt.yscale('log')
plt.xlabel('Word', fontsize=9)
plt.ylabel('Count', fontsize=9)
plt.show()