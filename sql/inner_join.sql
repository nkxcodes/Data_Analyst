CREATE DATABASE joins;

USE joins;

CREATE TABLE students (
    id int(3) primary key,
    name varchar(50)
)

CREATE TABLE student_marks (
    student_id int(3) foreign key,
    marks int(4)
)

INSERT INTO students (id, name)
VALUES (1, 'Aman'), (2, 'Riya'), (3, 'Mohan')

INSERT INTO student_marks (student_id, name)
VALUES (1, 85), (2, 92), (4, 70)

/*
Q1. Write a query to display each student's name and marks by matching students.id with
student_marks.student_id.
Q2. Joining two tables
You have these tables:
employees
id name department_id
1 Aman 10
2 Riya 20
3 Karan 30
departments
department_id department_name
10 IT
20 HR
40 Finance
Write a query to display employee names alongside their department names.
Q3. Understanding matching records
Using the tables from Q2, which employees will appear in the result of an INNER JOIN.
Explain why an employee whose department_id has no matching row in departments may
not appear in the result.
*/

-- Q1

SELECT students.name, student_marks.marks
FROM students
INNER JOIN student_marks
ON students.id = student_marks.student_id;

-- Q2
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments
ON employees.id = departments.department_id;

-- Q3
/*
An INNER JOIN returns only records that have matching
values in both tables. Aman (department_id = 10)
matches IT, and Riys (department_id = 20) matches HR.
Karan (department_id = 30) has no matching department, 
he is excluded.
*/

/*
Questions 4–6: Core concepts
Q4. Selecting specific columns
You have an orders table containing order_id, customer_id, and amount, and a
customers table containing customer_id and customer_name.
Write a query that displays only order_id, customer_name, and amount for matching
records.
Q5. Joining with table aliases
Using the employees and departments tables from Q2, write the same type of report as
before, but use short table aliases instead of writing the full table names repeatedly.
Q6. Applying a condition to joined data
Using the employees and departments tables, display only employees who belong to the IT
department.
Your result should contain the employee's name and department name.
*/

-- Q4
SELECT orders.order_id, customers.customer_name, orders.amount
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;

-- Q5
SELECT e.name, d.department_name
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.department_id;

-- Q6
SELECT e.name, d.department_name
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.department_id
WHERE d.department_name = 'IT';

/*
Questions 7–9: Practical application
Q7. Customer order report
An online store has two tables:
●​ customers(customer_id, customer_name, city)
●​ orders(order_id, customer_id, amount)
The manager wants a report showing each customer's name, city, order ID, and order amount.
Write the query needed to generate this report.
Q8. Students and courses
A school has these tables:
●​ students(student_id, name, age)
●​ enrollments(student_id, course_id)
●​ courses(course_id, course_name)
The school wants to see which students are enrolled in which courses.
Write a query displaying each student's name and the course name.
Q9. Finding qualifying purchases
Using the customers and orders tables from Q7, the manager wants to see customers
whose orders have an amount greater than 1,000.
Display the customer name, order ID, and amount.
*/

-- Q7
SELECT c.customer_name, c.city, o.order_id, o.amount
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id;

-- Q8
SELECT s.name, c.course_name
FROM students AS s
INNER JOIN enrollments AS e
ON s.student_id = e.student_id
INNER JOIN courses AS c
ON e.course_id = c.course_id;

-- Q9
SELECT c.customer_name, o.order_id, o.amount
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id
WHERE o.amount > 1000;