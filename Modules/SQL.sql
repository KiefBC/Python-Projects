INTEGER
    is a numeric data type that represents some range of mathematical integers (usually from -2147483648 to +2147483647).
    INTEGER type is good for counters, numeric identifiers, and

DECIMAL(precision, scale).
This type has two parameters: precision and scale.
    Scale is the count of digits to the right of the decimal point.
    Precision is the total count of digits in the number.

--The FLOAT data type is an approximate numeric data type used for floating-point numbers.
--The FLOAT data type has an optional parameter n that specifies the precision and storage size (from 1 to 53)

VARCHAR(n)
/*
    This type represents a string of symbols of varying lengths not longer than n
    For example, one can insert the strings apple, plum, and peach into a column with the type VARCHAR(5).
    The strings orange and banana will exceed the length restriction and the system will either truncate them or generate an error if one tries to insert such long values.
*/

BOOLEAN
    type represents boolean logic values: either TRUE or FALSE

CREATE TABLE census (
                        id INTEGER,
                        name VARCHAR(20),
                        birth_place_latitude REAL,
                        year_income DECIMAL(20,2),
                        is_parent BOOLEAN
);

YOU MAY NOTICE THIS:

CREATE TABLE table_name (
                            column_name_1 column_type_1,
    ...,
                            column_name_n column_type_n
);

You can directly specify the type of literal using the CAST(value AS type) function. Instead of the placeholders value and type, you can use your literal and type

SELECT
    CAST(1 AS DECIMAL(20,3));

In the example above, the numeric value 1 is interpreted as DECIMAL (20,3) and 1.000 as result of query.

SELECT literal;
SELECT 'Hello, World!';

To create a table, use the CREATE TABLE statement
To delete a database, you can use the DROP DATABASE statement
If you want to delete only a specific table, use the DROP TABLE statement

NULL is used in SQL to indicate that some data value is unknown or undefined
2+2∗NULL equals NULL
A NULL value can be stored in a column of any type
NOT NULL constraint in create table statement to specify that a column should not store NULL values
    NULL value basically means "value is not present".
    Nothing equals NULL; not even NULL equals NULL!

CREATE TABLE winners (
                         year INTEGER NOT NULL,
                         field VARCHAR(20) NOT NULL,
                         winner_name VARCHAR(100) NOT NULL,
                         winner_birth_year INTEGER);

SQL supports special predicates for that: IS NULL and IS NOT NULL

True:
SELECT 0+NULL IS NULL;
SELECT '' IS NOT NULL;

False:
SELECT NULL IS NOT NULL;
SELECT 1-1 IS NULL;

You can insert a new record into a table with a simple query using INSERT INTO statement
what you should do is write a list of values to be inserted after the keyword VALUES.

INSERT INTO customers (name, surname, zip_code, city)
VALUES ('Bobby', 'Ray', 60601, 'Chicago');

OR

INSERT INTO customers
VALUES ('Bobby', 'Ray', 60601, 'Chicago');

what if we want to insert more than 1 row?

INSERT INTO customers (name, surname, zip_code, city)
VALUES ('Mary', 'West', 75201, 'Dallas'),
       ('Steve', 'Palmer', 33107, 'Miami');


INSERT INTO table_name (column_1, column_2,..., column_n)
VALUES (list_of_values_1) [, (list_of_values_2), ..., (list_of_values_m)];

INSERT INTO table_name
VALUES (value_1, value_2,..., value_n);

ALTER TABLE
can be used to create, delete or change the type of columns.
You can add a new column to your table with a simple query using the ALTER TABLE statement with ADD COLUMN
To change the data type, make a query with ALTER TABLE statement and MODIFY COLUMN
To drop this column from the table, use the following query with the ALTER TABLE statement and DROP COLUMN
ALTER TABLE statement and CHANGE is used to change the name of a column

The following query will add the column employee_email to our table employees:
ALTER TABLE employees
ADD COLUMN employee_email VARCHAR(10);

As a result of the query execution, column employee_email will have the VARCHAR(45) type
ALTER TABLE employees
MODIFY COLUMN employee_email VARCHAR(45);

As a result deleting the entire native_city column
ALTER TABLE employees
DROP COLUMN native_city;

as a result changing the name of the column
ALTER TABLE employees
CHANGE employee_email email VARCHAR(45);

SUMMARY OF THE ALTER TABLE

To add a new column to the existing table, use this simple query template:
ALTER TABLE table_name
ADD COLUMN column_name DATATYPE;

The following query template can delete a column from the table:
ALTER TABLE table_name
DROP COLUMN column_name;

