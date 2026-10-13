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
Q1. Write a SQL query to display all columns of students whose marks are greater than 80.
Q2. Write a query to retrieve the names of students who live in Delhi.
Q3. The school wants to find students who are exactly 17 years old. Write a query that displays
their names and ages.
*/

-- Q1
SELECT * FROM students WHERE marks > 80;

-- Q2
SELECT name FROM students WHERE city = 'Delhi';

-- Q3
SELECT name, age FROM students WHERE age = 17;