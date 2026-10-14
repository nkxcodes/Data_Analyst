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
Q1. Write a SQL query to display all students, arranging their records by name in ascending
alphabetical order.
Q2. Write a query to display students' names and marks, starting with the students who scored
the highest marks and ending with those who scored the lowest.
Q3. Consider the following marks:
namemarks
Aman75
Riya92
Karan60
Neha84
If you sort the records by marks in ascending order, what will the resulting order of names be?
Explain the difference between ascending and descending order.
*/

-- Q1
SELECT *
FROM students
ORDER BY name ASC;

-- Q2
SELECT name, marks 
FROM students
ORDER BY marks DESC;

-- Q3
/*
Karan
Aman
Neha
Riya

Ascending - Smallest to Largest
Descending - Largest to Smallest
*/