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