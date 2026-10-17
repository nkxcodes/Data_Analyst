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
Q1. What does the SQL UPDATE statement do? Explain the difference between updating an
existing record and inserting a new record.
Q2. A student named Aman has an incorrect marks value. His id is 101, and his correct marks
are 85. Write a query to update his marks in the students table.
Q3. A student named Riya has moved from Mumbai to Delhi. Her student ID is 102. Write a
query to update only her city without changing any other information.
*/

-- Q1
/*
-- UPDATE modifies existing records.
-- INSERT INTO adds new records to a table.
*/

-- Q2
UPDATE students
SET marks = 85
WHERE id = 101;

-- Q3
UPDATE students
SET city = 'Delhi'
WHERE student_ID = 102;