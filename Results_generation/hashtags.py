import pandas as pd
import re
from collections import Counter
import json

data= pd.read_csv("sentAnalysis_zdata.csv")
tweets = data

def extract_hash_tags(s):
    return re.findall(r"#(\w+)", s)

hash_tags = []

for index, row in tweets.iterrows():
    extracted_tags = extract_hash_tags(str(tweets.text[index]))
    if len(extracted_tags) > 0:
        try:
            print(extracted_tags)
            for tag in extracted_tags:
                hash_tags.append(tag.lower())
        except:
            pass
    

print(1)

hash_set = set(hash_tags)
counts = Counter(hash_tags)

print(counts)

json_object = json.dumps(counts)
  
with open("hashtag_frequencies.json", "w") as outfile:
    outfile.write(json_object)