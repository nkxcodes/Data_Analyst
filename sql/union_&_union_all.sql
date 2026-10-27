
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