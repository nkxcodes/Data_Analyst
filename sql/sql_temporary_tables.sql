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