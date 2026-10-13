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