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