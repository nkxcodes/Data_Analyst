
/*
Questions 1–3: Absolute basics
Q1. Basic CASE in SELECT
You have a table students:
id name marks
1 Aman 85
2 Riya 42
3 Rahul 67
4 Neha 30
Write a query to display each student's name and marks, along with a new column called
result.
●​ If marks are 40 or above, display Pass.
●​ Otherwise, display Fail.
Q2. Understanding ELSE
Using the same students table, write a query that classifies students:
●​ Marks 80 or above → Excellent
●​ Marks 60 or above → Good
●​ Marks 40 or above → Average
●​ All remaining cases → Needs Improvement
Q3.
Consider this query:
SELECT
name,
marks,
CASE
WHEN marks >= 50 THEN 'Good'
WHEN marks >= 80 THEN 'Excellent'
ELSE 'Needs Improvement'
END AS performance
FROM students;
Answer:
1.​ What performance category will a student with 85 marks receive?
2.​ Why doesn't that student receive Excellent?
3.​ What does this tell you about the order of WHEN conditions?
*/

-- Q1
SELECT name, marks,
CASE
    WHEN marks >= 40 THEN 'Pass'
    ELSE 'Fail'
END result
FROM students;