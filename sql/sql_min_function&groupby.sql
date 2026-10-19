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
Q1. Understanding MIN()
Write an SQL query to find the lowest marks obtained by any student in the students table.
Q2. Finding the minimum age
Write a query to find the lowest age among all students in the table.
Q3. Understanding GROUP BY
The students table contains students from different cities.
Write a query that displays each city and the lowest marks obtained by a student in that city.
*/

-- Q1
SELECT MIN(marks) FROM students;

-- Q2
SELECT MIN(age) FROM students;

-- Q3
SELECT city, MIN(marks) FROM students GROUP BY city;