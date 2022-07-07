import pandas as pd 

df = pd.read_csv('sentAnalysis_zdata.csv')
print(len(df)-len(df.drop_duplicates()))
