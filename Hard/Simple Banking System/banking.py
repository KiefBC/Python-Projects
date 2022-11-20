import random
import sqlite3


class Card:
    def __init__(self, number, password):
        self.number = number
        self.password = password
        self.balance = 0


def connect_db(db_file):
    return sqlite3.connect(db_file)


def create_db():
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS card('
                   'id INTEGER PRIMARY KEY,'
                   'number TEXT,'
                   'pin TEXT,'
                   'balance INTEGER DEFAULT 0'
                   ')')
    connection.commit()


def print_menu():
    if not logged_in:
        print("1. Create an account\n2. Log into account\n0. Exit")
        return int(input())
    else:
        print('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit')
        return int(input())


def luhhn_algo(_card):
    numbers = list(str(_card.number))
    numbers = [eval(i) for i in numbers]
    # Multiply odd digits by 2
    counter = 0
    for _ in numbers:
        if counter % 2 == 0:
            numbers[counter] *= 2
        counter += 1
    counter = 0
    # Subtract 9 from digits over 9
    for number in numbers:
        if number > 9:
            numbers[counter] -= 9
        counter += 1
    # Add all numbers
    result = 0
    for number in numbers:
        result += number

    if result % 10 == 0:
        _card.number = int(str(_card.number) + '0')
        return True
    else:
        _card.number = int(str(_card.number) + str(10 - (result % 10)))
        return False


def add_card(card):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO CARD(number, pin) "
                   "VALUES ('" + str(card.number) + "', '" + str(card.password) + "')")
    connection.commit()


def create_account():
    card = Card(int('400000' + str(random.randint(100000000, 999999999))),
                random.randint(1000, 9999))
    luhhn_algo(card)
    print('Your card has been created')
    print('Your card number:')
    print(card.number)
    print('Your card PIN:')
    print(card.password)
    add_card(card)
    return card


def log_in():
    global current_card
    print('Enter your card number:')
    input_number = int(input())
    print('Enter your PIN:')
    input_pin = int(input())
    select = 'SELECT number, pin, balance from CARD where number =? and pin = ?'
    cursor = connection.cursor()
    cursor.execute(select, (str(input_number), str(input_pin)))
    card = cursor.fetchone()
    if card is not None:
        print('You have successfully logged in!')
        current_card = Card(card[0], card[1])
        current_card.balance = card[2]
        return True
    else:
        print('Wrong card number or PIN')
        return False


logged_in = False
current_card = None
connection = connect_db('card.s3db')
create_db()


def add_income():
    global current_card
    print('Enter income:')
    income = int(input())
    current_card.balance += income
    insert = "update card set balance = balance + ? where number= ?"
    cursor = connection.cursor()
    cursor.execute(insert, (income, str(current_card.number)))
    connection.commit()
    print('Income was added!')


def close_account():
    global current_card
    delete = "delete from card where number = ?"
    cursor = connection.cursor()
    cursor.execute(delete, (current_card.number,))
    connection.commit()
    print('The account has been closed!')


def check_receiver(receiver):
    select = "select number from card where number = ?"
    cursor = connection.cursor()
    cursor.execute(select, (receiver,))
    if cursor.fetchone() is not None:
        return True
    else:
        return False


def do_transfer():
    print('Transfer\n Enter card number:')
    receiver = input()
    temp = Card(receiver, '9609')
    if not luhhn_algo(temp):
        print('Probably you made a mistake in the card number.\n Please try again!')
        return
    elif not check_receiver(receiver):
        print('Such a card does not exist.')
        return
    else:
        print('How much money you want to transfer:')
        money = int(input())
        if current_card.balance < money:
            print('Not enough money!')
            return
        cursor = connection.cursor()
        cursor.execute('begin transaction')
        try:
            cursor.execute('update card set balance = balance - ? where number=?',
                           (money, current_card.number))
            cursor.execute('update card set balance = balance + ? where number = ?',
                           (money, receiver))
            cursor.execute('commit')
            connection.commit()
            current_card.balance -= money
            print('Success!')
        except sqlite3.Error:
            cursor.execute('rollback')


while True:
    choice = print_menu()
    if choice == 1:
        create_account()
    elif choice == 2:
        if not log_in():
            continue
        else:
            logged_in = True
            while True:
                choice = print_menu()
                if choice == 1:
                    print(f'Balance: {current_card.balance}')
                elif choice == 2:
                    add_income()
                elif choice == 3:
                    do_transfer()
                elif choice == 4:
                    close_account()
                elif choice == 5:
                    logged_in = False
                    print('You have successfully logged out!')
                    break
                elif choice == 0:
                    print('Bye!')
                    connection.close()
                    exit()
    elif choice == 0:
        print('Bye!')
        connection.close()
        exit()