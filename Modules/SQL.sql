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

create TABLE census (
                        id INTEGER,
                        name VARCHAR(20),
                        birth_place_latitude REAL,
                        year_income DECIMAL(20,2),
                        is_parent BOOLEAN
);

YOU MAY NOTICE THIS:

create TABLE table_name (
                            column_name_1 column_type_1,
    ...,
                            column_name_n column_type_n
);

You can directly specify the type of literal using the CAST(value AS type) function. Instead of the placeholders value and type, you can use your literal and type

select
    cast(1 as decimal(20,3));

In the example above, the numeric value 1 is interpreted as DECIMAL (20,3) and 1.000 as result of query.

select literal;
select 'Hello, World!';

To create a table, use the create TABLE statement
To delete a database, you can use the drop database statement
If you want to delete only a specific table, use the drop table statement

NULL is used in SQL to indicate that some data value is unknown or undefined
2+2∗NULL equals NULL
A NULL value can be stored in a column of any type
NOT NULL constraint in create table statement to specify that a column should not store NULL values
    NULL value basically means "value is not present".
    Nothing equals NULL; not even NULL equals NULL!

create TABLE winners (
                         year INTEGER NOT NULL,
                         field VARCHAR(20) NOT NULL,
                         winner_name VARCHAR(100) NOT NULL,
                         winner_birth_year INTEGER);

SQL supports special predicates for that: IS NULL and IS NOT NULL

True:
select 0+null IS NULL;
select '' IS NOT NULL;

False:
select null IS NOT NULL;
select 1-1 IS NULL;

You can insert a new record into a table with a simple query using insert into statement
what you should do is write a list of values to be inserted after the keyword VALUES.

insert into customers (name, surname, zip_code, city)
values ('Bobby', 'Ray', 60601, 'Chicago');

OR

insert into customers
values ('Bobby', 'Ray', 60601, 'Chicago');

what if we want to insert more than 1 row?

insert into customers (name, surname, zip_code, city)
values ('Mary', 'West', 75201, 'Dallas'),
       ('Steve', 'Palmer', 33107, 'Miami');


insert into table_name (column_1, column_2,..., column_n)
values (list_of_values_1) [, (list_of_values_2), ..., (list_of_values_m)];

insert into table_name
values (value_1, value_2,..., value_n);

alter table
can be used to create, delete or change the type of columns.
You can add a new column to your table with a simple query using the alter table statement with ADD COLUMN
To change the data type, make a query with alter table statement and MODIFY COLUMN
To drop this column from the table, use the following query with the alter table statement and drop COLUMN
alter table statement and CHANGE is used to change the name of a column

The following query will add the column employee_email to our table employees:
alter table employees
add column employee_email VARCHAR(10);

As a result of the query execution, column employee_email will have the VARCHAR(45) type
alter table employees
modify COLUMN employee_email VARCHAR(45);

As a result deleting the entire native_city column
alter table employees
drop COLUMN native_city;

as a result changing the name of the column
alter table employees
CHANGE employee_email email VARCHAR(45);

SUMMARY OF THE alter table

To add a new column to the existing table, use this simple query template:
alter table table_name
add column column_name DATATYPE;

The following query template can delete a column from the table:
alter table table_name
drop COLUMN column_name;

To change the column type, you can use this template:
alter table table_name
modify COLUMN column_name NEWDATATYPE;

To change the column name (and, possibly, datatype), use the following template:
alter table table_name
CHANGE old_column_name new_column_name NEWDATATYPE;

FOREIN KEYS AND PRIMARY KEYS

To mark a field or a group of fields as a foreign key, we can use the FOREIGN KEY constraint and create the table employees.
keyword REFERENCES specifies the table and the primary key column or columns (in parentheses) with unique values that the foreign key points to
The structure and data type of the primary key and the foreign key must be the same

After the query execution, the table employees becomes a child table, that is, a table containing the foreign key
Now if we try to insert a tuple (1, 'Ann Riding', 4) in the table employees, we will get an error
create TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    department_id INT,
    CONSTRAINT fk_department FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

We can specify how SQL should act if we change the data using ON delete and ON update actions.
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
    ON delete SET NULL
    ON update CASCADE
);

