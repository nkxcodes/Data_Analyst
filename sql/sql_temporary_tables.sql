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