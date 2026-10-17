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

/*
Questions 4–6: Core concepts
Difficulty: Medium
Q4. The school wants to delete all students whose marks are below 35. Write a query that
removes only those students and preserves the remaining records.
Q5. A temporary table named old_student_data is no longer needed. The school wants to
remove both the table and its stored data. Write the appropriate SQL statement.
Q6. The orders table contains thousands of records. A company wants to clear all its orders
before loading a fresh dataset, but it wants to keep the table structure. Choose the appropriate
statement and explain why it fits the requirement.
*/

-- Q4
DELETE FROM students WHERE marks < 35;

-- Q5
DROP TABLE old_student_data;

-- Q6
TRUNCATE TABLE orders;
/*
TRUNCATE removes all records from the orders table
while keeping its table structure for future use.
It is suitable for clearing a table before loading
a fresh dataset.
*/