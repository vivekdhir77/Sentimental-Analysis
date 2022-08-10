from collections import Counter
from matplotlib.ft2font import VERTICAL
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

f = open('Results_generation\hashtag_frequencies.json')
  
data = json.load(f)

word_list = []
count = 0
counts = {}

index = 10
for i in data:
    if count == index:
        break
    word_list.append(i)
    counts[i] = data[i]
    count+=1
  
# Closing file
f.close()

print(counts)

labels, values = zip(*counts.items())

# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

x_pos = []
for x in range(0,index):
    if len(labels[x])>7:
        x_pos.append(6*x)
    elif len(labels[x]) > 3 and len(labels[x]) <7:
        x_pos.append(6*x)
    else:
        x_pos.append(6*x)

    
x_pos = np.array(x_pos)

bar_width = 0.1

fig, ax = plt.subplots()
plt.bar(x_pos, values, width=10)

# add labels
plt.xticks(x_pos + bar_width, labels, rotation=VERTICAL)
plt.yscale('log')
plt.xlabel('Hashtag', fontsize=9)
plt.ylabel('Count', fontsize=9)

ax.tick_params(axis='x', labelsize=7)
plt.show()