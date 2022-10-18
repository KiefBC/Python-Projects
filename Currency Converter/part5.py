import requests

user_curr = input().lower()
madmoney = requests.get(f'http://www.floatrates.com/daily/{user_curr}.json').json()  # i didnt know i could do this
print(madmoney['usd'])
print(madmoney['eur'])
