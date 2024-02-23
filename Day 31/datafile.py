import pandas as pd
df=pd.read_csv('./data/french_words.csv')
data_file={}
french=list(df.French)
english=list(df.English)
data_file['French']=french
data_file['English']=english
print(data_file)