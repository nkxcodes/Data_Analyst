
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

/*
Questions 4–6: Core concepts
Q4. Understanding _
You have a table products:
product_id product_name
1 Pen
2 Book
3 Cup
4 Bag
5 Lamp
Write a query to find product names containing exactly three characters.
Q5. Combining wildcard patterns
Using the students table from Q1, write a query to find names that start with A and end with n,
with any number of characters in between.
Q6. the result
Consider this query:
SELECT name
FROM students
WHERE name LIKE 'A%';
Which names will match? Explain why the query can match both a one-character name A and
longer names starting with A.
*/

-- Q4
SELECT product_name
FROM products
WHERE product_name LIKE '___';

-- Q5
SELECT name
FROM students
WHERE name LIKE 'A%n';

-- Q6
/*
Aman
Ananya
Amit

-- '%' matches zero or more characters, so both 'A' and
    longer names match.
*/