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
SELECT city, COUNT(*) FROM students GROUP BY city;

/*
Questions 4–6: Core concepts
Q4. Finding the maximum value in each group
Find the highest marks obtained in each city. Display the city and its highest marks.
Q5. Combining aggregate functions
For each city, display:
●​ The city name.
●​ The total number of students.
●​ The highest marks.
Q6. Grouping by multiple columns
Your table contains city and gender columns.
Find the highest marks for each combination of city and gender. For example, Delhi–Male and
Delhi–Female should appear as separate groups.
*/

-- Q4
SELECT city, MAX(marks) FROM students GROUP BY city;

-- Q5
SELECT city, COUNT(*), MAX(marks) FROM students GROUP BY city;

-- Q6
SELECT city, gender, MAX(marks) FROM students GROUP BY city, gender;

/*
Questions 7–9: Practical application
Q7. School performance analysis
A school wants to know the highest marks obtained by students in each gender category.
Write a query that provides this information.
Q8. Finding the highest salary by department
Imagine you have an employees table with these columns:
id, name, department, salary
Write a query to find the highest salary in each department.
Q9. Identifying groups with a minimum performance level
A school wants to see only those cities where the highest student marks are greater than 80.
Display the city and its highest marks. Only qualifying cities should appear in the result.
*/

-- Q7
SELECT gender, MAX(marks) FROM students GROUP BY gender;

-- Q8
SELECT department, MAX(salary) FROM employees GROUP BY department;

-- Q9
SELECT city, MAX(marks) FROM students GROUP BY city HAVING MAX(marks) > 80;

/*
Questions 10–12: Deeper understanding
Q10. the result
Suppose the students table contains these records:
name city
Aman Delhi
marks 75
Riya Delhi 92
Mohan Mumbai 81
Priya Mumbai 88
What result will this query produce?
SELECT city, MAX(marks)
FROM students
GROUP BY city;
Write the expected output and explain why there are two rows.
Q11. Find the mistake
A beginner wants to display each city and its highest marks. They write:
SELECT city, name, MAX(marks)
FROM students
GROUP BY city;
Identify the problem with this query in MySQL when ONLY_FULL_GROUP_BY is enabled. Explain
what makes name different from city and MAX(marks) in this query.
Q12. Understand the difference
Consider these two queries:
SELECT MAX(marks)
FROM students;
SELECT city, MAX(marks)
FROM students
GROUP BY city;
Explain how their results differ. Also, what happens if a city has several students with the same
highest marks? Does MAX() automatically display every student's name who achieved that
score?
*/

-- Q10
/*
Delhi 92
Mumbai 88
*/

-- Q11
/*
-- name causes an error because each city has multiple students.
-- Use GROUP BY columns or aggregate functions in SELECT.

Correct query:
*/

SELECT city, MAX(marks) FROM students GROUP BY city;

-- Q12
/*
The first query returns the highest marks in the entire 
table. The second query returns the highest marks
separately for each city using GROUP BY.
MAX() returns only the maximum value, no the students'
names . If multiple students achieve that score, their
names are not automatically displayed. We need an 
additionalquery to retrieve them.
*/

/*
Questions 13–14: Mixed problems
Q13. Combining variables and conditions
You are analyzing student performance and have decided that a city should be considered only
if its highest marks exceed a variable threshold of 85.
Write the SQL query that displays the qualifying cities and their highest marks. In your written
answer, represent the threshold as the number 85 in SQL.
Q14. Combining WHERE, GROUP BY, and MAX()
The school wants to analyze students who scored at least 40 marks, then find the highest marks
in each city among those students.
Write a query that displays each qualifying city and its highest marks, considering only students
with marks greater than or equal to 40.
*/

-- Q13
SELECT city, MAX(marks) FROM students GROUP BY city HAVING MAX(marks) > 85;

-- Q14
SELECT city, MAX(marks) FROM students WHERE marks >= 40 GROUP BY city;

/*
Question 15: Mastery challenge
Q15. Student Performance Report
The school principal wants a report showing the highest-performing student marks for each city,
but only students who passed (marks of 40 or above) should be considered. The report should
include only cities whose highest qualifying marks are at least 75, and the results should be
arranged from the highest city-level score to the lowest.
Write a single SQL query that produces this report.
*/

-- Q15
SELECT city, MAX(marks)
FROM students
WHERE marks >= 40
GROUP BY city
HAVING MAX(marks) >= 75
ORDER BY MAX(marks) DESC;