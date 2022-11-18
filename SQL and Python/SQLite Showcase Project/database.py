import sqlite3


def initialize_db():
    conn = sqlite3.connect('customer.db')  # customer.db or :memory:
    c = conn.cursor()

    create = c.execute("""CREATE TABLE IF NOT EXISTS customer (
            first TEXT,
            last TEXT,
            email TEXT
            )""")

    create
    conn.commit()
    conn.close()


def show_all():
    """
    query the DB and return ALL records
    :return:
    """

    # connect to DB
    conn = sqlite3.connect('customer.db')  # customer.db or :memory:
    c = conn.cursor()

    # query the DB
    c.execute("SELECT rowid, * FROM customer")
    items = c.fetchall()
    for item in items:
        print(item)

    # commit our change
    conn.commit()
    # close our connection to the DB
    conn.close()


def add_many(many):
    """
    add multiple entries at once
    :param many:
    :return:
    """
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customer VALUES (?, ?, ?)", many)
    conn.commit()
    conn.close()


def add_one(first, last, email):
    """
    add a new record to the table
    :return:
    """

    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customer VALUES (?, ?, ?)", (first, last, email))
    conn.commit()
    conn.close()


def delete_one(id):
    conn = sqlite3.connect('customer.db')  # customer.db or :memory:
    c = conn.cursor()
    c.execute("DELETE FROM customer WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


def email_lookup(email):
    """
    this is where we will search for emails of users in the DB
    :return:
    """
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customer WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)

    conn.close()
