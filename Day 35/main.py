import os
from twilio.rest import Client
import requests
api_key='API_KEY'
lat=26.912434
lon=75.787270
OWN_endpoint='https://api.openweathermap.org/data/2.5/forecast'
account_sid = 'ACC_SID'
auth_token = 'AUTH_SID'
weather_params={
    'lat':lat,
    'lon':lon,
    'appid':api_key,
    'cnt':4
}
response=requests.get(url=OWN_endpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()
id=weather_data['list']
msg='Hey Kishore take an umbrella!'
will_rain=False
for data in weather_data['list']:
    id=int(data['weather'][0]['id'])
    if id<700:
        print('Bring an umbrella!')
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=msg,
        from_='NUM1',
        to='NUM2'
    )
print(message.status)