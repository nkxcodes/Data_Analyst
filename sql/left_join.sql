
/*
Questions 1–3: Absolute basics
Q1. Understanding LEFT JOIN
You have two tables:
students
id name
1 Aman
2 Riya
3 Mohan
student_marks
student_id marks
1 85
2 92
Write a query to display every student's name and their marks, including students who do not
have a matching record in student_marks.
Q2. Understanding unmatched records
Consider these tables:
employees
id named department_id
1 Aman 10
2 Riya 20
3 Karan 30
departments
department_id department_name
10 IT
20 HR
Write a query that displays every employee's name and their department name, including
employees whose department has no matching record.
Q3. Using the tables from Q1, what rows will appear when you join students with
student_marks using a LEFT JOIN?
Write the expected output, including any NULL values.
*/

-- Q1
SELECT students.name, student_marks.marks
FROM students
LEFT JOIN student_marks
ON students.id = student_marks.student_id;

-- Q2
SELECT e.name, d.department_name
FROM employees AS e
LEFT JOIN departments AS d
ON e.department_id = d.department_id;

-- Q3
/*
Aman 85
Riya 92
Mohan NULL
*/

/*
Questions 4–6: Core concepts
Q4. Selecting specific columns
You have two tables:
●​ customers(customer_id, customer_name, city)
●​ orders(order_id, customer_id, amount)
Write a query that displays every customer’s name and city, along with their order ID and order
amount where matching orders exist.
Q5. Using table aliases
Using the employees and departments tables from Q2, write the query using short aliases
for both tables. Display the employee name, department ID, and department name.
Q6. Understanding NULL after a join
Using the customers and orders tables from Q4, write a query that displays every customer
and their order amount.
Then explain why some customers may have NULL in the order amount column even though
the customer exists in the database.
*/

-- Q4
SELECT c.name, c.city, o.order_id, o.amount
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id;

-- Q5
SELECT e.name, d.department_name
FROM employees AS e
LEFT JOIN departments AS d
ON e.department_id = d.department_id;

-- Q6
SELECT c.*, o.amount
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id;
/*
some customers may have NULL in the order amount column
even though the customer exists in the database is because
we are doing LEFT JOIN, it gives all rows from left table
and matching rows from the right table.
*/