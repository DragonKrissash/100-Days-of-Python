import requests
from datetime import datetime
response=requests.get(url='http://api.open-notify.org/iss-now.json')
data=response.json()
iss_lat=float(data['iss_position']['latitude'])
iss_lng=float(data['iss_position']['longitude'])
print(iss_lat,iss_lng)
lat=12.971599
lng=77.594566

def isISSNear():
    if iss_lat-5 <= lat and lat<=iss_lat+5:
        if datetime.now().hour==sunrise or datetime.now().hour==sunset:
            return True
    else:
        return False

parameters={
    'lat':lat,
    'lng':lng,
    'formatted':0
}

response=requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
data=response.json()
sunrise=int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset=int(data['results']['sunset'].split('T')[1].split(':')[0])
if isISSNear():
    print('LOOKUP!')
else:
    print('DONT LOOKUP!')