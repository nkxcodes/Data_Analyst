
/*
Questions 1–3: Absolute basics
Q1. Understanding UNION
You have two tables:
class_a
name
Aman
Riya
class_b
name
Mohan
Riya
Write a query that combines the names from both tables using UNION.
Q2. Understanding UNION ALL
Using the same class_a and class_b tables from Q1, write a query that combines the names
from both tables while retaining duplicate rows.
Q3. the result
Using the tables from Q1, answer these questions:
●​ How many rows will UNION return?
●​ How many rows will UNION ALL return?
●​ Why does Riya appear a different number of times in the two results?
*/

-- Q1
SELECT * FROM class_a
UNION
SELECT * FROM class_b;

-- Q2
SELECT * FROM class_a
UNION ALL
SELECT * FROM class_b;

-- Q3
/*
-- UNION returns 3 rows because it removes duplicate rows.
-- UNION ALL returns 4 rows because it keeps all rows.
-- Riya appears once with UNION and twice with UNION ALL.
*/

/*
Questions 4–6: Core concepts
Q4. Combining multiple columns
You have two tables:
current_students(student_id, name, city)
former_students(student_id, name, city)
Write a query that combines the records from both tables using UNION, returning all three
columns.
Q5. Understanding column requirements
Suppose table_a contains two columns, id and name, while table_b contains three
columns, id, name, and city.
Can you combine these queries directly using UNION? Explain why or why not.
Q6. Sorting combined results
You have two tables, north_customers(customer_name) and
south_customers(customer_name).
Write a query that combines customer names from both tables, removes duplicate names, and
sorts the final result alphabetically.
*/

-- Q4
SELECT * FROM current_students
UNION
SELECT * FROM former_students;

-- Q5
/*
-- No, UNION requires both SELECT queries to return
-- the same number of columns.
-- Here, one returns 2 columns and the other returns 3,
-- so the query produces an error.
*/

-- Q6
SELECT customer_name FROM north_customers
UNION
SELECT customer_name FROM south_customers
ORDER BY customer_name ASC;