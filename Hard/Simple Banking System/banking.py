import random
import sqlite3


class BankMachine:
    """
    Just a simple Bank Machine program made in Python.
    Self-explanatory. User can Create an account, login to an account or View an account
    Nothing is currently saved once the program ends.
    """
    def __init__(self):
        self.iin = '400000'
        self.cards = []
        self.pins = []
        self.main_menu = "1. Create an account\n2. Log into account\n0. Exit"
        self.account_menu = '1. Balance\n2. Log Out\n0. Exit'
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS card (
                                    id INTEGER,
                                    number TEXT,
                                    pin TEXT,
                                    balance INTEGER DEFAULT 0
                                    );""")
        self.conn.commit()

    def insert_into_db(self, user_id, card_number, pin_number, balance):
        card_number = card_number
        pin_number = pin_number
        user_id = user_id
        balance = balance
        self.cur.execute('INSERT INTO card VALUES (?, ?, ?, ?)', (user_id, card_number, pin_number, balance))
        self.conn.commit()
        return


    def menu(self):
        """
        The main menu everyone will see upon accessing our Simple Banking System
        They have 3 choices. Create, Log in or Exit
        :return:
        """
        user_input = input(f'{self.main_menu}\n> ')
        match user_input:
            case '1':
                print("")
                self.card_creation()
                return self.menu()
            case '2':
                self.check_creds()
            case '0':
                print('Bye!')
                return

    def card_creation(self):
        """
        We create our user a new Card Number and PIN
        We utilize the Luhn Algorithm and add to the DB
        We hope the Human Centipede keep it safe.
        :return:
        """
        card_creation = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        card_number = f'{self.iin}{card_creation}'
        for checksum in range(10):
            if self.luhn_algo(card_number + str(checksum)):
                card_number = card_number + str(checksum)
                break
        self.cards.append(card_number)

        pin_creation = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        pin_number = f'{pin_creation}'
        self.pins.append(pin_number)

        user_balance = int(self.get_balance())

        print(f'Your card number:\n{card_number}')
        print(f'Your card PIN:\n{pin_number}\n')

        return self.insert_into_db(card_creation, card_number, pin_number, user_balance)

    def account(self):
        """
        This is the basic User Account that the user will see once they have successfully logged in
        after verifying themselves through check_creds()
        :return:
        """
        balance = 0
        account_input = input(f'{self.account_menu}\n> ')
        match account_input:
            case '1':
                print(f'Balance: {self.get_balance()}\n')
                return self.account()
            case '2':
                print('You have successfully logged out!')
                return self.menu()
            case '0':
                print('Bye!')
                return

    def get_balance(self):
        balance = int(0)
        return balance

    def luhn_algo(self, card_number):
        """
        The Luhn algorithm will detect any single-digit error, as well as almost all transpositions of adjacent
        digits. It will not, however, detect transposition of the two-digit sequence 09 to 90 (or vice versa). It
        will detect most of the possible twin errors (it will not detect 22 ↔ 55, 33 ↔ 66 or 44 ↔ 77) :param
        card_number: :return:
        """
        card_number = [int(num) for num in card_number]
        for i in range(len(card_number)):
            if i % 2 == 0:
                card_number[i] = card_number[i] * 2
        for i in range(len(card_number)):
            if card_number[i] > 9:
                card_number[i] -= 9
        if sum(card_number) % 10 == 0:
            return True
        else:
            return False

    def check_creds(self):
        """
        This is the function for checking and verifying the credentials
        we received from the user as well as utilizing the Luhn Algo
        before accepting a PIN in case of Card Number entry error
        :return:
        """
        print("")
        card_input = input('Enter your card number:\n> ')
        pin_input = input('Enter your PIN:\n> ')
        if self.luhn_algo(card_input):
            if pin_input in self.pins:
                print('You have successfully logged in!')
                return self.account()
            else:
                print('Wrong card number or PIN!\n')
                return self.menu()
        else:
            print('Wrong card number or PIN!\n')
            return self.menu()


bank = BankMachine()
bank.menu()