To change the column type, you can use this template:
ALTER TABLE table_name
MODIFY COLUMN column_name NEWDATATYPE;

To change the column name (and, possibly, datatype), use the following template:
ALTER TABLE table_name
CHANGE old_column_name new_column_name NEWDATATYPE;

FOREIN KEYS AND PRIMARY KEYS

To mark a field or a group of fields as a foreign key, we can use the FOREIGN KEY constraint and create the table employees.
keyword REFERENCES specifies the table and the primary key column or columns (in parentheses) with unique values that the foreign key points to
The structure and data type of the primary key and the foreign key must be the same

After the query execution, the table employees becomes a child table, that is, a table containing the foreign key
Now if we try to insert a tuple (1, 'Ann Riding', 4) in the table employees, we will get an error
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    department_id INT,
    CONSTRAINT fk_department FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

We can specify how SQL should act if we change the data using ON DELETE and ON UPDATE actions.
We can specify different actions:
    CASCADE: if a row in the parent table is deleted or updated, all matching rows will be deleted or updated automatically;
    SET NULL: if a row in the parent table is deleted or updated, all matching foreign key values in the child table will be set to NULL;
    RESTRICT: if we try to update or delete a row in the parent table, the operation will be rejected;
    SET DEFAULT: if a row with the corresponding value is deleted or updated, the foreign key value in the child table will be set to the default value;
    NO ACTION: this keyword can mean different actions depending on a dialect. In MySQL, it is equivalent to the RESTRICT keyword, so if we create the table employees with one of the queries below, delete and update actions in the table departments will be forbidden.

CREATE TABLE employees (
    employee_id int PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    department_id INT,
    CONSTRAINT fk_department FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

To add a foreign key to the existing table, you can use the ALTER TABLE ADD FOREIGN KEY statement
If we created our table employees without a foreign key, we can add it with a simple SQL query:

ALTER TABLE employees
ADD FOREIGN KEY (department_id) REFERENCES departments(department_id);

To add a named foreign key or a FOREIGN KEY constraint to multiple columns, use the ALTER TABLE ADD CONSTRAINT statement:

ALTER TABLE employees
ADD CONSTRAINT fk_department FOREIGN KEY (department_id)
REFERENCES departments(department_id);

To delete a foreign key, use the ALTER TABLE DROP FOREIGN KEY statement:

ALTER TABLE employees
DROP FOREIGN KEY fk_department;

This will show us the FK
SHOW CREATE TABLE customers;

The PRIMARY KEY constraint specifies a set of columns with values that can help identify any table record.
Since the primary key has to identify each table row, it must be unique and can not be null.
important thing is that a table can have one and only one primary key, but it is allowed to include multiple columns in it

CREATE TABLE chefs (
    chef_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20)
);

We assume that it's possible to have two employees with identical identifiers across different departments,
but it is impossible to have several employees with identical id's in a single department
So, we can have tuples (42, 15, 'Ann Brown') and (43, 15, 'Bob Freud') in the table
but we cannot add a tuple (42, 15, 'John Smith') to that table since there already is an Ann Brown.

In this case, we can define a named PRIMARY KEY constraint on multiple columns when we create the employee table

CREATE TABLE employees (
    department_id INT NOT NULL,
    employee_id INT NOT NULL,
    name varchar(50) NOT NULL,
    CONSTRAINT pk_employee PRIMARY KEY (department_id,employee_id)
);

Assume that we have a table named countries that was created as follows:
CREATE TABLE countries (
    country_name VARCHAR(40) NOT NULL UNIQUE,
    population INT CHECK (population > 0),
    area REAL NOT NULL
);

We want to make the column country_name our primary key
To add an unnamed PRIMARY KEY constraint to the column country_name, we use the ALTER TABLE ADD PRIMARY KEY statement

ALTER TABLE countries
ADD PRIMARY KEY (country_name);

We can also add a named PRIMARY KEY constraint to an existing table using the ALTER TABLE ADD CONSTRAINT
The query below will add a primary key pk_student. This primary key will have two columns: name and birth_date

ALTER TABLE students
ADD CONSTRAINT pk_student PRIMARY KEY (name,birth_date);

To drop the PRIMARY KEY, use ALTER TABLE DROP PRIMARY KEY:

ALTER TABLE students
DROP PRIMARY KEY;

USING ON THE CONSTRAINTS

The NOT NULL constraint will not allow adding a null value to a column. In our table employees, we can make the age column a not null one.

ALTER TABLE employees
MODIFY age INT NOT NULL;

To remove this constraint, just use ALTER TABLE MODIFY again without the NOT NULL attribute:

