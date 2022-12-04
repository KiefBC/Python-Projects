from models import Base, session, Library, engine
import csv
import datetime
import time

# Try creating pagination for the books, so you only see 5 books at a time when viewing them
# Try giving the user options for searching for a book (besides searching by id)
# Try adding other columns to your database like topic area, difficulty level, number of pages, etc.

MAIN_MENU = """
    \r1. Add Book(s)
    \r2. View all Books
    \r3. Search for Book
    \r4. Analysis of Books
    \r5. Exit"""

SUB_MENU = """
    \r1. Edit
    \r2. Delete
    \r3. Return to Main Menu"""


def main_menu():
    print(MAIN_MENU)
    choice = input('Input Number Here: ')
    if choice in ['1', '2', '3', '4', '5']:
        return choice
    else:
        input('Please choose one of the menu items above. '
              'A number between 1-5.\nPress enter.')


def sub_menu():
    while True:
        sub_menu_choice = input(f'{SUB_MENU}\n\nWhat would you like to do?  ')
        if sub_menu_choice not in ['1', '2', '3']:
            input('Please choose one of the menu items above. '
                  'A number between 1-3.\nPress enter.')
        else:
            return sub_menu_choice


# Cleaning any input the user has entered to add books to our DB
def clean_date(data: str):
    months = months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                       'November', 'December']

    # First we need to split the Oct 17, 2022 into ['Oct', '17', '2022'] so we can index and clean
    split_date = data.split(' ')
    print(split_date)
    # We are passing in October and checking inside the List and tell me what its Index is which is [9]
    # We add + 1 because it starts at 0. Other-wise Oct would be 9 which is September
    # Datetime needs to be an Integer
    try:
        month = int(months.index(split_date[0]) + 1)
        # """
        # Recap:
        # We are taking split_date[0] which is October, and we are finding it within our months List
        # Which gives us the Index but that will give us a number 1 less because 0 Index.
        # So we will add 1 to it and turn that into a regular Integer
        # """
        day = int(split_date[1].replace(',', ''))
        year = int(split_date[2])
        date_return = datetime.date(year, month, day)
    except ValueError as ve:
        print(f'This is BAD! Error: {ve}')
        return
    else:
        print(f'Day: {day}\nMonth: {month}\nYear: {year}')
        return date_return


# Cleaning the price
def clean_price(price):
    try:
        float_p = float(price)
        print(f'Price: {float_p}')
        print(f'Price as an INT: {int(round(float_p))}')
        print(f'Price as cents: {int(float_p * 100)}')
        # returning the value in cents
        return int(float_p * 100)
    except ValueError as ve:
        print(f'Oh no. You did not give me proper input. Error: {ve}')
        return


# Cleaning any bad ID inputs from the user
def clean_id(id, options):
    try:
        book_id = int(id)
    except ValueError as ve:
        print(f'Not right bruv. Error: {ve}')
        return
    else:
        if book_id in options:
            return book_id
        else:
            print('\nBAD MAN BRUV')
            return


# Adding our CSV to our Library DB
def add_csv():
    with open('suggested_books.csv') as csv_file:
        data = csv.reader(csv_file)
        for row in data:
            # What if the Book already exists in the Library?
            # .one_or_none() will either return the book if there is one, or return none is there is no book
            book_in_db = session.query(Library).filter(Library.title == row[0]).one_or_none()
            # Now the Book will only be created if it does not exist in our Database
            if book_in_db is None:
                print(row)
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                # Create our query to add our new_book
                new_book = Library(title=title, author=author, date_pub=date, price=price)
                # Create our context Manager session()
                session.add(new_book)
        # Commit our changes
        session.commit()


