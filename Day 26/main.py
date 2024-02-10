# # import csv
# # with open('weather_data.csv') as data_file:
# #     data=csv.reader(data_file)
# #     temp=[]
# #     for row in data:
# #         if row[1]=='temp':
# #             continue
# #         else:
# #             temp.append(int(row[1]))
# #     print(temp)
# import pandas as pd
# data=pd.read_csv('weather_data.csv')
# # data_dict=data.to_dict()
# # print(data)
# # temp_list=data['temp'].to_list()
# print(data[data.temp==data.temp.max()])
# monday=data[data.day=='Monday']
# print((monday.temp)*9/5+32)
l=[2*i for i in range(10) if i%2!=0]
print(l)