from user_data import dataset
from datetime import datetime,timedelta
class User():
    def addUser(self,name,id):
        data={
            'Name':name,
            'ID':id,
            'Books_Borrowed':0,
            'Books':[]
        }
        dataset.append(data)

    def bookBorrowed(self,user_name,title,author):
        for user in dataset:
            if user['Name']==user_name:
                day=datetime.now().day
                month=datetime.now().month
                year=datetime.now().year
                borrow_date=datetime(year,month,day)
                due_date=borrow_date+timedelta(days=14)
                borrow_date=borrow_date.strftime("%d-%m-%Y")
                due_date=due_date.strftime("%d-%m-%Y")
                user['Books_Borrowed']+=1
                book_data={
                        'title':title,
                        'author':author,
                        'borrow_date':borrow_date,
                        'due_date':due_date
                }
                user["Books"].append(book_data)
                print(f'Your borrow date is: {borrow_date} \nDue date is: {due_date}')

    def bookReturned(self,user_name,title):
        for user in dataset:
            if user['Name']==user_name:
                day = datetime.now().day
                month = datetime.now().month
                year = datetime.now().year
                current_date=datetime(year,month,day)
                for book in user['Books']:
                    if book['title']==title:
                        due_date=book['due_date']
                due_date=datetime.strptime(due_date,"%d-%m-%Y")
                days_dif=(due_date-current_date).days
                if days_dif<=14 and days_dif>=0:
                    print('Thank you! Hope you enjoyed the book!')
                else:
                    print('You have crossed your due date!')
                    print(f'You need to pay a fine of ${-days_dif}')

    def extendDue(self,user_name,title):
        for user in dataset:
            if user['Name']==user_name:
                for book in user['Books']:
                    if book['title']==title:
                        due_date=book['due_date']
                        due_date=datetime.strptime(due_date,"%d-%m-%Y")
                        due_date=due_date+timedelta(days=7)
                        due_date = due_date.strftime("%d-%m-%Y")
                        print('Your due date has been extended by 7 days!\nDue date: ',due_date)

#
# User().addUser('Krishna','1')
# User().bookBorrowed('Krishna','Mahabharata','vyasa')
# User().bookReturned('Krishna','Mahabharata')
# User().extendDue('Krishna','Mahabharata')