ALTER TABLE employees
MODIFY age INT;

You can also use this constraint in the CREATE TABLE statement. Just add it to the end of the column type declaration:

CREATE TABLE employees (
    personal_id INT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INT NOT NULL
);

The UNIQUE constraint will prohibit adding duplicate values to the column.

CREATE TABLE employees (
    personal_id INT UNIQUE,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INT
);

ALTER TABLE employees
ADD UNIQUE (personal_id);

Sometimes we have to make more than one column unique. In this case, we can define a named constraint at the end of the CREATE TABLE statement:

CREATE TABLE employees (
    personal_id INT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INT,
    CONSTRAINT uq_id_last_name UNIQUE (personal_id, last_name)
);

To drop a named constraint, you can also use ALTER TABLE DROP INDEX statement:

ALTER TABLE employees
DROP INDEX uq_id_last_name;

The CHECK constraint allows us to add a logical expression
we can say that all our employees should be older than sixteen. We can add the CHECK constraint in CREATE TABLE

CREATE TABLE employees (
    personal_id INT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INT CHECK (age > 16)
);

ALTER TABLE employees
ADD CHECK age;

ALTER TABLE employees
DROP CHECK age;

ALTER TABLE employees
ADD CONSTRAINT chk_employee CHECK (age > 16 AND personal_id > 0);

Both the CHECK constraint and a named UNIQUE constraint may be added using the ALTER TABLE ADD CONSTRAINT command.
To delete a named CHECK constraint, you can use the ALTER TABLE DROP CHECK statement.

The DEFAULT constraint defines the initial value in a column: the value that will appear if you dont insert anything
Now even if you add a new row with only personal_id, the columns first_name, last_name, and age will be defined as 'John', 'Doe', and 17 respectively.

CREATE TABLE employees (
    personal_id INT,
    first_name VARCHAR(30) DEFAULT 'John',
    last_name VARCHAR(30) DEFAULT 'Doe',
    age INT DEFAULT 17
);

To add the DEFAULT constraint to an existing table, use the ALTER TABLE ALTER SET DEFAULT statement:

ALTER TABLE employees
ALTER first_name SET DEFAULT 'John';

To delete an existing DEFAULT constraint, use the ALTER TABLE ALTER DROP DEFAULT statement:

ALTER TABLE employees
ALTER first_name DROP DEFAULT;


Obviously, a column can have more than one constraint.
For example, it is useful to combine NOT NULL and DEFAULT constraints to avoid errors when adding some new information.

CREATE TABLE employees (
    personal_id INT NOT NULL UNIQUE,
    first_name VARCHAR(30) NOT NULL DEFAULT 'John',
    last_name VARCHAR(30) NOT NULL DEFAULT 'Doe',
    age INT DEFAULT 17,
    CHECK (age > 16)
);

DATE AND TIME IN SQL

--The DATE type is used for storing a date that consists of a year, a month, and a day (without the time) in the 'YYYY-MM-DD' format
--The TIME type stores hours, minutes, and seconds in the 'hh:mm:ss' format
--The DATETIME type stores both date and time in the 'YYYY-MM-DD hh:mm:ss' format
--The TIMESTAMP is another type used to store both date and time but in MySQL and its range is more narrow than DATETIME
--The INTERVAL can use it to store the interval between two dates. There are two classes of the INTERVAL type: INTERVAL YEAR TO MONTH and INTERVAL DAY TO SECOND.

To get the current date, we can use the CURDATE() or CURRENT_DATE() functions.

SELECT CURDATE();

Likewise, to get the current time, you can use CURRENT_TIME() or CURTIME() functions. To select the current time, we can use the following function:

SELECT CURTIME();

To select both date and time, apply CURRENT_TIMESTAMP() function:

SELECT CURRENT_TIMESTAMP();

If you want to get the difference between the two dates, you can use the DATEDIFF(first_date, second_date) function.
In MySQL, you can also use the function TIMEDIFF(first_time, second_time) to get the difference between two TIME values.

For example, the query below in MySQL will return 5 as the result:

SELECT DATEDIFF('2020-05-15 09:34:34', '2020-05-10 15:34:43');

To get a part of the date, you can use the EXTRACT(unit FROM date) function, which extracts a specified piece from a given date.
The query below will extract the month from the given date and return 11 as the result:

SELECT EXTRACT(MONTH FROM '2020-11-04');

You can also add and subtract dates using DATE_ADD(date, INTERVAL value_of_interval units) and DATE_SUB(date, INTERVAL value_of_interval units) functions
add ten days to the current date, using the DATE_ADD function:

