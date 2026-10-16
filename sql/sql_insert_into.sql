USE students;

CREATE TABLE students(
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    marks INT,
    city VARCHAR(50)
)

/*
Questions 1–3: Absolute basics
Difficulty: Easy
Q1. What does the SQL INSERT INTO statement do? Explain the difference between inserting
a new row and retrieving an existing row.
Q2. Write a SQL query to insert a student with these details into the students table:
Name: Aman
Age: 17
City: Delhi
Gender: Male
Marks: 85
Q3. You want to insert a student named Riya, aged 16, who lives in Mumbai and has scored 92
marks. The gender column is optional for this exercise. Write a query that inserts the provided
information without specifying the id column.
*/

-- Q1
/*
The SQL INSERT INTO statement is used to add new records
(rows) to a database table.

Inserting a new row adds new data to the table, whereas retrieving
an existing row means fetching stored data using the
SELECT statement. INSERT INTO changes the table's data by
adding a record, while SELECT only retrieves data without
modifying it.
*/

-- Q2
INSERT INTO students (name, age, city, gender, marks)
VALUES ('Aman', 17, 'Delhi', 'Male', 85)

-- Q3
INSERT INTO students (name, age, city, marks)
VALUES ('Riya', 16, 'Mumbai', 92)

/*
Questions 4–6: Core concepts
Difficulty: Medium
Q4. Write a single SQL statement to insert three students into the students table:
name
age
city
gender
marks
Karan 17 Jaipur Male 78
Neha 16 Delhi Female 88
Arjun 18 Mumbai Male 73
Q5. A table named employees contains the columns id, name, department, and salary.
You want to insert an employee with a name of Priya and a salary of 45,000, leaving
department to its default value if one is defined. Write the query, assuming id is
auto-incremented.
Q6. The products table has columns product_id, product_name, price, and stock.
Write a query that inserts a product with the values 101, Notebook, 50, and 200, explicitly
matching each value to its intended column.
*/

-- Q4
INSERT INTO students (name, age, city, gender, marks)
VALUES ('Karan', 17, 'Jaipur', 'Male', 78), ('Neha', 16, 'Delhi', 'Female', 88), ('Arjun', 18, 'Mumbai', 'Male', 73);

-- Q5
INSERT INTO employees (name, salary)
VALUES ('Priya', 45000);

-- Q6
INSERT INTO products (product_id, product_name, price, stock)
VALUES (101, 'Notebook', 50, 200);

/*
Questions 7–9: Practical application
Difficulty: Application
Q7. A school administrator receives records for two new students. Both records need to be
added to the existing students table. Decide how you would insert both records efficiently in
one SQL statement.
Use these records:
●​ Meera, 17, Delhi, Female, 81 marks
●​ Rahul, 18, Jaipur, Male, 76 marks
Assume id is auto-incremented.
Q8. A company has an existing table called new_employees with the columns name,
department, and salary. Another table, applicants, contains the same columns and holds
the records of selected applicants.
Write a query to copy all applicants into new_employees without manually entering every
person's information.
Q9. An online store receives a new order with an order ID of 501, customer ID of 12, and total
amount of 2,500. The orders table contains order_id, customer_id, and total_amount.
Write the query needed to record this order.
*/

-- Q7
INSERT INTO students (name, age, city, gender, marks)
VALUES ('Meera', 17, 'Delhi', 'Female', 81), ('Rahul', 18, 'Jaipur', 'Male', 76);

-- Q8
INSERT INTO new_employees (name, department, salary)
SELECT name, department, salary
FROM applicants;

-- Q9
INSERT INTO orders (order_id, customer_id, total_amount)
VALUES (501, 12, 2500);