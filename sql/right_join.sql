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

/*
Questions 7–9: Practical application
Q7. Course enrollment audit
A school has these tables:
●​ courses(course_id, course_name)
●​ enrollments(enrollment_id, course_id, student_id)
The school wants a report showing every enrollment record alongside its course name. Even
enrollment records with no matching course must appear.
Write the query.
Q8. Product sales report
A shop has these tables:
●​ products(product_id, product_name, price)
●​ sales(sale_id, product_id, quantity_sold)
The manager wants a report containing every sale, along with the product name and price when
a matching product exists.
Write the query.
Q9. Finding unused departments
A company wants to identify departments that currently have no employees.
Using employees(id, name, department_id) and departments(department_id,
department_name), write a query that returns only departments without matching employee
records.
*/

-- Q7
SELECT e.*, c.course_name
FROM enrollments AS e
RIGHT JOIN courses AS c
ON e.course_id = c.course_id;

-- Q8
SELECT s.*, p.product_name, p.price
FROM products AS p
RIGHT JOIN sales AS s
ON p.product_id = s.product_id;

-- Q9
SELECT d.*
FROM employees AS e
RIGHT JOIN departments AS d
ON e.department_id = d.department_id
WHERE e.department_id IS NULL;

/*
Questions 10–12: Deeper understanding
Q10. the result
Consider these tables:
students
id name
1 Aman
2 Riya
marks
student_id subject score
1 SQL 80
1 Python 90
3 SQL 75
What result will this query produce?
SELECT s.name, m.subject, m.score
FROM students AS s
RIGHT JOIN marks AS m
ON s.id = m.student_id;
Write the expected rows. Explain why Aman appears twice and why the row with student_id
= 3 is preserved.
Q11. Find the mistake
A beginner wants to display every department, including departments without employees. They
write:
SELECT d.department_name, e.name
FROM employees AS e
RIGHT JOIN departments AS d
ON e.department_id = d.department_id
WHERE e.salary > 50000;
Assume employees contains a salary column.
Explain why this query can remove departments that have no employees. What happens to the
NULL salary values in the WHERE condition?
Q12. Understand duplicate matches
Suppose the right table contains three records for the same department, and the left table
contains two employees belonging to that department.
Answer these questions:
How many joined rows will those two employees produce for that department?
What happens to a right-table record that has no matching left-table record?
Does RIGHT JOIN guarantee one output row per right-table record?
Why can multiple matching records increase the number of result rows?
*/

-- Q10
/*
Output:
Aman SQL 80
Aman Python 90
NULL SQL 75

Explanation:

1. Aman appears twice because two records in the marks table have
    student_id = 1, matching Aman in the students table.

2. The row with student_id = 3 is preserved because marks is the
    right-hand table in the RIGHT JOIN.

3. Since no student has id = 3, the student's name is NULL.

4. Riya does not appear because she has no matching marks record.
*/

-- Q11
/*
The query can remove departments without employees because
the WHERE condition filters the result after the RIGHT JOIN.

For departments without employees, e.salary is NULL.
The condition NULL > 50000 evaluates to UNKNOWN, not TRUE.
WHERE keeps only rows where the condition is TRUE, so those
departments are removed.

The same condition also removes employees whose salary is
50000 or less.

To preserve every department while matching only employees
earning more than 50000, the salary condition should be
placed in the ON clause instead of the WHERE clause.
*/

-- Q12
/*
1. 2 employees x 3 matching records = 6 joined rows.
2. Unmatched right-table rows are preserved, with NULL
    values in the left-table columns.
3. RIGHT JOIN does not guarantee one output row per
    right-table record because mulitple matches create
    multiple rows.
*/

/*
Questions 13–14: Mixed problems
Q13. Combining RIGHT JOIN, filtering, and sorting
A company has these tables:
●​ employees(id, name, department_id, salary)
●​ departments(department_id, department_name)
Write a query that displays every department and its matching employees, including
departments without employees. Display employee names and salaries where available, and
sort the results alphabetically by department name.
Q14. Joining three tables
A school stores information in these tables:
●​ students(student_id, name)
●​ enrollments(student_id, course_id, marks)
●​ courses(course_id, course_name)
The school wants every course to appear in a report, along with the names of enrolled students
and their marks when available. Courses without enrollments must remain in the report.
Write a query joining the three tables to produce this report.
*/

-- Q13
SELECT d.*, e.name, e.salary
FROM employees AS e
RIGHT JOIN departments AS d
ON e.department_id = d.department_id
ORDER BY d.department_name ASC;

-- Q14
SELECT c.*, s.name, e.marks
FROM students AS s
RIGHT JOIN enrollments AS e
ON s.student_id = e.student_id
RIGHT JOIN courses AS c
ON e.course_id = c.course_id;

/*
Question 15: Mastery challenge
Q15. Complete Course Coverage Report
A school wants to review all courses offered during the term.
The database contains:
●​ courses(course_id, course_name)
●​ enrollments(enrollment_id, course_id, student_id, marks)
●​ students(student_id, name)
Create a report that includes every course, the enrolled student names, and their marks where
available. Courses without enrollment records must still appear. Sort the report by course name
alphabetically and then by student name.
Write one SQL query to generate the report.
*/

-- Q15
SELECT c.*, s.name, e.marks
FROM students AS s
RIGHT JOIN enrollments AS e
ON s.student_id = e.student_id
RIGHT JOIN courses AS c
ON e.course_id = c.course_id
ORDER BY c.course_name ASC, s.name ASC;