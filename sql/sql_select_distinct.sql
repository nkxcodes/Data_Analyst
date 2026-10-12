CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50),
    gender VARCHAR(10),
    marks INT
);

INSERT INTO students (id, name, age, city, gender, marks)
VALUES
(1, 'Rahul', 17, 'Delhi', 'Male', 85),
(2, 'Priya', 16, 'Mumbai', 'Female', 92),
(3, 'Aman', 17, 'Delhi', 'Male', 76),
(4, 'Sneha', 18, 'Jaipur', 'Female', 88),
(5, 'Rohit', 16, 'Pune', 'Male', 65),
(6, 'Anjali', 17, 'Mumbai', 'Female', 95),
(7, 'Vikas', 18, 'Delhi', 'Male', 72),
(8, 'Neha', 16, 'Jaipur', 'Female', 81),
(9, 'Arjun', 17, 'Pune', 'Male', 90),
(10, 'Kavya', 18, 'Delhi', 'Female', 78);

/*
Questions 1–3: Absolute basics
Difficulty: Easy

Q1. The students table contains many students from the same cities. Write a SQL query to
display each city only once.

Q2. Write a SQL query to display all the different ages present in the students table, without
repeating any age.

Q3. Suppose the gender column contains the values Male, Female, Male, Female, Male.
What would a query that selects distinct gender values return? Write the query and predict the
result.
*/

-- Q1
SELECT DISTINCT city FROM students;

-- Q2
SELECT DISTINCT age FROM students;

-- Q3
SELECT DISTINCT gender FROM students;

/*
Questions 4–6: Core concepts
Difficulty: Medium
Q4. Write a query to display all the unique marks obtained by students. If multiple students have
the same marks, each marks value should appear only once.
Q5. The school wants to know which different combinations of city and gender exist in its
student records. Write a query that displays these combinations without repeating identical
pairs.
Q6. A beginner thinks that selecting distinct city and gender means both columns will
independently contain unique values. Is this understanding correct? Explain what SQL
considers a duplicate when DISTINCT is applied to both columns together.
*/

-- Q4
SELECT DISTINCT marks FROM students;

-- Q5
SELECT DISTINCT city, gender FROM students;

-- Q6
/*
When DISTINCT is applied to multiple columns, SQL
considers the entire combination of those columns
when identifying duplicates.
*/

/*
Questions 7–9: Practical application
Difficulty: Application

Q7. A school administrator wants to know which different cities have students aged 17. Display
each qualifying city only once.

Q8. A teacher wants to see the different marks obtained by students who live in Delhi. The
same marks should not appear repeatedly in the result.

Q9. A school wants to identify all the different combinations of age and city among students
who scored more than 80 marks. Construct a query that returns only unique combinations for
qualifying students.
*/

-- Q7
SELECT DISTINCT city FROM students WHERE age = 17;

-- Q8
SELECT DISTINCT marks FROM students WHERE city = 'Delhi';

-- Q9
SELECT DISTINCT age, city FROM students WHERE marks > 80;

/*
Questions 10–12: Deeper understanding
Difficulty: Tricky
Q10. Predict the result.
Consider the following records:
city
Delhi
Mumbai
Delhi
Jaipur
Mumbai
What values would be returned by a query selecting distinct cities? Would the number of
returned rows necessarily equal the number of rows in the original table? Explain.
Q11. Find the mistake.
A beginner wants to display every unique city but writes:
SELECT city DISTINCT
FROM students;
Identify the syntax mistake and rewrite the query correctly.
Q12. Understand the difference.
Consider these two queries:
SELECT DISTINCT city
FROM students;
SELECT DISTINCT city, age
FROM students;
Can the second query return more rows than the first? Explain why, even though both queries
use DISTINCT.
*/

-- Q10
/*
Delhi
Mumbai
Jaipur
*/

-- Q11
SELECT DISTINCT city FROM students;

-- Q12
-- Query seconds retuns more rows than the first because, it returns are unique combinations.

/*
Questions 13–14: Mixed problems
Difficulty: Mixed
Q13. A Python variable stores a city name:
selected_city = "Delhi"
Write a SQL query to retrieve the different marks obtained by students from the city stored in
selected_city.
Assume you are writing a normal SQL query and must use the literal city value in the query,
rather than automatically substituting the Python variable.
Q14. A school wants to know which different cities have students who are either younger than
16 or have scored more than 90 marks. Display each qualifying city only once.
Construct a query that correctly combines both conditions without accidentally excluding
qualifying students.
*/

-- Q13
SELECT DISTINCT marks FROM students WHERE city = 'Delhi';

-- Q14
SELECT DISTINCT city FROM students WHERE age < 16 OR marks > 90;

/*
Question 15: Mastery challenge
Difficulty: Challenge
Q15. Student Data Analysis
A school administrator wants to analyze the student database and generate a report containing
the unique combinations of student age and city for students who meet these requirements:
●​ They scored at least 75 marks.
●​ They live in Delhi or Mumbai.
●​ Each identical age-and-city combination should appear only once.
Write a single SQL query that produces this report.
*/

SELECT DISTINCT age, city FROM students WHERE (city = 'Delhi' OR city = 'Mumbai') AND marks >= 75;