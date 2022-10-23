class CoinConvert:
    def __init__(self):
        self.amount = 0
        self.exchange_rate = 0
        self.dollar_value = 0

    def get_amount(self):
        self.amount = int(input('Please, enter the number of conicoins you have: '))

    def get_exchange_rate(self):
        self.exchange_rate = float(input('Please, enter the exchange rate: '))

    def convert(self):
        self.dollar_value = self.amount * self.exchange_rate
        print("The total amount of dollars:", self.dollar_value)

def main():
    cc = CoinConvert()
    cc.get_amount()
    cc.get_exchange_rate()
    cc.convert()

if __name__ == '__main__':
    main()