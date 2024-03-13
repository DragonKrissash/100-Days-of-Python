import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY='0NKHWVPBQR22BXAZ'
NEWS_API_KEY='4f0c39f108774e73a89816b11117d62e'
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


from requests import request
from datetime import datetime,timedelta
stockEndPoint='https://www.alphavantage.co/query'
fnc='TIME_SERIES_DAILY'
stock_params={
'function':fnc,
    'symbol':STOCK,
    'datatype':'json',
    'apikey':STOCK_API_KEY
}
response=requests.get(url=stockEndPoint,params=stock_params)
stock_data=response.json()['Time Series (Daily)']
newsEndPoint='https://newsapi.org/v2/top-headlines'
news_params={
    'apiKey':NEWS_API_KEY,
    'country':'us',
    'category':'business',
    'q':'Tesla'

}
resp=requests.get(url=newsEndPoint,params=news_params)
news_data=resp.json()
news=news_data['articles'][2]
def getStrDate(curr_date):
    day=curr_date.day
    month=curr_date.month
    year=curr_date.year
    if month<10:
        month=f'0{month}'
    if day<10:
        day=f'0{day}'
    return f'{year}-{month}-{day}'

def getHigh(date):
    high=float(stock_data[date]['2. high'])
    return high

def getStockHigh(curr_date):
    if curr_date.weekday()==0:
        date1 = curr_date - timedelta(days=3)
        date2 = curr_date - timedelta(days=4)
    elif curr_date.weekday()==6:
        date1 = curr_date - timedelta(days=2)
        date2 = curr_date - timedelta(days=3)
    elif curr_date.weekday()==5:
        date1 = curr_date - timedelta(days=1)
        date2 = curr_date - timedelta(days=2)
    elif curr_date.weekday()==1:
        date1 = curr_date - timedelta(days=1)
        date2 = curr_date - timedelta(days=4)
    else:
        date1 = curr_date - timedelta(days=1)
        date2 = curr_date - timedelta(days=2)

    date1_price=getHigh(getStrDate(date1))
    date2_price=getHigh(getStrDate(date2))
    return date1_price-date2_price

stock_dif=getStockHigh(datetime.now())
if stock_dif < 0:
    print(f"It's a bearish attack! {stock_dif}")
else:
    print(f"It's a bullish attack! {stock_dif}")
print(f"Title: {news['title']}\n"
          f"Content: {news['content']}")
