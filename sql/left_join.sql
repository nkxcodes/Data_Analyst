
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

/*
Questions 7–9: Practical application
Q7. Customers who have never ordered
An online store wants to identify customers who have never placed an order.
Using customers(customer_id, customer_name) and orders(order_id,
customer_id, amount), write a query that displays only customers who have no matching
order.
Q8. Employee department report
A company has these tables:
●​ employees(id, name, department_id, salary)
●​ departments(department_id, department_name)
The company wants a report containing every employee's name, salary, and department name.
Employees without a matching department must still appear.
Write the query.
Q9. Products with no sales
A shop has two tables:
●​ products(product_id, product_name, price)
●​ sales(sale_id, product_id, quantity_sold)
The manager wants to find products that have never been sold.
Write a query to identify those products, including their names and prices.
*/

-- Q7
SELECT c.*, o.order_id, o.amount
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Q8
SELECT e.name, e.salary, d.department_name
FROM employees AS e
LEFT JOIN departments AS d
ON e.department_id = d.department_id;

-- Q9
SELECT p.*, s.quantity_sold
FROM products AS p
LEFT JOIN sales AS s
ON p.product_id = s.product_id
WHERE s.sale_id IS NULL;

/*
Questions 10–12: Deeper understanding
the result
Consider these tables:
students
id name
1 Aman
2 Riya
3 Mohan
marks
student_id subject score
1 SQL 80
1 Python 90
2 SQL 75
What result will this query produce?
SELECT s.name, m.subject, m.score
FROM students AS s
LEFT JOIN marks AS m
ON s.id = m.student_id;
Write the expected rows. Explain why Aman appears twice and why Mohan still appears in the
result.
Q11. Find the mistake
A beginner wants to display every customer, including those who have not placed an order.
They write:
SELECT c.customer_name, o.amount
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id
WHERE o.amount > 1000;
Explain why this query may fail to preserve customers who have no orders. What happens to
rows where o.amount is NULL?
Q12. Understand duplicate matches
Suppose a customer has three matching orders, another customer has one order, and a third
customer has no orders.
Answer these questions:
How many result rows will each customer contribute to a LEFT JOIN?
Will the customer without orders still appear?
Does LEFT JOIN automatically return only one row per customer?
What happens when a single left-table record matches several right-table records?
*/

-- Q10
/*
Expected rows:
Aman  | SQL    | 80
Aman  | Python | 90
Riya  | SQL    | 75
Mohan | NULL   | NULL

Aman appears twice because he has two matching records in
the marks table.

Mohan still appears because LEFT JOIN keeps all students,
even if they have no matching record in the marks table.
NULL means no matching marks information was found.
*/

-- Q11
/*
The WHERE condition filters out customers who have no
orders.

For customers without orders, o.amount is NULL.
The condition NULL > 1000 evaluates to UNKNOWN, so
those rows are excluded by WHERE.

Although LEFT JOIN preserves every customer intially,
the WHERE condition removes customers without matching
orders.
*/

-- Q12
/*
1. Aman contributes 3 rows, Riya contributes 1 row,
    and Mohan contributes 1 row.

2. Mohan still appears because LEFT JOIN preserves
    all records from the left table.

3. LEFT JOIN does not automatically return one row
    per customer.

4. When one customer matches multiple orders, SQL
    returns one row for each matching pair.
*/

/*
Questions 13–14: Mixed problems
Q13. Combining LEFT JOIN, conditions, and sorting
A school has these tables:
●​ students(student_id, name, city)
●​ enrollments(student_id, course_id, marks)
Write a query that displays every student's name and city, along with their marks when
available. Sort the results alphabetically by student name.
Q14. Joining three tables
A school stores data in these tables:
●​ students(student_id, name, city)
●​ enrollments(student_id, course_id, marks)
●​ courses(course_id, course_name)
The school wants to display every student and their enrolled course names and marks when
available. Students without enrollment records must still appear.
Write a query that produces this report.
*/

-- Q13
SELECT s.name, s.city, e.marks
FROM students AS s
LEFT JOIN enrollments AS e
ON s.student_id = e.student_id
ORDER BY s.name ASC;

-- Q14
SELECT s.*, c.course_name, e.marks
FROM students AS s
LEFT JOIN enrollments AS e
ON s.student_id = e.student_id
LEFT JOIN courses AS c
ON e.course_id = c.course_id;

/*
Question 15: Mastery challenge
Q15. Student Enrollment Audit
A school wants to identify students who may need follow-up because they have not enrolled in
any course.
The database contains:
●​ students(student_id, name, city)
●​ enrollments(student_id, course_id, enrollment_date)
●​ courses(course_id, course_name)
Create a report that displays each student’s name and city, along with their course name and
enrollment date when available. Students without enrollments must remain in the report. Your
final report should make it possible to identify students who have no enrollment records.
Write one SQL query to generate the report.
*/

-- Q15
SELECT s.name, s.city, c.course_name, e.enrollment_date
FROM students AS s
LEFT JOIN enrollments AS e
ON s.student_id = e.student_id
LEFT JOIN courses AS c
ON e.course_id = c.course_id;