# we need the column name. otherwise, are we editing name? date_pub or price?
def edit_check(column_name, current_value):
    if column_name == 'Price':
        # converting cents to dollars again
        print(f'\nYou are editing: <{column_name}>\nThe current value is: <{current_value / 100}>')
    elif column_name == 'Date':
        # translating date into string-formatted time
        print(f'\nYou are editing: <{column_name}>\nThe current value is: <{current_value.strftime("%B %d, %Y")}>')
    else:
        print(f'\nYou are editing: <{column_name}>\nThe current value is: <{current_value}>')

    if column_name == 'Date' or column_name == 'Price':
        while True:
            changes = input('What would you like to change the value to? ')
            if changes == 'Date':
                changes = clean_date(changes)
                if type(changes) == datetime.date:
                    return changes
            elif column_name == 'Price':
                changes = clean_price(changes)
                if type(changes) == int:
                    return changes
    else:
        return input('What would you like to change the value to? ')


def app():
    app_running = True
    while app_running:
        main_m = main_menu()
        match main_m:
            case '1':
                # Add our Book and Clean the Data
                name_book = input('What is the name of the book? ')
                author_book = input('Who is the Author? ')
                pub_error = True
                while pub_error:
                    pub_book = input('When was it published? (ex. October 25, 2022) ')
                    pub_book = clean_date(pub_book)
                    # If our Date is datetime valid end Loop
                    if type(pub_book) == datetime.date:
                        pub_error = False
                price_error = True
                while price_error:
                    price_book = input('What is the price? (ex. 28.99) ')
                    price_book = clean_price(price_book)
                    if type(price_book) == int:
                        price_error = False
                new_book = Library(title=name_book, author=author_book, date_pub=pub_book, price=price_book)
                session.add(new_book)
                session.commit()
                # Let the user know it was added
                print('Book Added!')
                time.sleep(2)
            case '2':
                # View all Books in our Library
                for book in session.query(Library):
                    # print(book)
                    print(f'{book.id} | {book.title} | {book.author}')
                input('\nPress <Enter> to return to the Main Menu')
            case '3':
                # let the user search for books in our DB
                id_options = []
                for book in session.query(Library):
                    id_options.append(book.id)
                id_error = True
                while id_error:
                    id_choice = input(f'''
                    ID Options: {id_options}
                    <Enter> Book ID: ''')
                    id_choice = clean_id(id_choice, id_options)
                    if type(id_choice) == int:
                        id_error = False
                    # Query the DB to see if the Book is indeed here
                    the_book = session.query(Library).filter(Library.id == id_choice).first()
                    print(f'''
                    {the_book.title} by {the_book.author}
                    Published: {the_book.date_pub}
                    Price: ${the_book.price / 100}''')  # turning Cents into Dollars
                    sub_choice = sub_menu()
                    match sub_choice:
                        case '1':
                            the_book.title = edit_check('Title', the_book.title)
                            the_book.author = edit_check('Author', the_book.author)
                            the_book.date_pub = edit_check('Published Date', the_book.date_pub)
                            the_book.price = edit_check('Price', the_book.price)
                            print(session.dirty)
                            session.commit()
                            time.sleep(2)
                        case '2':
                            # delete books
                            session.delete(the_book)
                            print('Book has been DELETED! UNDO IMPOSSIBLE!')
                            time.sleep(2)
            case '4':
                # most recent book and oldest book in the DB
                oldest_book = session.query(Library).order_by(Library.date_pub).first()
                newest_book = session.query(Library).order_by(Library.date_pub.desc()).first()
                # total number of books in DB. count returns the # of entries
                total_books = session.query(Library).count()
                # let see number of books with Python in the name. like() is similar to LIKE in SQL, and we know what
                # % does
                python_books = session.query(Library).filter(Library.title.like('%Python%')).count()
                print(f"""
                \rThe oldest book in the Library is: {oldest_book}
                \rThe newest book in the Library is: {newest_book}
                \rThe total number of books in the Library is: {total_books}
                \rThe total number of Python books are: {python_books}""")
            case '5':
                print("\nFine, whatever. goodbye. Didn't want you here anyways.")
                app_running = False
                exit()
            case _:
                print('\nWell this is embarrassing...\nPlease select once of the choices.\n(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    app()
    for book in session.query(Library):
        print(book)
