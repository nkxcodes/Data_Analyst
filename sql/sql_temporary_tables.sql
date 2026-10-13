USE students;

CREATE TABLE students(
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    marks INT,
    city VARCHAR(50)
)


INSERT INTO students (student_id, name, age, marks, city)
VALUES
(1, 'Rahul', 17, 85, 'Delhi'),
(2, 'Priya', 18, 92, 'Mumbai'),
(3, 'Aman', 17, 76, 'Jaipur'),
(4, 'Sneha', 18, 88, 'Pune'),
(5, 'Arjun', 17, 95, 'Delhi'),
(6, 'Neha', 16, 68, 'Lucknow'),
(7, 'Karan', 18, 81, 'Mumbai'),
(8, 'Ananya', 17, 73, 'Jaipur');

/*
Questions 1–3: Absolute basics
Difficulty: Easy
Q1. What is a temporary table in SQL? Explain how it differs from a regular table in terms of its
purpose and lifetime.

Q2. Write a SQL query to create a temporary table named student_backup with two columns:
student_name of type VARCHAR(100) and marks of type INT.

Q3. You have created a temporary table named high_scorers. Write a SQL query to retrieve
all rows and columns from it.
*/

-- Q1
/*
A temporary table in SQL is a table used to store data
temporarily while performing a task. It is usually
deleted automatically when the database session ends.
*/

-- Q2
CREATE TEMPORARY TABLE student_backup(
    student_name VARCHAR(100),
    marks INT
);

-- Q3
SELECT * FROM high_scorers;

/*
Questions 4–6: Core concepts
Difficulty: Medium
Q4. You want to create a temporary table named delhi_students containing the id, name,
age, and marks of students who live in Delhi. Create the temporary table using data from the
existing students table.
Q5. A temporary table named student_results already exists with columns name and
marks. Write a query to insert a new student's name and marks into it.
Q6. You want to remove all rows from a temporary table named student_results while
keeping the table itself available for further use. What SQL statement would you use?
*/

-- Q4
CREATE TEMPORARY TABLE delhi_students AS
SELECT id, name, age, marks
FROM students
WHERE city = 'Delhi';

-- Q5
INSERT INTO student_results VALUES ('Manav', 45);

-- Q6
DELETE FROM students_results;

/*
Questions 7–9: Practical application
Difficulty: Application
Q7. A teacher wants to analyze students who scored at least 75 marks without repeatedly
filtering the original students table. Create a temporary table containing the qualifying
students' IDs, names, and marks.
Q8. A school administrator wants to calculate the average marks of students from Delhi. The
administrator first wants to store the relevant student records in a temporary table and then
calculate the average from that table. Write the SQL statements needed for both steps.
Q9. You need to compare students' marks with their cities across several analysis queries.
Instead of repeatedly selecting the same columns from the original table, prepare a temporary
table containing only name, city, and marks. Choose an appropriate way to create and
populate it.
*/

-- Q7
CREATE TEMPORARY TABLE students_more_than_75_marks AS
SELECT id, name, marks
FROM students
WHERE marks >= 75;

-- Q8
CREATE TEMPORARY TABLE students_from_delhi AS
SELECT *
FROM students
WHERE city = 'Delhi';

SELECT AVG(marks) FROM students_from_delhi;

-- Q9
CREATE TEMPORARY TABLE student_02 AS
SELECT name, city, marks
FROM students;

/*
Questions 10–12: Deeper understanding
Difficulty: Tricky
Q10. Predict the behavior.
You create a temporary table named test_results in your current MySQL session, insert
three rows, and query it successfully.
What do you expect to happen to this temporary table when:
●​ You execute another query in the same session.
●​ You close the database connection and open a new session.
Explain why.
Q11. Find the mistake.
A beginner executes the following statements in MySQL:
CREATE TEMPORARY TABLE high_scorers (
name VARCHAR(100),
marks INT
);
CREATE TEMPORARY TABLE high_scorers (
name VARCHAR(100),
marks INT
);
The second statement produces an error. Explain why this happens and how the beginner could
handle the situation if the table might already exist.
Q12. Understand table names and scope.
A regular table named students already exists in a database. During the same session, you
create a temporary table that is also named students.
Explain which table MySQL uses when you refer to students in a query during that session.
What happens to the regular table itself, and why should this behavior be handled carefully?
*/

-- Q10
/*
1. The query will be successfully executed because we are
in the same session where the temporary table is been
created.
2. And after closing the database and opening a new session,
the queries for that temporary table will not work, because
that session is already ended in which that temporary table
is been created.
*/

-- Q11
/*
A second CREATE TEMPORARY TABLE statement produces an
error because a temporary table with the same name
already exists in the current session. We can use
CREATE TEMPORARY TABLE IF NOT EXISTS to avoid the error,
or drop the existing table using DROP TEMPORARY TABLE 
IF EXISTS before creating it again.
*/

-- Q12
/*
A temporary table takes precendence over a regular table with the
same name in MySQL. During that session, queries using the
shared access the temporary table. The regular table remains
unchanges and becomes accessible again after the temporary
table is removed or the session ends. This behavios must be
handles carefully because queries may retrieve data from the
temporary table instead of the regular table.
*/

/*
Questions 13–14: Mixed problems
Difficulty: Mixed
Q13. You are analyzing students whose marks meet a minimum threshold. A Python variable
stores the threshold:
minimum_marks = 80
Write a MySQL query that creates a temporary table named qualified_students containing
the id, name, and marks of students who meet the threshold.
Assume you're writing a normal SQL query, so use the threshold value directly in the SQL
statement.
Q14. A temporary table named monthly_sales contains product_name, quantity, and
unit_price. You need to generate a report that calculates total revenue for each product and
displays only products whose total revenue exceeds ₹10,000.
Write a query that use
*/

-- Q13
CREATE TEMPORARY TABLE qualified_students AS
SELECT id, name, marks
FROM students
WHERE >= 80;

-- Q14
SELECT product_name,
       SUM(quantity * unit_price) AS total_revenue
FROM monthly_sales
GROUP BY product_name
HAVING SUM(quantity * unit_price) >  10000;

/*
Question 15: Mastery challenge
Difficulty: Challenge
Q15. Student Performance Analysis
A school administrator wants to prepare a temporary working table for a student performance
report.
The report must:
●​ Include students who scored at least 75 marks.
●​ Include only students who live in Delhi or Mumbai.
●​ Store each qualifying student's id, name, city, and marks in a temporary table named
performance_report.
●​ Display the stored records for inspection.
●​ Calculate the average marks of the students in that temporary table.
Write the SQL statements needed to complete this task in MySQL.
*/

-- Q15
CREATE TEMPORARY TABLE performance_report AS
SELECT id, name, city, marks
FROM students
WHERE (city = 'Delhi' OR city = 'Mumbai')
AND marks >= 75;

SELECT * FROM performance_report;

SELECT AVG(marks) FROM performance_report;