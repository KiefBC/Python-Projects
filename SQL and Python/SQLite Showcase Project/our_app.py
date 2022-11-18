import database


database.initialize_db()
database.add_one("Laura", "Smith", "lsmith@mailme.com")
many_customers = [
    ('West', 'Brown', 'wes@mailmenowhere.ca'),
    ('Mary', 'Breef', 'mary@mailme.com'),
    ('Jim', 'Bobby', 'jimbo@nowhere.com'),
    ('Luke', 'Broff', 'lukeb@nowhere.com'),
    ('Kim', 'Lob', 'kimbo@nowhere.com')
]
database.add_many(many_customers)

# delete records
database.delete_one('6')

# show all the records
database.show_all()

# search/query our DB
database.email_lookup('kimbo@nowhere.com')


