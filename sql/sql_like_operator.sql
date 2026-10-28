
/*
Questions 1–3: Absolute basics
Q1. Understanding LIKE
You have a table students:
id name
1 Aman
2 Ananya
3 Rahul
4 Amit
Write a query to find students whose names start with A.
Q2. Understanding % at the end
Using the same students table, write a query to find names that start with Am and can have
any number of characters after Am.
Q3. Understanding % at the beginning
Write a query to find students whose names end with a, regardless of what characters appear
before a.
*/

-- Q1
SELECT *
FROM students
WHERE name LIKE 'A%';

-- Q2
SELECT *
FROM students
WHERE name LIKE 'Am%';

-- Q3
SELECT *
FROM students
WHERE name LIKE '%a';