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
Difficulty: Easy
Q1. Write a SQL query to display all students, arranging their records by name in ascending
alphabetical order.
Q2. Write a query to display students' names and marks, starting with the students who scored
the highest marks and ending with those who scored the lowest.
Q3. Consider the following marks:
namemarks
Aman75
Riya92
Karan60
Neha84
If you sort the records by marks in ascending order, what will the resulting order of names be?
Explain the difference between ascending and descending order.
*/

-- Q1
SELECT *
FROM students
ORDER BY name ASC;

-- Q2
SELECT name, marks 
FROM students
ORDER BY marks DESC;

-- Q3
/*
Karan
Aman
Neha
Riya

Ascending - Smallest to Largest
Descending - Largest to Smallest
*/

/*
Questions 4–6: Core concepts
Difficulty: Medium
Q4. The school wants to arrange students from youngest to oldest. Write a query that displays
their names and ages in the correct order.
Q5. The administrator wants to sort students by city alphabetically and, within each city,
arrange students from highest marks to lowest. Write the query.
Q6. A teacher wants to sort students by marks in descending order and then by name in
ascending order. Write a query that applies both sorting rules.
*/

-- Q4
SELECT name, age
FROM students
ORDER BY age asc;

-- Q5
SELECT name, city, marks
FROM students
ORDER BY city asc, marks desc;

-- Q6
SELECT name, marks 
FROM students
ORDER BY marks desc, name asc;

/*
Questions 10–12: Deeper understanding
Difficulty: Tricky
Q10. the result.
Consider these records:
name
marks
Aman80
Riya95
Karan80
Neha70
A query sorts the table by marks in descending order.
●​ Which student or students will appear first?
●​ Where will the two students with 80 marks appear relative to the student with 95 marks?
●​ Can you guarantee the order of Aman and Karan without specifying another sorting
column? Explain.
Q11. Find the mistake.
A beginner wants to display students from highest marks to lowest but writes:
SELECT name, marks
FROM students
ORDER BY marks;
The beginner believes this automatically sorts from highest to lowest.
Explain the misunderstanding and rewrite the query so it follows the requirement.
Q12. Understand multiple-column sorting.
Consider this query:
SELECT name, city, marks
FROM students
ORDER BY city ASC, marks DESC;
Explain how MySQL decides the order of the records.
What happens when two students have the same city but different marks? What happens when
both their city and marks are the same?
*/

-- Q11
/*
1. Riya
2. Both Aman and Karan will appear after Riya.
3. No.
*/

-- Q12
/*
MySQL sorts records according to the columns listen in the
ORDER BY clause, from left to right.

First, city ASC arranges cities alphabetically. Within
the same city, marks DESC arranges students from highest
marks to lowest.

If two students have the same city but different marks,
the student with higher marks appears first.

If both their city and marks are the same, their relative
order is not guaranteed because no additional sorting rule
has been specified. We can use name ASC as a third sorting
column to arrange them alphabetically.
*/

/*
Questions 13–14: Mixed problems
Difficulty: Mixed
Q13. A Python variable stores a minimum marks threshold:
minimum_marks = 70
Write a SQL query that displays the names and marks of students who scored at least that
threshold, arranging the highest-scoring students first.
Assume you're writing a normal SQL query, so use the threshold value directly rather than
automatically substituting the Python variable.
Q14. A school administrator wants a report of students who are at least 16 years old and live in
Delhi or Mumbai.
The report must display their name, age, city, and marks. Arrange the results by city
alphabetically, then by marks from highest to lowest, and then by name alphabetically.
Write the query that satisfies all these requirements.
*/

-- Q13
SELECT name, marks
FROM students
WHERE marks >= 70
ORDER BY marks DESC;

-- Q14
SELECT name, age, city, marks
FROM students
WHERE age >= 16
AND IN ('Delhi', 'Mumbai')
ORDER BY city ASC, marks DESC, name ASC;