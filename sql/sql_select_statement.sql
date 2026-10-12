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
Q1. Write a SQL query to retrieve all columns and all rows from the students table.
*/

SELECT * FROM students;

-- Q2. Write a SQL query to retrieve only the name column from the students table.

SELECT name FROM students;

/*Q3. You want to display students' names and marks together, without displaying their other
information. Write the SQL query.*/

SELECT name, marks FROM students;

/*
Questions 4–6: Core concepts
Difficulty: Medium
Q4. Write a query to display the name, age, and city columns in that exact order. Does the
order of columns in your SELECT statement matter?
*/

SELECT name, age, city FROM students;

/*
Q5. The school wants to display each student's name and marks, but the marks column should
appear under the heading score in the query result. Write the query without changing the
actual table structure.
*/

SELECT name, marks AS score FROM students;

/*
Q6. Write a query that displays only the different cities present in the students table, without
repeating a city that appears multiple times.
*/

SELECT DISTINCT city FROM students;

/*
Questions 7–9: Practical application
Difficulty: Application
Q7. A teacher wants to find students who scored more than 80 marks. Display only their names
and marks.
*/

SELECT name, marks FROM students WHERE marks > 80;

/*
Q8. A school administrator wants a list of students who are 17 years old and live in Delhi.
Display their names, ages, and cities.
*/

SELECT name, age, city FROM students WHERE age = 17 AND city = 'Delhi';

/*
Q9. A teacher wants to review students whose marks are between 60 and 90, including both 60
and 90. Display their names and marks.
*/

SELECT name, marks FROM students WHERE marks BETWEEN 60 AND 90;

/*
Questions 10–12: Deeper understanding
Difficulty: Tricky
Q10. Predict what each query will return. Explain the difference between the results.
SELECT * FROM students;
SELECT name FROM students;
*/
/*
1. Give all columns from the table students.
2. Give only the name column from the table students.
*/

/*
Q11. Find the mistake.
A beginner writes this query to retrieve the names and marks of students who scored above 80:
SELECT name, marks
FROM students
WHERE marks > 80
The beginner says the query is incorrect because it does not end with a semicolon. Is the
beginner necessarily correct? Explain when the semicolon matters.

Answer:-
Yes, the beginner is correct that query is incorrect,
a query in sql should must end with and semicolon(;)
*/

/*
Q12. Consider this query:
SELECT name, age
FROM students;
A beginner wants to display every column but writes:
SELECT name, age, *
FROM students;
Is this a good way to retrieve every column? Explain what is problematic about this approach
and how you would write the query correctly.

Answer:
It is not a good way of retrieving every column,
because it will give name, age and then every column,
so we will get name and age twice.

better:-
SELECT * FROM students;
*/

/*
Questions 13–14: Mixed problems
Difficulty: Mixed
Q13. You are given a Python variable:
minimum_marks = 75
Write a SQL query that displays the names and marks of students whose marks are greater
than the value stored in minimum_marks.
Assume you are writing an ordinary SQL query, not Python code that automatically substitutes
the variable.
*/

SELECT name, marks FROM students WHERE marks > 75;