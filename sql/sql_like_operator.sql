
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

/*
Questions 7–9: Practical application
Q7. Searching email addresses
A table customers contains:
customer_id, name, email
Write a query to find customers whose email addresses end with @gmail.com.
Q8. Finding products by name
A table products contains:
product_id, product_name, price
A manager wants to find products whose names contain the word phone anywhere in the
name, such as Smartphone, Phone Case, or Headphones.
Write the query.
Q9. Filtering employee records
A table employees contains:
employee_id, name, department, email
The HR team wants employees whose names start with R but whose email addresses do not
end with @company.com.
Write a query that satisfies both conditions.
*/

-- Q7
SELECT *
FROM customers
WHERE email LIKE '%@gmail.com';

-- Q8
SELECT *
FROM products
WHERE product_name LIKE '%phone%';

-- Q9
SELECT *
FROM employees
WHERE name LIKE 'R%'
AND email NOT LIKE '%@company.com';

/*
Questions 10–12: Deeper understanding
Q10. Find the mistake
A beginner wants to find all students whose names start with A. They write:
SELECT * FROM students
WHERE name = 'A%';
Explain what is wrong with this query and rewrite it correctly.
Q11. Understanding _ versus %
Suppose a table codes contains these values:
code
AB1
AB12
A12
ABC
AB
For each pattern below, identify which values match and explain why.
●​ LIKE 'AB_'
●​ LIKE 'AB%'
●​ LIKE '_B%'
Q12. Case sensitivity and NULL values
A table users contains:
username
Aman
aman
Riya
NULL
Answer the following:
1.​ Will username LIKE 'A%' necessarily treat Aman and aman differently in MySQL?
2.​ What determines whether a LIKE comparison is case-sensitive?
3.​ Does the row containing NULL match username LIKE 'A%'? Why?
*/

-- Q10
/*
The = operator checks for an exact match and does not
treat % as a wildcard.

Correct query:
*/
SELECT *
FROM students
WHERE name LIKE 'A%';

-- Q11
/*
1. 'AB_'
    Matches AB1 and ABC because _ requires exactly one
    character after AB.

2. 'AB%'
    Matches AB1, AB12, ABC, and AB because % allows zero
    or more characters after AB.

3. '_B%'
    Matches AB1, AB12, ABC, and AB because _ matches 
    exactly one first character, B must be second, and 
    % matches zero or more characters after B.
*/

-- Q12
/*
1. LIKE may or may not distinguish Aman and aman. 
    It depends on the column's collation.

2. Collation determines whether text comparisons are 
    case-sensitive or case-insensitive.

3. NULL LIKE 'A%' returns UNKNOWN because NULL represents 
    an unknown value. WHERE only keeps TRUE conditions.
*/

/*
Questions 13–14: Mixed problems
Q13. Combining LIKE, AND, and OR
A table products contains:
product_id, product_name, category, price
Write a query to find products that either:
●​ Have names starting with Sam and cost less than ₹1,000, or
●​ Belong to the Accessories category and have names ending with Case.
Make sure your conditions are grouped correctly.
Q14. Pattern matching with multiple conditions
A table students contains:
id, name, city, marks
Write a query to find students who:
●​ Have names containing an anywhere,
●​ Live in either Delhi or Mumbai,
●​ Have marks of at least 60.
Return only name, city, and marks, sorted by marks from highest to lowest.
*/

-- Q13
SELECT *
FROM products
WHERE (product_name LIKE 'Sam%' AND price < 1000)
    OR (category = 'Accessories' AND product_name LIKE '%Case')

-- Q14
SELECT name, city, marks
FROM students
WHERE name LIKE '%an%'
    AND (city = 'Delhi' OR city = 'Mumbai')
    AND marks >= 60
ORDER BY marks DESC;

/*
Q15. Mastery challenge — Customer search report
A company stores customer information in a table named customers:
●​ customer_id
●​ customer_name
●​ email
●​ city
●​ total_spent
The sales manager needs a report of customers whose names begin with S or whose email
addresses contain shop. Include only customers who live in Delhi or Mumbai and have spent
more than ₹5,000.
Display the customer ID, name, email, city, and total spent. Sort the results by total spent from
highest to lowest.
Write the complete query. Pay attention to how you combine the conditions so that the results
follow all the manager's requirements.
*/

-- Q15
SELECT customer_id, customer_name, email, city, total_spent
FROM customers
WHERE (customer_name LIKE 'S%' OR email LIKE '%shop%')
    AND (city = 'Delhi' OR city = 'Mumbai')
    AND total_spent > 5000
ORDER BY total_spent DESC;