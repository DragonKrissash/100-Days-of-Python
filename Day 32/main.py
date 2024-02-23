##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import random as rd

df=pd.read_csv('Names.csv')

my='dragonkrishoredbzgt@gmail.com'

with open('./Birthday Wisher (Day 32) start/quotes.txt') as file:
    quotes=file.read();
    quotes=quotes.split('\n')

with open('./letter_templates/letter_1.txt') as file:
    letter=file.read()

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     password = "yoro vjbn aiva zqew"
#     connection.starttls()
#     connection.login(user=my, password=password)

    # for ind,row in df.iterrows():
    #     name=row['Name']
    #     email=row['Email']
    #     letter = letter.replace('[NAME]', name)
    #     letter = letter.replace('DATA', quotes[rd.randint(0,len(quotes)-1)])
    #     connection.sendmail(from_addr=my,
    #                         to_addrs=email,
    #                         msg=f'Subject:POWERED PACKED MOTIVATION!\n\n{letter}')
for ind,row in df.iterrows():
    print(row['Name'],row['Email'])