import random
import sqlite3

class BankMachine:
    """
    Just a simple Bank Machine program made in Python.
    Self-explanatory. User can Create an account, login to an account or View an account
    Everything is saved to a database with: Unique ID, Card Number, PIN, and Balance
    """

    def __init__(self):
        self.iin = '400000'
        self.main_menu = "1. Create an account\n2. Log into account\n0. Exit"
        self.account_menu = '1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit'

    # STEP 0
    def initialize_db(self):
        """
        This will initialize our DB for use with the Banking System
        else it wont if it exists
        :return:
        """
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()
        create = c.execute("""CREATE TABLE IF NOT EXISTS card (
                                            id INTEGER,
                                            number TEXT,
                                            pin TEXT,
                                            balance INTEGER DEFAULT 0
                                            );""")
        conn.commit()
        conn.close()
        return self.menu()

    # STEP 1
    def menu(self, unique_id=None):
        """
        The main menu everyone will see upon accessing our Simple Banking System
        They have 3 choices. Create, Log in or Exit
        :return:
        """
        unique_id = unique_id
        user_input = input(f'{self.main_menu}\n> ')
        match user_input:

            # create a card
            case '1':
                print("")
                self.card_creation()

            # log into account
            case '2':
                self.check_creds(unique_id)

            # quit the app
            case '0':
                print('Bye!')
                return

    # STEP 2 - DONE!
    def card_creation(self):
        """
        We create our user a new Card Number and PIN
        We utilize the Luhn Algorithm and add to the DB
        We hope the Human Centipede keep it safe.
        :return:
        """
        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        # Create Unique Identifier
        unique_id = ''.join([str(random.randint(0, 9)) for _ in range(9)])

        # create Credit Card number
        card_number = f'{self.iin}{unique_id}'

        # Create and append the Luhn Algo Checksum
        for checksum in range(10):
            if self.luhn_algo(card_number + str(checksum)):
                card_number = card_number + str(checksum)
                break

        # Create our PIN
        pin_creation = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        pin_number = f'{pin_creation}'

        # Add the finalized Unique ID, Credit Card and PIN to our DB
        c.execute("INSERT INTO card (id, number, pin) VALUES (?, ?, ?)", (int(unique_id), card_number, pin_number))
        conn.commit()
        conn.close()

        print("Your card has been created")
        print(f'Your card number:\n{card_number}')
        print(f'Your card PIN:\n{pin_number}\n')

        return self.menu(unique_id)

    # STEP 3
    def account(self, unique_id):
        """
        This is the basic User Account that the user will see once they have successfully logged in
        after verifying themselves through check_creds()
        :return:
        """
        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        unique_id = unique_id

        c.execute("SELECT * FROM card")
        items = c.fetchall()
        print(items)


        account_input = input(f'{self.account_menu}\n> ')
        match account_input:
            case '1':  # balance
                return self.get_balance(unique_id)
            case '2': # add income
                return self.add_balance(unique_id)
            case '3':  # transfer
                trans_card = input('Enter card number:\n> ')
                if self.luhn_algo(trans_card):
                    return self.transfer_funds(trans_card, unique_id)
                else:
                    print('Probably you made a mistake in the card number. Please try again!')
                    return self.account(unique_id)
            case '4':  # close account
                return self.close_account(unique_id)
            case '5':  # log out
                print('You have successfully logged out!')
                return self.menu()
            case '0':
                print('Bye!')
                return

    # OPTION 1 - DONE!
    def add_balance(self, unique_id):
        """
        This will allow the user to deposit funds into their account
        :param unique_id:
        :return:
        """
        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        unique_id = unique_id

        add_amount = int(input('Enter income:\n> '))
        if add_amount:
            c.execute("SELECT balance FROM card WHERE id=?", [unique_id])
            items = c.fetchone()
            new_balance = items[0] + add_amount
            print(new_balance)
            c.execute("UPDATE card SET balance=? WHERE id=?", [new_balance, unique_id])
            conn.commit()
            conn.close()
            print('\nIncome was added!')
            return self.account(unique_id)

    # OPTION 3 - DONE!
    def transfer_funds(self, trans_card, unique_id):
        """
        This will allow the user to transfer funds to another account
        :param trans_card:
        :param unique_id:
        :return:
        """

        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        unique_id = unique_id
        trans_card = trans_card

        trans_money = int(input('Enter how much money you want to transfer:\n> '))
        c.execute("SELECT balance FROM card WHERE id=?", [unique_id])
        items = c.fetchone()
        print(f'These are our items: {items}')
        if trans_money > items[0]:
            print('Not enough money!')

            # End DB Connection
            conn.commit()
            conn.close()

            return self.account(unique_id)
        else:
            c.execute("SELECT balance FROM card WHERE id=?", [unique_id])
            items = c.fetchone()
            new_balance = items[0] - trans_money
            c.execute("UPDATE card SET balance=? WHERE id=?", [new_balance, unique_id])
            print('Success!')

            # End DB Connection
            conn.commit()
            conn.close()

            return self.account(unique_id)

    # OPTION 2 - DONE!
    def close_account(self, unique_id):
        """
        This will allow the user to delete their account from our database
        :param unique_id:
        :return:
        """
        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        c.execute('DELETE FROM card WHERE id=?', [unique_id])
        conn.commit()
        conn.close()
        return self.menu()

    # OPTION 3 - DONE!
    def get_balance(self, unique_id):
        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        unique_id = unique_id

        c.execute("SELECT balance FROM card WHERE id=?", [unique_id])
        items = c.fetchone()
        print(items)
        balance = items[0]
        print(f'Balance: {balance}\n')

        # End DB Connection
        conn.commit()
        conn.close()
        return self.account(unique_id)

    # THE ALGORITHM - DONE!
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

    # VERIFYING - DONE!
    def check_creds(self, unique_id):
        """
        This is the function for checking and verifying the credentials
        we received from the user as well as utilizing the Luhn Algo
        before accepting a PIN in case of Card Number entry error
        :return:
        """
        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        print("")
        unique_id = unique_id
        card_input = input('Enter your card number:\n> ')
        pin_input = input('Enter your PIN:\n> ')
        c.execute("SELECT * FROM card")
        items = c.fetchall()
        verify = [item for item in items]
        print(f'This is our Verify list: {verify}')
        if self.luhn_algo(card_input):
            if card_input in verify[-1] and pin_input in verify[-1]:
                print('\nYou have successfully logged in!\n')

                # End DB Connection
                conn.close()

                return self.account(unique_id)
            else:
                print('Wrong card number or PIN!\n')

                # End DB Connection
                conn.close()

                return self.menu(unique_id)
        else:
            print('Wrong card number or PIN!\n')

            # End DB Connection
            conn.close()

            return self.menu(unique_id)


bank = BankMachine()
bank.initialize_db()
bank.menu()
