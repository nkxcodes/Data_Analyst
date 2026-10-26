/*
SQL RIGHT JOIN — 15 Practice Questions
Questions 1–3: Absolute basics
Q1. Understanding RIGHT JOIN
You have two tables:
students
id name
1 Aman
2 Riya

student_marks
student_id marks
1 85
2 92
3 78
Write a query to display every record from student_marks along with the matching student
name, including marks records that have no matching student.
Q2. Understanding which rows are preserved
Consider these tables:
employees
id name department_id
1 Aman 10
2 Riya 20

departments
department_id department_name
10IT
20HR
30Finance
Write a query that displays every department and the names of employees belonging to it.
Departments without employees must also appear.

Q3. the result
Using the tables from Q2, the output of a RIGHT JOIN between employees and
departments, matching their department_id columns.
Write the expected rows, including any NULL values, and explain why Finance appears even
though no employee belongs to it.
*/

-- Q1
SELECT student_marks.*, students.name
FROM students
RIGHT JOIN student_marks
ON students.id = student_marks.student_id;

-- Q2
SELECT d.*, e.name
FROM employees AS e
RIGHT JOIN departments AS d
ON e.department_id = d.department_id;

-- Q3
/*
10 IT Aman
20 HR Riya
30 FINANCE NULL

FINANCE appeared because we are using RIGHT JOIN with 
departments table on the right side, it give us the all
data from the right table even if the data does not have
matching columns or values in the left table.
*/

/*
Questions 4–6: Core concepts
Q4. Selecting specific columns
You have two tables:
●​ customers(customer_id, customer_name)
●​ orders(order_id, customer_id, amount)
Write a query that displays every order alongside the matching customer name. Every order
must appear, even if its customer_id does not match a customer record.
Q5. Using table aliases
Using the employees and departments tables from Q2, write the query using short aliases
for both tables. Display the department name, employee name, and employee ID.
Q6. Filtering joined results
Using the employees and departments tables from Q2, display every department but include
employee details only when the employee's salary is greater than 50,000.
Assume the employees table also contains a salary column. Departments without a
qualifying employee must remain in the result.
*/

-- Q4
SELECT o.*, c.customer_name
FROM customers AS c
RIGHT JOIN orders AS o
ON c.customer_id = o.customer_id;

-- Q5
SELECT d.department_name, e.name, e.id
FROM employees AS e
RIGHT JOIN departments AS d
ON e.department_id = d.department_id;

-- Q6
SELECT d.department_name, e.name, e.id
FROM employees AS e
RIGHT JOIN departments AS d
ON e.department_id = d.department_id
AND e.salary > 50000;