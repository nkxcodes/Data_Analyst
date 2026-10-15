USE students;

CREATE TABLE students(
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    marks INT,
    city VARCHAR(50)
)

/*
Questions 1–3: Absolute basics
Difficulty: Easy
Q1. What does the SQL INSERT INTO statement do? Explain the difference between inserting
a new row and retrieving an existing row.
Q2. Write a SQL query to insert a student with these details into the students table:
Name: Aman
Age: 17
City: Delhi
Gender: Male
Marks: 85
Q3. You want to insert a student named Riya, aged 16, who lives in Mumbai and has scored 92
marks. The gender column is optional for this exercise. Write a query that inserts the provided
information without specifying the id column.
*/

-- Q1
/*
The SQL INSERT INTO statement is used to add new records
(rows) to a database table.

Inserting a new row adds new data to the table, whereas retrieving
an existing row means fetching stored data using the
SELECT statement. INSERT INTO changes the table's data by
adding a record, while SELECT only retrieves data without
modifying it.
*/

-- Q2
INSERT INTO students (name, age, city, gender, marks)
VALUES ('Aman', 17, 'Delhi', 'Male', 85)

-- Q3
INSERT INTO students (name, age, city, marks)
VALUES ('Riya', 16, 'Mumbai', 92)