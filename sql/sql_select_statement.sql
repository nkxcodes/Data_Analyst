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
Q1. Write a SQL query to retrieve all columns and all rows from the students table.
*/

SELECT * FROM students;

-- Q2. Write a SQL query to retrieve only the name column from the students table.

SELECT name FROM students;

/*Q3. You want to display students' names and marks together, without displaying their other
information. Write the SQL query.*/

SELECT name, marks FROM students;

/*
Questions 4–6: Core concepts
Difficulty: Medium
Q4. Write a query to display the name, age, and city columns in that exact order. Does the
order of columns in your SELECT statement matter?
*/

SELECT name, age, city FROM students;

/*
Q5. The school wants to display each student's name and marks, but the marks column should
appear under the heading score in the query result. Write the query without changing the
actual table structure.
*/

SELECT name, marks AS score FROM students;

/*
Q6. Write a query that displays only the different cities present in the students table, without
repeating a city that appears multiple times.
*/

SELECT DISTINCT city FROM students;