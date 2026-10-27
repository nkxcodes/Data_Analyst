
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

/*
Questions 7–9: Practical application
Q7. Combining contact listsA company maintains two tables:
●​ office_contacts(contact_name, phone)
●​ event_contacts(contact_name, phone)
Some people appear in both tables.
The company wants one combined contact list without duplicate rows. Write the query.
Q8. Combining transaction records
A business stores transactions in two tables:
●​ online_sales(sale_id, amount)
●​ store_sales(sale_id, amount)
The finance team wants to combine every transaction record from both sources, preserving
repeated rows if they occur.
Write the query that best fits this requirement.
Q9. Creating a unified student list
A school stores students from two campuses in campus_a_students and
campus_b_students. Both tables contain student_id and name.
The school wants one list of unique student IDs and names. Choose the appropriate set
operator and write the query.
*/

-- Q7
SELECT contact_name, phone FROM office_contacts
UNION
SELECT contact_name, phone FROM event_contacts;

-- Q8
SELECT sale_id, amount FROM online_sales
UNION ALL
SELECT sale_id, amount FROM store_sales;

-- Q9
SELECT student_id, name FROM campus_a_students
UNION
SELECT student_id, name FROM campus_b_students;

/*
Questions 13–14: Mixed problems
Q13. Combining data with conditions
You have two tables:
●​ employees_2025(id, name, salary)
●​ employees_2026(id, name, salary)
Write a query that combines employees earning more than 50,000 from both tables, removes
duplicate result rows, and sorts the combined result by salary from highest to lowest.
Q14. Combining different categories
A school has two tables:
●​ students(student_id, name)
●​ teachers(teacher_id, name)
The principal wants a single list containing the names of all students and teachers, along with a
label identifying each person as either a student or a teacher.
Write a query that combines both groups into one result with columns for name and role.
*/

-- Q13
SELECT id, name, salary FROM employees_2025
WHERE salary > 50000
UNION
SELECT id, name, salary FROM employees_2026
WHERE salary > 50000
ORDER BY salary DESC;

-- Q14
SELECT name, 'Student' AS role FROM students
UNION ALL
SELECT name, 'Teacher' AS role FROM teachers;