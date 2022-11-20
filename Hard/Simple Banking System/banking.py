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

    # THIS WORKS AND CREATES OUR DB IF NOT EXISTS
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
        return

    # STEP 2 - EVERYTHING IS WORKING AS INTENDED
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

        c.execute("INSERT INTO card (id) VALUES (?)", [unique_id])
        conn.commit()

        # create Credit Card number
        card_number = f'{self.iin}{unique_id}'

        # Create and append the Luhn Algo Checksum
        for checksum in range(10):
            if self.luhn_algo(card_number + str(checksum)):
                card_number = card_number + str(checksum)
                break

        # c.execute("INSERT INTO card (number) VALUES (?, ?) WHERE id=?", [card_number, unique_id])
        c.execute("UPDATE card SET number=? WHERE id=?", [card_number, unique_id])
        conn.commit()

        # Create our PIN
        pin_creation = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        pin_number = f'{pin_creation}'

        # c.execute("INSERT INTO card (pin) VALUES (?, ?)  WHERE id=? ", [pin_number, unique_id])
        c.execute("UPDATE card SET pin=? WHERE id=?", [pin_number, unique_id])
        conn.commit()

        c.execute("SELECT * FROM card")

        # Print out our Confirmation of addition
        items = c.fetchall()

        print("Your card has been created")
        print(f'Your card number:\n{card_number}')
        print(f'Your card PIN:\n{pin_number}\n')

        # Close DB Connection
        conn.close()

        return f'{unique_id}'

    # NOW COMPLETELY ADDS THE BALANCE TO THE CURRENT USER!
    def add_balance(self, session_id):
        """
        This will allow the user to deposit funds into their account
        :param card_number:
        :return:
        """
        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        c.execute("SELECT * FROM card WHERE id=?", [session_id])
        items = c.fetchone()

        add_amount = int(input('Enter income:\n> '))
        new_balance = items[3] + add_amount

        c.execute("UPDATE card SET balance=? WHERE id=?", [new_balance, session_id])
        conn.commit()
        conn.close()
        print('\nIncome was added!\n')
        return

    # OPTION 3 - DONE!
    def transfer_funds(self, session_id):
        """
        This will allow the user to transfer funds to another account
        :param trans_card:
        :param unique_id:
        :return:
        """

        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        trans_money = int(input('Enter how much money you want to transfer:\n> '))
        c.execute("SELECT balance FROM card WHERE id=?", [session_id])
        items = c.fetchone()
        if trans_money > items[0]:
            print('Not enough money!')
            # End DB Connection
            conn.close()
            return
        else:
            new_balance = items[0] - trans_money
            c.execute("UPDATE card SET balance=? WHERE id=?", [new_balance, session_id])
            print('Success!')

            # End DB Connection
            conn.commit()
            conn.close()

            return

    # IS NOW WORKING FULLY
    def close_account(self, session_id):
        """
        This will allow the user to delete their account from our database
        :param session_id:
        :return:
        """
        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        c.execute('DELETE FROM card WHERE id=?', [session_id])
        conn.commit()
        conn.close()
        return

    # GET BALANCE DOES WHAT ITS SUPPOSED TOO
    def get_balance(self):
        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        c.execute("SELECT balance FROM card")
        items = c.fetchall()
        balance = items[-1]

        # End DB Connection
        conn.commit()
        conn.close()
        return f'\nBalance: {balance[0]}\n'

    # THE ALGORITHM WORKS FULLY
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

    # VERIFYING - NOW WORKS FLAWLESSLY
    def check_creds(self, session_id=None):
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
        card_input = input('Enter your card number:\n> ')
        pin_input = input('Enter your PIN:\n> ')

        if self.luhn_algo(card_input):
            c.execute("SELECT * FROM card WHERE id=?", [session_id[0]])
            items = c.fetchall()
            if card_input in items[0][1] and pin_input in items[0][2]:
                print('\nYou have successfully logged in!\n')

                # End DB Connection
                conn.close()

                return True
            else:
                print('Wrong card number or PIN!\n')

                # End DB Connection
                conn.close()

                return False
        else:
            print('Wrong card number or PIN!\n')

            # End DB Connection
            conn.close()

            return False

    # THIS SUCCESSFULLY DROPS THE TABLE EVERY TIME WE RUN THE SCRIPT
    def drop_table(self):
        # Connect to DB
        conn = sqlite3.connect('card.s3db')
        c = conn.cursor()

        c.execute("DROP TABLE IF EXISTS card")
        conn.commit()

        # Confirm
        # c.execute("SELECT * FROM card")
        # items = c.fetchall()
        # print(f'\nThis is our confirmation of the table being dropped: {[item for item in items]}\n')

        # Close DB Connection
        conn.commit()
        conn.close()
        return


bank = BankMachine()
bank.drop_table()
bank.initialize_db()
x = True


while x:
    # Holds all current session_id until STOP
    session_ids = []
    # Connect to DB
    conn = sqlite3.connect('card.s3db')
    c = conn.cursor()

    user_input = input("1. Create an account\n2. Log into account\n0. Exit\n> ")
    match user_input:
        case '1':  # CREATE ACCOUNT
            print("")
            # session_id = (bank.card_creation(),)
            # session_ids.append(unique_id)
            session_id = (bank.card_creation(),)
            # session_id = session_ids[-1]
        case '2':  # LOG INTO ACCOUNT
            if bank.check_creds(session_id):
                while True:
                    account_input = input(
                        '1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n> ')


                    match account_input:

                        case '1':  # balance
                            print(bank.get_balance())
                            continue


                        case '2':  # add income
                            bank.add_balance(session_id)


                        case '3':  # TRANSFERING FUNDS CROSS-ACCOUNT

                            trans_card = input('Enter card number:\n> ')
                            if_exists = c.execute("SELECT EXISTS(SELECT number FROM card WHERE number=?)", (trans_card,))
                            fetched = if_exists.fetchone()[0]

                            if bank.luhn_algo(trans_card):
                                if fetched == 1:
                                    c.execute("SELECT number FROM card")
                                    items = c.fetchall()
                                    if trans_card == items[0][0]:
                                        print("\nYou can't transfer money to the same account!\n")
                                        continue
                                    else:
                                        bank.transfer_funds(session_id)
                                else:
                                    print('\nSuch a card does not exist\n')
                                    continue
                            else:
                                print('\nProbably you made a mistake in the card number. Please try again!\n')



                        case '4':  # close account
                            conn.close()
                            bank.close_account(session_id)


                        case '5':  # log out
                            conn.close()
                            print('You have successfully logged out!')
                            break


                        case '0':
                            print('Bye!')
                            x = False
                            break


                        case _:
                            conn.close()
                            print('\nPlease select from available options.\n')
                            continue


        case '0':
            conn.close()
            print('Bye!')
            break
        case _:
            conn.close()
            print('\nPlease select from available options.\n')
            continue
