
/*
Questions 1–3: Absolute basics
Q1. Understanding LEFT JOIN
You have two tables:
students
id name
1 Aman
2 Riya
3 Mohan
student_marks
student_id marks
1 85
2 92
Write a query to display every student's name and their marks, including students who do not
have a matching record in student_marks.
Q2. Understanding unmatched records
Consider these tables:
employees
id named department_id
1 Aman 10
2 Riya 20
3 Karan 30
departments
department_id department_name
10 IT
20 HR
Write a query that displays every employee's name and their department name, including
employees whose department has no matching record.
Q3. Using the tables from Q1, what rows will appear when you join students with
student_marks using a LEFT JOIN?
Write the expected output, including any NULL values.
*/

-- Q1
SELECT students.name, student_marks.marks
FROM students
LEFT JOIN student_marks
ON students.id = student_marks.student_id;

-- Q2
SELECT e.name, d.department_name
FROM employees AS e
LEFT JOIN departments AS d
ON e.department_id = d.department_id;

-- Q3
/*
Aman 85
Riya 92
Mohan NULL
*/