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
Q1. Understanding SUM()
Using the students table, write a query to calculate the total marks of all students.
Q2. Understanding AVG()
Write a query to calculate the average marks of all students in the table.
Q3. Understanding COUNT()
Write a query to count the total number of students in the students table.
*/

-- Q1
SELECT SUM(marks) FROM students;

-- Q2
SELECT AVG(marks) FROM students;

-- Q3
SELECT COUNT(*) FROM students;