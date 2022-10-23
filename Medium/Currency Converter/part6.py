import requests

CHECKING_CACHE = 'Checking the cache...'
IN_CACHE = 'Oh! It is in the cache!'
NOT_IN_CACHE = 'Sorry, but it is not in the cache!'


class ForeignExchange:
    def __init__(self):
        self.amount = 0.0
        self.from_currency = None
        self.to_currency = None
        self.rates_cache = {}

    def request(self, code_currency):
        url = f'http://www.floatrates.com/daily/{code_currency}.json'
        return requests.get(url).json()

    def user_currency_symbol(self):
        return input().lower()

    def cached_exchange_rates(self):
        self.rates_cache['usd'] = self.request(code_currency='usd')
        self.rates_cache['eur'] = self.request(code_currency='eur')

    def exchange_rates(self):
        self.rates_cache[self.to_currency] = self.request(code_currency=self.to_currency)

    def currency_conversion(self):
        result = round(self.amount * self.rates_cache[self.to_currency][self.from_currency]['inverseRate'], 2)
        return result

    def exchange(self):
        self.from_currency = self.user_currency_symbol()
        self.cached_exchange_rates()
        while to_currency := self.user_currency_symbol():
            self.to_currency = to_currency
            self.amount = float(input())
            print(CHECKING_CACHE)
            if self.to_currency in self.rates_cache:
                print(IN_CACHE)
            else:
                print(NOT_IN_CACHE)
                self.exchange_rates()
            print(f'You received {self.currency_conversion()} {self.to_currency.upper()}.')


def main():
    fx = ForeignExchange()
    fx.exchange()


if __name__ == '__main__':
    main()
