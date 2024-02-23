# import smtplib
# my_email='dragonkrishoredbzgt@gmail.com'
# # connection=smtplib.SMTP('smtp.gmail.com')
# # password="yoro vjbn aiva zqew"
# # connection.starttls()
# # connection.login(user=my_email,password=password)
# # connection.sendmail(from_addr=my_email,to_addrs='dragonkrishoredbzgt.cloud1@gmail.com',msg='Hello')
# # connection.close()
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     password="yoro vjbn aiva zqew"
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,to_addrs='dragonkrishoredbzgt.cloud1@gmail.com',msg='Hello')

import datetime as dt
import random as rd
import smtplib

my='dragonkrishoredbzgt@gmail.com'
to='aadhaargoel123@outlook.com'

with open('quotes.txt','r') as file:
    data=file.read().split(sep='\n')
    quote=data[rd.randint(0,len(data)-1)]

with smtplib.SMTP('smtp.gmail.com') as connection:
    password = "yoro vjbn aiva zqew"
    connection.starttls()
    connection.login(user=my, password=password)
    connection.sendmail(from_addr=my,
                        to_addrs=to,
                        msg=f'Subject:POWERED PACKED MOTIVATION!\n\n{quote}')


