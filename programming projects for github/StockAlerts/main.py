import requests
from twilio.rest import Client



STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = #your key here from alphavantage
NEWS_API_KEY = YOUR_NEWS_API_KEY
TWILLIO_SID = YOUR_TILLIO_SID
TWILLIO_AUTH_TOKEN = #your twillio auth token here

YOUR_TWILLIO_NUMBER = #your number from twillio 
YOUR_NUMBER = # your number that will recieve text. make sure its on your twillio confirmed recievers list.
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock prices increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock prices. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey': STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params )
# print(response.json())
data = response.json()['Time Series (Daily)']
# print(data)
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)
#  Get the day before yesterday's closing stock prices
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)
#- Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
print(difference)
up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'
# Work out the percentage difference in prices between closing prices yesterday and closing prices the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price))*100
print(diff_percent)
# - If TODO4 percentage is greater than 5 then print("Get News").
# if diff_percent > 5:
#     print('Get News')
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 0.5:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qinTitle': COMPANY_NAME,

    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    # print(articles)
#. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's text and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# "headling: {article_title}. \nBrief description "
formatted_articles = [f'{STOCK_NAME}: {up_down}{diff_percent}\nHeading: {article["text"]}.\nBrief: {article["description"]}' for article in three_articles]
print(formatted_articles)


client = Client(TWILLIO_SID, TWILLIO_AUTH_TOKEN)
#TODO 9. - Send each article as a separate message via Twilio.
for article in formatted_articles:
    message = client.messages.create(
        body= article,
        from_=YOUR_TWILLIO_NUMBER,
        to=YOUR_NUMBER
    )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

