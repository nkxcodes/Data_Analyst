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
Q1. Understanding MIN()
Write an SQL query to find the lowest marks obtained by any student in the students table.
Q2. Finding the minimum age
Write a query to find the lowest age among all students in the table.
Q3. Understanding GROUP BY
The students table contains students from different cities.
Write a query that displays each city and the lowest marks obtained by a student in that city.
*/

-- Q1
SELECT MIN(marks) FROM students;

-- Q2
SELECT MIN(age) FROM students;

-- Q3
SELECT city, MIN(marks) FROM students GROUP BY city;

/*
Questions 4–6: Core concepts
Q4. Combining aggregate functions
For each city, display:
●​ The city name.
●​ The lowest marks.
●​ The highest marks.
Q5. Grouping by multiple columns
Using the city and gender columns, find the lowest marks for each city–gender combination.
Q6. Counting students alongside minimum marks
For each city, display the city name, the total number of students, and the lowest marks in that
city.
*/

-- Q4
SELECT city, MIN(marks), MAX(marks) FROM students GROUP BY city;

-- Q5
SELECT city, gender, MIN(marks) FROM students GROUP BY city, gender;

-- Q6
SELECT city, COUNT(*), MIN(marks) FROM students GROUP BY city;

/*
Questions 7–9: Practical application
Q7. School attendance analysis
Imagine you have an attendance table with these columns:
student_id, student_name, attendance_percentage
The school wants to identify the lowest attendance percentage among all students.
Write the query that produces this result.
Q8. Finding the cheapest product
Imagine you have a products table containing:
product_id, product_name, category, price
A shopkeeper wants to know the cheapest product price in each category. Write a query to
produce this report.
Q9. Analyzing passing students
The school wants to find the lowest passing marks in each city. A student passes with marks of
40 or above.
Write a query that considers only passing students and displays each city with its lowest
qualifying marks.
*/

-- Q7
SELECT MIN(attendance_percentage) FROM attendance;

-- Q8
SELECT category, MIN(price) FROM products GROUP BY category;

-- Q9
SELECT city, MIN(marks) FROM students WHERE marks >= 40 GROUP BY city;