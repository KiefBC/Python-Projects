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

-- FILLING SOME OF OUR BOXES WITH INFORMATION
-- COPYING DIRECTLY INTO ITSELF

insert_book_table = "INSERT INTO book (book_name, isbn, genre, author, book_year, book_count, book_page, rank)
SELECT book_name, isbn, genre, author, book_year, book_count, book_page, rank
from book;"

insert_staff_table = "INSERT INTO staff (full_name, gender, date_of_birth)
SELECT full_name, gender, date_of_birth
from staff;"

insert_student_table = "INSERT INTO student (full_name, gender, date_of_birth)
SELECT full_name, gender, date_of_birth
from student;"

insert_operation_table = "INSERT INTO operation (student_id, staff_id, book_id, iss_date, return_date, return_indicator)
SELECT student_id, staff_id, book_id, iss_date, return_date, return_indicator
from operation
where return_indicator = 1;"

update_staff_inf = "UPDATE staff SET full_name = 'Ashley Bailey' WHERE full_name = 'Ashley Miller';"

--UPDATE staff SET full_name = replace(full_name, 'Ashley Miller', 'Ashley Bailey');

-- this should be the one that works

--UPDATE staff SET full_name = 'Ashley Bailey' WHERE full_name = 'Ashley Miller';

update_operation_inf = "UPDATE operation SET return_date = replace(return_date, '10 days later', '10 days before'), return_indicator = replace(return_indicator, 0, 1) WHERE student_id = '3';"

--UPDATE operation SET return_date = replace(return_date, '10 days later', '10 days before'), return_indicator = replace(return_indicator, 0, 1) WHERE student_id = '3';

update_book_inf = "UPDATE book SET book_count = replace(book_count, '2', '3');"

--UPDATE book SET book_count = replace(book_count, '2', '3');
