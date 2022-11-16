import random


class BankMachine:

    def __init__(self):
        self.iin = '400000'
        self.cards = []
        self.pins = []
        self.main_menu = ("1. Create an account\n2. Log into account\n0. Exit")
        self.account_menu = ('1. Balance\n2. Log Out\n0. Exit')

    def menu(self):
        print(self.cards)
        print(self.pins)
        user_input = input(f'{self.main_menu}\n> ')
        match user_input:
            case '1':
                print(f"Your card number:\n{self.card_creation()}")
                print(f'Your card PIN:\n{self.pin_creation()}\n')
                return self.menu()
            case '2':
                self.check_creds()
            case '0':
                print('Bye!')
                return

    def card_creation(self):
        card_creation = random.randint(999999999, 9999999999)
        ready_card = f'{self.iin}{card_creation}'
        self.cards.append(ready_card)
        return f'{self.iin}{card_creation}'

    def pin_creation(self):
        pin_creation = random.randint(999, 9999)
        ready_pin = f'{pin_creation}'
        self.pins.append(ready_pin)
        return f'{ready_pin}'

    def account(self):
        account_input = input(f'{self.account_menu}\n> ')
        match account_input:
            case '1':
                print('Balance: 0\n')
            case '2':
                print('You have successfully logged out!')
                return self.menu()
            case '0':
                print('Bye!')
                return

    def check_creds(self):
        print("")
        card_input = input('Enter your card number:\n> ')
        pin_input = input('Enter your PIN:\n> ')
        if card_input in self.cards:
            if pin_input in self.pins:
                print('You have successfully logged in!')
                return self.account()
            else:
                print('Wrong card number or PIN!')
                return self.menu()
        else:
            print('Wrong card number or PIN!')
            return self.menu()


bank = BankMachine()
bank.menu()
