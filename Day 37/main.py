import requests
from datetime import datetime
pixela_endpoint='https://pixe.la/v1/users'
USERNAME='dk1119'
token='SECRET_KEY'
user_params={
    'token':token,
    'username':USERNAME,
    'agreeTermsOfService':'no',
    'notMinor':'yes'
}
# response=requests.post(url=pixela_endpoint,json=user_params)
graph_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs'
id='graph1'
graph_params={
    'id':id,
    'name':'Coding Graph',
    'unit':'minutes',
    'type':'int',
    'color':'shibafu'
}
headers={
    'X-USER-TOKEN':token
}
# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.json())
post_pixel_endpoint=f'{graph_endpoint}/{id}'
qnt=40
pixel_params={
    'date':datetime.now().strftime('%Y%m%d'),
    'quantity':str(qnt)
}
# response=requests.post(url=post_pixel_endpoint,json=pixel_params,headers=headers)
update_pixel_endpoint=f'{post_pixel_endpoint}/{datetime.now().strftime('%Y%m%d')}'
response=requests.put(url=update_pixel_endpoint,json={'quantity':'70'},headers=headers)
print(response.text)