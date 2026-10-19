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
Q1. Understanding SUM()
Using the students table, write a query to calculate the total marks of all students.
Q2. Understanding AVG()
Write a query to calculate the average marks of all students in the table.
Q3. Understanding COUNT()
Write a query to count the total number of students in the students table.
*/

-- Q1
SELECT SUM(marks) FROM students;

-- Q2
SELECT AVG(marks) FROM students;

-- Q3
SELECT COUNT(*) FROM students;

/*
Questions 4–6: Core concepts
Q4. Combining SUM() and AVG()
Write a query that displays both the total marks and average marks of all students in one result.
Q5. Counting students in each city
Write a query to display each city and the number of students belonging to that city.
Q6. Calculating grouped totals and averages
For each city, display:
The city name.
The total marks of its students.
The average marks of its students.
The number of students in that city.
*/

-- Q4
SELECT SUM(marks), AVG(marks) FROM students;

-- Q5
SELECT city, COUNT(*) FROM students GROUP BY city;

-- Q6
SELECT city, SUM(marks), AVG(marks), COUNT(*) FROM students GROUP BY city;

/*
Questions 7–9: Practical application
Q7. Analyzing student performance by gender
The school wants to compare academic performance across gender categories.
Write a query that displays each gender, its average marks, and the total number of students in
that category.
Q8. Monthly sales report
Imagine you have a sales table with these columns:
sale_id, product_name, category, quantity, unit_price
The manager wants to know how many units were sold in each product category. Write a query
to generate this report.
Q9. Finding high-performing cities
The principal wants to see only cities where the average student marks are at least 75.
Display each qualifying city and its average marks.
*/

-- Q7
SELECT gender, AVG(marks), COUNT(*) FROM students GROUP BY gender;

-- Q8
SELECT category, SUM(quantity) FROM sales GROUP BY category;

-- Q9
SELECT city, AVG(marks) FROM students GROUP BY city HAVING AVG(marks) >= 75;

/*
Questions 10–12: Deeper understanding
the result
Suppose the students table contains these records:
name city marks
Aman Delhi 60
Riya Delhi 80
Mohan Mumbai 70
Priya Mumbai 90
What result will this query produce?
SELECT city, SUM(marks), AVG(marks), COUNT(*)
FROM students
GROUP BY city;
Write the expected output and explain what each aggregate function calculates for each city.
Q11. Find the mistake
A beginner wants to find the average marks in each city but writes:
SELECT city, AVG(marks)
FROM students
WHERE AVG(marks) > 70
GROUP BY city;
Identify the error and explain why the condition cannot be placed in WHERE in this query.
Q12. Understand COUNT() and NULL
Suppose a table named students contains these records:
id name marks
1 Aman 60
2 Riya NULL
3 Mohan 80
4 Priya NULL
Answer these questions:
●​ What does COUNT(*) return?
●​ What does COUNT(marks) return?
●​ How do SUM(marks) and AVG(marks) treat the NULL values?
●​ Why can COUNT(*) and COUNT(marks) return different results?
*/

-- Q10

/*
city SUM(marks) AVG(marks) COUNT(*)
Delhi 140 70 2
Mumbai 160 80 2

GROUP BY city separate group for each city.
SUM(marks) calculates the total marks per city.
AVG(marks) calculates the average marks per city.
COUNT(*) counts the students in each city.
*/

-- Q11

/*
-- WHERE filters rows before grouping.
-- HAVING filters groups after aggregation.
-- Therefore, AVG(marks) > 70 belongs in HAVING.

Correct query:
*/

SELECT city, AVG(marks)
FROM students
GROUP BY city
HAVING AVG(marks) > 70;

-- Q12

/*
COUNT(*) counts all rows.
COUNT(marks) ignores NULL marks.
SUM() and AVG() ignore NULL values.
Therefore, COUNT(*) and COUNT(marks) can differ.
*/

/*
Questions 13–14: Mixed problems
Q13. Combining filtering and aggregation
A school wants to analyze only students who scored at least 40 marks.
Write a query that groups these students by city and displays each city's student count and
average marks.
Q14. Combining multiple conditions
A school wants a report for students aged 18 or older. For each city, calculate the total marks
and average marks of these students. Display only cities whose total marks exceed 200, and
sort the results by average marks from highest to lowest.
Write the complete SQL query.
*/

-- Q13
SELECT city, COUNT(*), AVG(marks) FROM students WHERE marks >= 40 GROUP BY city;

-- Q14
SELECT city, SUM(marks), AVG(marks) 
FROM students 
WHERE age >= 18 
GROUP BY city 
HAVING SUM(marks) > 200 
ORDER BY AVG(marks) DESC;