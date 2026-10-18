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
Q1. Understanding MAX()
Your students table contains students with different marks.
Write an SQL query to find the highest marks in the table.
Q2. Using MAX() with a specific column
Write a query to find the highest age among all students in the students table.
Q3. Understanding GROUP BY
The students table contains students from different cities.
Write a query that displays each city only once, along with the number of students belonging to
that city.
*/

-- Q1
SELECT MAX(marks) FROM students;

-- Q2
SELECT MAX(age) FROM students;

-- Q3
SELECT city, count(*) FROM students GROUP BY city;