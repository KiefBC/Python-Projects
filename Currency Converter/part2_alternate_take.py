class CurrencyConverter:
    def __init__(self, amount):
        self.amount = amount
        self.exchange_rate = 100
        self.amount_after_conversion = 0

    def converter(self):
        self.amount_after_conversion = self.amount * self.exchange_rate
        print(f'I have {self.amount} conicoins.')
        print(f'{self.amount} conicoins cost {self.amount_after_conversion} dollars.')
        print('I am rich! Yippee!')


if __name__ == '__main__':
    coins = int(input())
    cc = CurrencyConverter(amount=coins)
    cc.converter()