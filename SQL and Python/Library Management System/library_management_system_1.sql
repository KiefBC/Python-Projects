-- CREATING OUR TABLES TO USE IN OUR LIBRARY PROJECT
-- NOTHING SHOULD BE EMPTY

create_book_table = "CREATE TABLE book (
id INTEGER PRIMARY KEY NOT NULL,
isbn TEXT NOT NULL,
book_name TEXT NOT NULL,
genre TEXT NOT NULL,
author TEXT NOT NULL,
book_year INTEGER NOT NULL,
book_count INTEGER NOT NULL,
book_page INTEGER NOT NULL,
rank REAL NOT NULL,
FOREIGN KEY (id) REFERENCES operation(book_id)
);"

create_operation_table = "CREATE TABLE operation (
id INTEGER PRIMARY KEY NOT NULL,
student_id INTEGER NOT NULL,
staff_id INTEGER NOT NULL,
book_id INTEGER NOT NULL,
iss_date TEXT NOT NULL,
return_date TEXT NOT NULL,
return_indicator NUMERIC  NOT NULL,
FOREIGN KEY (student_id) REFERENCES student(id),
FOREIGN KEY (staff_id) REFERENCES staff(id),
FOREIGN KEY (book_id) REFERENCES book(id)
);"

create_student_table = "CREATE TABLE student (
id INTEGER PRIMARY KEY NOT NULL,
full_name TEXT NOT NULL,
gender TEXT NOT NULL,
date_of_birth TEXT NOT NULL
);"

create_staff_table = "CREATE TABLE staff (
id INTEGER PRIMARY KEY NOT NULL,
full_name TEXT NOT NULL,
gender TEXT NOT NULL,
date_of_birth TEXT NOT NULL
);"