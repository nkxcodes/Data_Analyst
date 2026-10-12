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