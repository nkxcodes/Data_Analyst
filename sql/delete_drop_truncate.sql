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
Q1. Explain the purpose of SQL DELETE, DROP, and TRUNCATE. What is the main difference
between removing rows from a table and removing the table itself?
Q2. Write a SQL query to delete the student whose id is 105 from the students table.
Q3. A school wants to remove all records from a temporary table named test_results while
keeping the table structure available for future use. Which SQL statement would you use?
*/

-- Q1
/*
DELETE:
DELETE is used to remove specific rows or all rows from a table.
We can use WHERE to remove only rows that match a condition.
The table structure remains unchanged.

TRUNCATE:
TRUNCATE is used to remove all rows from a table.
It does not support WHERE.
The table structure remains, but all its records are removed.

DROP:
DROP TABLE is used to remove the entire table,
including its data and structure.
The table must be created again if we want to use it.
*/

-- Q2
DELETE FROM students WHERE id = 105;

-- Q3
TRUNCATE TABLE test_results;