SELECT DATE_ADD(CURDATE(), INTERVAL 10 DAY);

There is also a function called ADDDATE which has two forms: the first is similar to DATE_ADD and the second accepts only days as an argument:
This query will return the date that will be in 10 days from today.

SELECT ADDDATE(CURDATE(), 10);

Lets subtract 2 years from the date '1996-11-30':

SELECT DATE_SUB('1996-11-30', INTERVAL 2 YEAR);

--to convert dates from one time zone to another, you can use CONVERT_TZ (value, from_time_zone, to_time_zone)
--As a timezone, you can use both named time zones such as 'Europe/Helsinki' or 'UTC' or offsets in the inclusive range from '-12:59' to '+13:00'. You can also use the system time zone using keyword 'SYSTEM'
--
--For example, the query below will convert the given date and time from the 'UTC' time zone to the 'US/Eastern' timezone:

SELECT CONVERT_TZ('2008-05-15 12:00:00','UTC','US/Eastern');

You can also set the time zone per session using the following query:

SET time_zone = timezone;

we can select specific attributes

SELECT
    day,
    hour,
    phenomena,
    temperature AS "temperature in Celsius",
    feels_like AS "feels like in Celsius",
    wind_speed AS "wind speed in m/s"
FROM
    weather
;

SELECT
    col1 [AS alias1], ..., colN [AS aliasN]
FROM
    table_name
;


we can also use expressions to select

SELECT
    'London' AS place,
    day,
    hour,
    phenomena,
    temperature*9/5+32 AS "temperature in Fahrenheit",
    feels_like < temperature AS "feels colder",
    wind_speed AS "wind speed in m/s"
FROM
    weather
;


SELECT
    exp1 [AS alias1], ..., expN [AS aliasN]
FROM
    table_name
;

The selection of a subset of rows from a table is called filtering.

SELECT *
FROM table
WHERE conditions

--Let's imagine that your first client wants to buy a book by Charles Dickens. Let's write a query that selects books that meet the criteria:

SELECT id, title, rating
FROM books
WHERE author = 'Charles Dickens';

= 	equality check
<, > 	less, greater
<=, >= 	less or equal, greater or equal
<>, != 	not equal

--Let's say, we want to know which products in our table cost more than 250. This time we use the > operator. The query looks like this:

SELECT *
FROM products
WHERE price > 250

--This time, we want to select all products from the table that are related to the vegetables category. Our SQL query will look like this:

SELECT *
FROM products
WHERE category = 'vegetables'


--    NOT returns True if argument equals to False and vice versa.
--    AND compares operands and returns True only if all of them are True. Alternatively, returns False.
--    OR returns True if at least one of the operands is True. Otherwise, returns False.

--In order to hire the right person for the project, we need a candidate to meet two requirements: be a Middle or a Senior and know SQL.
--Our query should look like this:

SELECT *
FROM staff
WHERE (status="Middle" OR status="Senior") AND skills="SQL"

--We can arrange the same criteria selection by using the NOT operand instead of OR:

SELECT *
FROM staff
WHERE NOT(status="Junior") AND skills="SQL"

SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');


DELETE FROM books

DELETE FROM books
WHERE quantity = 0

DELETE FROM table_name
WHERE logical_expression

--Inserting selected rows

INSERT INTO users (user, user_email, zip_code)
SELECT * FROM customers;

--Say we need to add only the information about Tomato Inc:

INSERT INTO users
SELECT
    supplier,
    supplier_email,
    zip_code,
    city
FROM
    suppliers
WHERE
    supplier = 'Tomato Inc';

INSERT INTO table1 (column_1, column_2, ..., column_n)
SELECT
    column_1,
    column_2,
    ...,
    column_n
FROM
    table2
WHERE
    condition;

--What information is necessary for making an update? Name of a table where we want to change data, column name(s) where the data resides and an expression to calculate a new value for each specified column:

UPDATE table_name
SET col1 = expr1,
    col2 = expr2,
    …,
    colN = expr;

--If for some reason all workers need to be moved to department #14, we could write the following:

UPDATE employees
SET department_id = 14;

--What if we want to celebrate such a massive change in the company's structure and give our employees a raise?
--Absolute values won’t do here, so their current salaries should be used:

UPDATE employees
SET salary = salary + 10000;

--Pay attention: during the execution of UPDATE, every row of a table is considered individually. If we want to use old value(s) to compute a new value for a cell, only cell(s) from the same row will be taken into account.

--It’s possible to update multiple columns simultaneously, so we can achieve the same result using only one query instead of two:

UPDATE employees
SET department_id = 14,
    salary = salary + 10000;

