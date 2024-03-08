import pandas as pd
from books_data import dataset
class Books():

    def showBooks(self):
            df = pd.DataFrame(dataset)
            df.columns = ['Author', 'Title']
            df['ID'] = [i for i in range(1, len(dataset)+1)]
            order = ['ID', 'Author', 'Title']
            df = df[order]
            print(df)


    def showAvailability(self,title):
        if title.lower() in [i['title'].lower() for i in dataset]:
            return True
        else:
            return False

    def addBook(self,author,title):
        data={
            'author':author,
            'title':title
        }
        dataset.append(data)

    def removeBook(self,author,title):
        data={
            'author':author,
            'title':title
        }
        dataset.pop(dataset.index(data))


# Books().addBook('Me','wow')
# Books().showBooks()
# Books().removeBook('Me','wow')
# Books().showBooks()


# df = pd.DataFrame(dataset)
#         df = df.drop(columns=['country', 'language', "imageLink", "link", "pages", ], axis=1)
#         df.columns = ['Author', 'Title', 'Year']
#         df['ID'] = [i for i in range(1, 101)]
#         order = ['ID', 'Author', 'Title', 'Year']
#         df = df[order]
#         with open('books_data.csv','w') as file:
#             df.to_csv(file,index=False)