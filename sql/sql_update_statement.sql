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
WHERE student_id = 102;

/*
Questions 4–6: Core concepts
Difficulty: Medium
Q4. The school has discovered that a student with ID 103 has an incorrect age and city. The
correct age is 18, and the correct city is Jaipur. Update both columns in a single SQL
statement.
Q5. The school wants to increase the marks of every student by 5. Write a query that performs
this change directly using the existing marks values.
Q6. The school wants to correct the city of every student named Aman to Delhi. Write a query
that updates all matching records, even if multiple students have that name.
*/

-- Q4
UPDATE students
SET age = 18,
    city = 'Jaipur'
WHERE student_id = 103;

-- Q5
UPDATE students
SET marks = marks + 5;

-- Q6
UPDATE students
SET city = 'Delhi'
WHERE name = 'Aman';

/*
Questions 7–9: Practical application
Difficulty: Application
Q7. A teacher decides that students whose marks are below 40 should receive a revised marks
value of 40 after a correction process. Update the records according to this rule.
Q8. A school administrator discovers that all students currently listed as living in Bombay should
have their city recorded as Mumbai. Update the relevant records.
Q9. A school is offering a 10-mark bonus to students who scored at least 80 marks and live in
Delhi. Update the marks of only those students.
*/

-- Q7
UPDATE students
SET marks = 40
WHERE marks < 40;

-- Q8
UPDATE students
SET city = 'Mumbai'
WHERE city = 'Bombay';

-- Q9
UPDATE students
SET marks = marks + 10
WHERE marks >= 80 AND city = 'Delhi';