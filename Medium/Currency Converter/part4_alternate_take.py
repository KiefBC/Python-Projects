class CurrencyConverter:
    def __init__(self):
        self.amount = 0
        self.exchange_rate = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}

    def get_amount(self):
        self.amount = float(input())

    def converter(self):
        for currency, exchange_rate in self.exchange_rate.items():
            amount_after_conversion = round(self.amount * exchange_rate, 2)
            print(f'I will get {amount_after_conversion} {currency} from the sale of {self.amount} conicoins.')


def main():
    cc = CurrencyConverter()
    cc.get_amount()
    cc.converter()


if __name__ == '__main__':
    main()