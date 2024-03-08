import pandas as pd
from books_data import dataset
df=pd.DataFrame(dataset)
df=df.drop(columns=['country','language',"imageLink","link","pages",],axis=1)
df.columns=['Author','Title','Year']
df['ID']=[i for i in range(1,101)]
order=['ID','Author','Title','Year']
df=df[order]
print (df)
class Books():
    def showAvailability(self,title):
        if title.lower() in [i.lower() for i in list(df['Title'])]:
            return True
        else:
            return False


book=Books()
print(book.showAvailability('mahabharata'))