To add a foreign key to the existing table, you can use the alter table add FOREIGN KEY statement
If we created our table employees without a foreign key, we can add it with a simple SQL query:

alter table employees
add FOREIGN KEY (department_id) REFERENCES departments(department_id);

To add a named foreign key or a FOREIGN KEY constraint to multiple columns, use the alter table add CONSTRAINT statement:

alter table employees
add CONSTRAINT fk_department FOREIGN KEY (department_id)
REFERENCES departments(department_id);

To delete a foreign key, use the alter table drop FOREIGN KEY statement:

alter table employees
drop FOREIGN KEY fk_department;

This will show us the FK
SHOW create TABLE customers;

The PRIMARY KEY constraint specifies a set of columns with values that can help identify any table record.
Since the primary key has to identify each table row, it must be unique and can not be null.
important thing is that a table can have one and only one primary key, but it is allowed to include multiple columns in it

create TABLE chefs (
    chef_id INT PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20)
);

We assume that it's possible to have two employees with identical identifiers across different departments,
but it is impossible to have several employees with identical id's in a single department
So, we can have tuples (42, 15, 'Ann Brown') and (43, 15, 'Bob Freud') in the table
but we cannot add a tuple (42, 15, 'John Smith') to that table since there already is an Ann Brown.

In this case, we can define a named PRIMARY KEY constraint on multiple columns when we create the employee table

create TABLE employees (
    department_id INT NOT NULL,
    employee_id INT NOT NULL,
    name varchar(50) NOT NULL,
    CONSTRAINT pk_employee PRIMARY KEY (department_id,employee_id)
);

Assume that we have a table named countries that was created as follows:
create TABLE countries (
    country_name VARCHAR(40) NOT NULL UNIQUE,
    population INT CHECK (population > 0),
    area REAL NOT NULL
);

We want to make the column country_name our primary key
To add an unnamed PRIMARY KEY constraint to the column country_name, we use the alter table add PRIMARY KEY statement

alter table countries
add PRIMARY KEY (country_name);

We can also add a named PRIMARY KEY constraint to an existing table using the alter table add CONSTRAINT
The query below will add a primary key pk_student. This primary key will have two columns: name and birth_date

alter table students
add CONSTRAINT pk_student PRIMARY KEY (name,birth_date);

To drop the PRIMARY KEY, use alter table drop PRIMARY KEY:

alter table students
drop primary key;

USING ON THE CONSTRAINTS

The NOT NULL constraint will not allow adding a null value to a column. In our table employees, we can make the age column a not null one.

alter table employees
modify age INT not NULL;

To remove this constraint, just use alter table modify again without the not NULL attribute:

alter table employees
modify age INT;

You can also use this constraint in the create TABLE statement. Just add it to the end of the column type declaration:

create TABLE employees (
    personal_id INT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INT NOT NULL
);

The UNIQUE constraint will prohibit adding duplicate values to the column.

create TABLE employees (
    personal_id INT UNIQUE,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INT
);

alter table employees
add UNIQUE (personal_id);

Sometimes we have to make more than one column unique. In this case, we can define a named constraint at the end of the create TABLE statement:

create TABLE employees (
    personal_id INT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INT,
    CONSTRAINT uq_id_last_name UNIQUE (personal_id, last_name)
);

To drop a named constraint, you can also use alter table drop index statement:

alter table employees
drop INDEX uq_id_last_name;

The CHECK constraint allows us to add a logical expression
we can say that all our employees should be older than sixteen. We can add the CHECK constraint in create TABLE

create TABLE employees (
    personal_id INT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INT CHECK (age > 16)
);

alter table employees
add CHECK age;

alter table employees
drop CHECK age;

alter table employees
add CONSTRAINT chk_employee CHECK (age > 16 AND personal_id > 0);

Both the CHECK constraint and a named UNIQUE constraint may be added using the alter table add CONSTRAINT command.
To delete a named CHECK constraint, you can use the alter table drop CHECK statement.

The DEFAULT constraint defines the initial value in a column: the value that will appear if you dont insert anything
Now even if you add a new row with only personal_id, the columns first_name, last_name, and age will be defined as 'John', 'Doe', and 17 respectively.

