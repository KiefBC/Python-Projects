INTEGER
    is a numeric data type that represents some range of mathematical integers (usually from -2147483648 to +2147483647).
    INTEGER type is good for counters, numeric identifiers, and

DECIMAL(precision, scale).
This type has two parameters: precision and scale.
    Scale is the count of digits to the right of the decimal point.
    Precision is the total count of digits in the number.

The FLOAT data type is an approximate numeric data type used for floating-point numbers.
The FLOAT data type has an optional parameter n that specifies the precision and storage size (from 1 to 53)

VARCHAR(n)
    This type represents a string of symbols of varying lengths not longer than n
    For example, one can insert the strings apple, plum, and peach into a column with the type VARCHAR(5).
    The strings orange and banana will exceed the length restriction and the system will either truncate them or generate an error if one tries to insert such long values.

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