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

/*
Questions 4–6: Core concepts
Difficulty: Medium
Q4. Retrieve the names and marks of students who scored at least 75 marks but fewer than 90
marks. Both conditions must be satisfied.
Q5. A school administrator wants to retrieve students who live in either Delhi or Mumbai. Write a
query that returns their names and cities.
Q6. Retrieve the names and marks of students whose marks are not equal to 50. Make sure
you use a valid SQL comparison operator.
*/

-- Q4
SELECT name, marks FROM students WHERE marks >= 75 AND marks < 90;

-- Q5
SELECT name, city FROM students WHERE city = 'Delhi' OR city = 'Mumbai';

-- Q6
SELECT name, marks FROM students WHERE marks != 50;

/*
Questions 7–9: Practical application
Difficulty: Application
Q7. A teacher wants to identify students who need academic support. The school's rule is that
students scoring below 40 marks require support. Display their names, cities, and marks.
Q8. A school wants to identify students whose names begin with the letter A, regardless of what
comes after that letter. Display their names.
Q9. The administrator wants to find students whose marks fall within the range of 60 to 85,
including both boundaries, and who live in Jaipur. Display their names, marks, and cities.
*/

-- Q7
SELECT name, city, marks FROM students WHERE marks < 40;

-- Q8
SELECT name FROM students WHERE name LIKE 'A%';

-- Q9
SELECT name, marks, city FROM students WHERE city = 'Jaipur' AND marks BETWEEN 60 AND 85;

/*
Questions 10–12: Deeper understanding
Difficulty: Tricky
Q10. Predict the result.
Consider these student records:
namecity
marks
AmanDelhi85
RiyaMumbai65
KaranDelhi45
NehaJaipur90
A query filters students using the condition city = 'Delhi' AND marks > 50.
Which students will appear in the result? Explain why the other students are excluded.
Q11. Find the mistake.
A beginner wants to retrieve students who live in Delhi or Mumbai and writes:
SELECT name, city
FROM students
WHERE city = 'Delhi' OR 'Mumbai';
Identify the problem with the condition and rewrite the query correctly.
Q12. Understand NULL.
The students table contains some records where marks is NULL, meaning the marks are
unknown or missing.
The administrator wants to find students whose marks have not been recorded.
●​ Write the appropriate filtering condition.
●​ Explain why checking whether marks equals NULL is not the correct approach.
●​ What is the difference between a missing value and a marks value of zero?
*/

-- Q10
/*
Only Aman will appear in the result because he
satisfies both conditions:
1. His city is Delhi.
2. His marks are greater than 50.

Riya and Neha are excluded because they don't
live in Delhi. Karan is excluded because his
marks are not greater than 50.
*/

-- Q11
SELECT name, city
FROM students
WHERE city = 'Delhi'
OR city = 'Mumbai';

-- Q12
SELECT *
FROM students
WHERE marks IS NULL;

/*
Questions 13–14: Mixed problems
Difficulty: Mixed
Q13. A Python variable stores the minimum required marks:
minimum_marks = 75
Write a SQL query to display the names and marks of students whose marks are greater than
the value stored in minimum_marks.
Assume you're writing a normal SQL query, not Python code that automatically substitutes the
variable.
Q14. A school administrator wants to find students who meet either of these requirements:
●​ They live in Delhi and have scored at least 80 marks.
●​ They live in Mumbai and have scored at least 90 marks.
Display their names, cities, and marks. Make sure each city has its own correct marks
requirement.
*/

-- Q13
SELECT name, marks
FROM students
WHERE marks > 75;

-- Q14
SELECT *
FROM students
WHERE (city = 'Delhi' AND marks >= 80)
OR (city = 'Mumbai' AND marks >= 90);

/*
Question 15: Mastery challenge
Difficulty: Challenge
Q15. Student Eligibility Report
A school needs a list of students who qualify for a special academic program.
The eligibility rules are:
●​ Students must be at least 16 years old.
●​ They must have scored at least 75 marks.
●​ They must live in Delhi, Mumbai, or Jaipur.
●​ Their marks must be recorded; students with missing marks cannot qualify.
●​ Display each qualifying student's id, name, age, city, and marks.
Write a single SQL query that generates the report.
*/

SELECT id, name, age, city, marks
FROM students
WHERE age >= 16
AND marks >= 75
AND city IN ('Delhi', 'Mumbai', 'Jaipur')
AND marks IS NOT NULL;