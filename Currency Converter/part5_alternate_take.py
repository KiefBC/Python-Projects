import requests


class ForeignExchange:
    def __init__(self):
        self.user_currency = None
        self.r = None

    def request(self):
        request_url = f'http://www.floatrates.com/daily/{self.user_currency}.json'
        self.r = requests.get(request_url)

    def user_currency_symbol(self):
        self.user_currency = input().lower()

    def exchange(self):
        print(self.r.json()['usd'])
        print(self.r.json()['eur'])


def main():
    fx = ForeignExchange()
    fx.user_currency_symbol()
    fx.request()
    fx.exchange()


if __name__ == '__main__':
    main()