CREATE TABLE employees (
    personal_id INT,
    first_name VARCHAR(30) DEFAULT 'John',
    last_name VARCHAR(30) DEFAULT 'Doe',
    age INT DEFAULT 17
);

To add the DEFAULT constraint to an existing table, use the alter table alter SET DEFAULT statement:

alter table employees
alter first_name SET DEFAULT 'John';

To delete an existing DEFAULT constraint, use the alter table alter drop DEFAULT statement:

alter table employees
alter first_name drop DEFAULT;


Obviously, a column can have more than one constraint.
For example, it is useful to combine NOT NULL and DEFAULT constraints to avoid errors when adding some new information.

create TABLE employees (
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

select CURDATE();

Likewise, to get the current time, you can use CURRENT_TIME() or CURTIME() functions. To select the current time, we can use the following function:

select CURTIME();

To select both date and time, apply CURRENT_TIMESTAMP() function:

select current_timestamp();

If you want to get the difference between the two dates, you can use the DATEDIFF(first_date, second_date) function.
In MySQL, you can also use the function TIMEDIFF(first_time, second_time) to get the difference between two TIME values.

For example, the query below in MySQL will return 5 as the result:

select DATEDIFF('2020-05-15 09:34:34', '2020-05-10 15:34:43');

To get a part of the date, you can use the EXTRACT(unit FROM date) function, which extracts a specified piece from a given date.
The query below will extract the month from the given date and return 11 as the result:

select extract(month from '2020-11-04');

You can also add and subtract dates using DATE_ADD(date, INTERVAL value_of_interval units) and DATE_SUB(date, INTERVAL value_of_interval units) functions
add ten days to the current date, using the DATE_ADD function:

select DATE_ADD(CURDATE(), interval 10 day);

There is also a function called ADDDATE which has two forms: the first is similar to DATE_ADD and the second accepts only days as an argument:
This query will return the date that will be in 10 days from today.

select ADDDATE(CURDATE(), 10);

Lets subtract 2 years from the date '1996-11-30':

select DATE_SUB('1996-11-30', interval 2 year);

--to convert dates from one time zone to another, you can use CONVERT_TZ (value, from_time_zone, to_time_zone)
--As a timezone, you can use both named time zones such as 'Europe/Helsinki' or 'UTC' or offsets in the inclusive range from '-12:59' to '+13:00'. You can also use the system time zone using keyword 'SYSTEM'
--
--For example, the query below will convert the given date and time from the 'UTC' time zone to the 'US/Eastern' timezone:

select CONVERT_TZ('2008-05-15 12:00:00','UTC','US/Eastern');

You can also set the time zone per session using the following query:

SET time_zone = timezone;

we can select specific attributes

select
    day,
    hour,
    phenomena,
    temperature as "temperature in Celsius",
    feels_like as "feels like in Celsius",
    wind_speed as "wind speed in m/s"
from
    weather
;

select
    col1 [AS alias1], ..., colN [AS aliasN]
FROM
    table_name
;


we can also use expressions to select

select
    'London' as place,
    day,
    hour,
    phenomena,
    temperature*9/5+32 as "temperature in Fahrenheit",
    feels_like < temperature as "feels colder",
    wind_speed as "wind speed in m/s"
from
    weather
;


select
    exp1 [AS alias1], ..., expN [AS aliasN]
FROM
    table_name
;

The selection of a subset of rows from a table is called filtering.

select *
from table
where conditions

--Let's imagine that your first client wants to buy a book by Charles Dickens. Let's write a query that selects books that meet the criteria:

select id, title, rating
from books
where author = 'Charles Dickens';

= 	equality check
<, > 	less, greater
<=, >= 	less or equal, greater or equal
<>, != 	not equal

--Let's say, we want to know which products in our table cost more than 250. This time we use the > operator. The query looks like this:

select *
from products
where price > 250

--This time, we want to select all products from the table that are related to the vegetables category. Our SQL query will look like this:

select *
from products
where category = 'vegetables'


--    NOT returns True if argument equals to False and vice versa.
--    AND compares operands and returns True only if all of them are True. Alternatively, returns False.
--    OR returns True if at least one of the operands is True. Otherwise, returns False.

--In order to hire the right person for the project, we need a candidate to meet two requirements: be a Middle or a Senior and know SQL.
--Our query should look like this:

select *
from staff
where (status="Middle" or status="Senior") and skills="SQL"

--We can arrange the same criteria selection by using the NOT operand instead of OR:

select *
from staff
where not(status="Junior") and skills="SQL"

select * from Customers
where Country not in ('Germany', 'France', 'UK');


delete from books

delete from books
where quantity = 0

delete from table_name
where logical_expression

--Inserting selected rows

insert into users (user, user_email, zip_code)
select * from customers;

--Say we need to add only the information about Tomato Inc:

insert into users
select
    supplier,
    supplier_email,
    zip_code,
    city
from
    suppliers
where
    supplier = 'Tomato Inc';

insert into table1 (column_1, column_2, ..., column_n)
select
    column_1,
    column_2,
    ...,
    column_n
from
    table2
where
    condition;

--What information is necessary for making an update? Name of a table where we want to change data, column name(s) where the data resides and an expression to calculate a new value for each specified column:

update table_name
set col1 = expr1,
    col2 = expr2,
    …,
    colN = expr;

--If for some reason all workers need to be moved to department #14, we could write the following:

update employees
set department_id = 14;

--What if we want to celebrate such a massive change in the company's structure and give our employees a raise?
--Absolute values won’t do here, so their current salaries should be used:

update employees
set salary = salary + 10000;

--Pay attention: during the execution of UPDATE, every row of a table is considered individually. If we want to use old value(s) to compute a new value for a cell, only cell(s) from the same row will be taken into account.

--It’s possible to update multiple columns simultaneously, so we can achieve the same result using only one query instead of two:

update employees
set department_id = 14,
    salary = salary + 10000;

-- The BETWEEN operator in WHERE clause selects values that are within the given range.
-- you can think of WHERE BETWEEN as a shorthand for >= AND <= in WHERE clause

select
    product
from
    products
where
    price between 8 and 13;

-- You can also get the same result set with the query without BETWEEN:

select
    product
from
    products
where
    (price >= 8
     and price <= 13);

--To select all the products outside of the range you can use NOT BETWEEN operator:

select
    product
from
    products
where
    price not between 8 and 13;

-- The IN operator in WHERE clause is a shorthand to multiple OR conditions and allows to specify multiple values.
-- Let's select products with price equal to 10,12 or 16 from the table products from the previous example:

SELECT
    product
FROM
    products
WHERE
    price IN (10, 12, 16);

SELECT
    product
FROM
    products
WHERE
    price NOT IN (10, 12, 16);

--The LIKE operator can be used in the WHERE clause to check if a string matches a pattern.
--To create a pattern you can use two wildcard match options: % and _.
--The % represents any number of characters: zero, one, or more.
--For example, if you write a pattern %s%, the strings s, toaster, string, and cats will all match this pattern.
--The _ represents exactly one character.
--if you write pattern s_, the string so will match this pattern, but the strings s and soap will not.

--Let's select all the products with the letter 'a' in any position from our products table:

SELECT
    product
FROM
    products
WHERE
    product LIKE '%a%';

--As with BETWEEN and IN operator, you can negate LIKE operator with NOT to get all the products without the a in the product name:

SELECT
    product
FROM
    products
WHERE
    product NOT LIKE '%a%';

--The EXISTS operator checks if the subquery returns any records or not.
--If the subquery returns any records, the EXISTS operator will return TRUE, otherwise, it will return FALSE

--We will use the EXISTS operator to select all the suppliers who supply both milk and pasta:

SELECT DISTINCT
    supplier
FROM
    suppliers AS milk_suppliers
WHERE
    product = 'milk'
    AND EXISTS
(SELECT supplier
FROM
    suppliers
WHERE
    product = 'pasta'
    AND supplier = milk_suppliers.supplier);

--The negated EXISTS operator returns FALSE if the subquery returns any records and TRUE otherwise.
--We can modify our previous query to get the suppliers who supply milk but not pasta:

SELECT DISTINCT
    supplier
FROM
    suppliers AS milk_suppliers
WHERE
    product = 'milk'
    AND NOT EXISTS
(SELECT
    supplier
FROM
    suppliers
WHERE
    product = 'pasta'
    AND supplier = milk_suppliers.supplier);

--The ANY operator returns TRUE if any of the subquery values meet the condition.

--Let's use our tables products and suppliers and use ANY operator to find the supplier who supplies a product that is not listed in the products table:

SELECT DISTINCT
    supplier
FROM
    suppliers
WHERE
    NOT product = ANY (SELECT product FROM products);

--The IS NULL operator returns TRUE if the value in the column is equal to NULL.

--We can use IS NULL operator to select all rows without the information about the city from the persons table:

SELECT
    name
FROM
    persons
WHERE
    city IS NULL;

SELECT
    name
FROM
    persons
WHERE
    city IS NOT NULL;

--The IS DISTINCT FROM operator is very similar to not equality check (!= or <>).
--This operator returns TRUE only if two values are different, otherwise it returns FALSE
--YOU AND ME ARE DIFFERENT would be TRUE because we are not equal

--Let's select all the rows where the city is not equal to New-York from the persons table:

SELECT
    *
FROM
    persons
WHERE
    city IS DISTINCT FROM 'New-York';

-- this will be True because we are saying we want the result to be the same
-- NOT .... DISTINCT ... so the same.

SELECT
    *
FROM
    persons
WHERE
    city IS NOT DISTINCT FROM NULL;

--To execute an aggregate function and pass all values from a column to it, use the following syntax:

SELECT AGG_FUNCTION(column_name)
FROM table_name;

--Using the MAX function, we can easily find the highest price among all the stocks:

SELECT MAX(price)
FROM stocks;

--This query will produce 89.8. Likewise, the MIN function for the same column would give us 15.6.
--If we want to know the count of deals made yesterday, we can use this query:

SELECT SUM(yesterday_deals)
FROM stocks;

--If we want to know the count of deals made yesterday, we can use this query:

SELECT SUM(yesterday_deals)
FROM stocks;

--It is also possible to use WHERE to choose a subset of rows on which we want to run our aggregation functions.
--For example, let's find the average price and average count of deals for all stocks that cost more than 40:

SELECT
    AVG(price) AS avg_price,
    AVG(yesterday_deals) AS avg_deals
FROM
    stocks
WHERE
    price > 40;

--When working with large amounts of data, you might be interested in omitting all duplicate values.
--To do that, place the DISTINCT keyword inside the brackets of your aggregate function:

SELECT COUNT(DISTINCT yesterday_deals)
FROM stocks;

--A regular call of the COUNT function with a column name as an argument will simply count the total amount of values in the column.
--If you call COUNT with an asterisk, then you're telling the function to count all rows that exist in the table.
-- COUNT() DOES NOT COUNT NULL BUT COUNT(*) WILL

SELECT COUNT(*)
FROM stocks;

-- When you query data, SQL does not provide any default order of rows in the query evaluation result.
-- To specify the order of the resulting rows, you should use the ORDER BY clause in the query

SELECT
    hotel_id,
    hotel_name,
    price_per_night,
    price_for_early_check_in,
    rating,
    stars
FROM
    hotels
ORDER BY
    price_per_night
;

--You may sort the rows by expressions as well. For example, in the query below, we order hotels by price for two nights with an early check-in:

SELECT
    hotel_id,
    hotel_name,
    price_per_night,
    price_for_early_check_in,
    rating,
    stars
FROM
    hotels
ORDER BY
    price_per_night*2 + price_for_early_check_in
;

--The sorting is based on the definition of the comparison operator (<) for the expression type.
--It can specify whether greater or smaller values should be placed higher in the list. Let's consider an example:
-- ASC and DESC

SELECT
    hotel_id,
    hotel_name,
    price_per_night,
    price_for_early_check_in,
    rating,
    stars
FROM
    hotels
ORDER BY
    rating DESC
;

--Let's write a query that sorts hotels by both price and rating:

SELECT
    hotel_id,
    hotel_name,
    price_per_night,
    price_for_early_check_in,
    rating,
    stars
FROM
    hotels
ORDER BY
    rating DESC,
    price_per_night*2 + price_for_early_check_in
;

--we can use alias
-- the 3 is 'rating' in the select statement

SELECT
    hotel_name,
    price_per_night*2 + price_for_early_check_in AS total_price,
    rating,
    stars
FROM
    hotels
ORDER BY
    total_price, 3 DESC
;