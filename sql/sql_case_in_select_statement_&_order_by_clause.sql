
/*
Questions 1–3: Absolute basics
Q1. Basic CASE in SELECT
You have a table students:
id name marks
1 Aman 85
2 Riya 42
3 Rahul 67
4 Neha 30
Write a query to display each student's name and marks, along with a new column called
result.
●​ If marks are 40 or above, display Pass.
●​ Otherwise, display Fail.
Q2. Understanding ELSE
Using the same students table, write a query that classifies students:
●​ Marks 80 or above → Excellent
●​ Marks 60 or above → Good
●​ Marks 40 or above → Average
●​ All remaining cases → Needs Improvement
Q3.
Consider this query:
SELECT
name,
marks,
CASE
WHEN marks >= 50 THEN 'Good'
WHEN marks >= 80 THEN 'Excellent'
ELSE 'Needs Improvement'
END AS performance
FROM students;
Answer:
1.​ What performance category will a student with 85 marks receive?
2.​ Why doesn't that student receive Excellent?
3.​ What does this tell you about the order of WHEN conditions?
*/

-- Q1
SELECT name, marks,
CASE
    WHEN marks >= 40 THEN 'Pass'
    ELSE 'Fail'
END result
FROM students;

-- Q2
SELECT name, marks,
CASE
    WHEN marks >= 80 THEN 'Excellent'
    WHEN marks >= 60 THEN 'Good'
    WHEN marks >= 40 THEN 'Average'
    ELSE 'Needs Improvement'
END result
FROM students;

-- Q3
/*
-- CASE checks WHEN conditions from top to bottom.
-- It returns the result of the first matching condition.
-- Therefore, condition order matters.
-- Place higher thresholds first to avoid incorrect matches.
*/

/*
Questions 4–6: Core concepts
Q4. CASE with multiple conditions
A table employees contains:
employee_id, name, salary, department
Write a query to classify employees based on salary:
●​ Salary above ₹60,000 → High Salary
●​ Salary between ₹30,000 and ₹60,000 (inclusive) → Medium Salary
●​ Salary below ₹30,000 → Low Salary
Display employee name, salary, and the salary category.
Q5. Simple CASE expression
A table orders contains:
order_id, customer_name, status
The status column contains values such as P, S, D, and C.
Write a query to display:
●​ P → Pending
●​ S → Shipped
●​ D → Delivered
●​ C → Cancelled
●​ Any other value → Unknown Status
Use the simple form of the CASE expression.
Q6. CASE in ORDER BY
A table employees contains:
employee_id, name, department, salary
The company wants employees displayed in this custom department order:
1.​ IT
2.​ HR
3.​ Sales
4.​ Finance
Write a query that sorts employees according to this order rather than alphabetical order.
*/

-- Q4
SELECT name, salary,
CASE
    WHEN salary > 60000 THEN 'High Salary'
    WHEN salary BETWEEN 30000 AND 60000 THEN 'Medium Salary'
    WHEN salary < 30000 THEN 'Low Salary'
END salary_category
FROM employees;

-- Q5
SELECT order_id, customer_name, status,
CASE status
    WHEN 'P' THEN 'Pending'
    WHEN 'S' THEN 'Shipped'
    WHEN 'D' THEN 'Delivered'
    WHEN 'C' THEN 'Cancelled'
    ELSE 'Unknown Status'
END AS order_status
FROM orders;

-- Q6
SELECT employee_id, name, department, salary
FROM employees
ORDER BY
    CASE
        WHEN department = 'IT' THEN 1
        WHEN department = 'HR' THEN 2
        WHEN department = 'Sales' THEN 3
        WHEN department = 'Finance' THEN 4
    END;

/*
Questions 7–9: Practical application
Q7. Creating a discount category
An online store has a table products:
product_id, product_name, price
The manager wants to classify products:
●​ Price below ₹500 → Budget
●​ Price from ₹500 to ₹2,000 → Standard
●​ Price above ₹2,000 → Premium
Display product name, price, and the generated category.
Q8. Prioritizing customer orders
A table orders contains:
order_id, customer_name, order_status, order_date
The operations team wants to see orders in this priority:
1.​ Pending
2.​ Processing
3.​ Shipped
4.​ Delivered
Within each status, the oldest order should appear first.
Write a query to produce this sorting.
Q9. Conditional sorting
A table employees contains:
employee_id, name, department, salary
The HR team wants:
●​ IT employees sorted by salary from highest to lowest.
●​ All other employees sorted by name alphabetically.
Write a query that achieves this using conditional sorting.
*/

-- Q7
SELECT product_name, price, 
CASE
    WHEN price < 500 THEN 'Budget'
    WHEN price BETWEEN 500 AND 2000 THEN 'Standard'
    WHEN price > 2000 THEN 'Premium'
END category
FROM products;

-- Q8
SELECT order_id, customer_name, order_status, order_date
FROM orders
ORDER BY 
    CASE
        WHEN order_status = 'Pending' THEN 1
        WHEN order_status = 'Processing' THEN 2
        WHEN order_status = 'Shipped' THEN 3
        WHEN order_status = 'Delivered' THEN 4
    END,
    order_date ASC;

-- Q9
SELECT employee_id, name, department, salary
FROM employees
ORDER BY
    CASE
        WHEN department = 'IT' THEN salary
    END DESC,

    CASE
        WHEN department <> 'IT' THEN name
    END ASC;

/*
Questions 10–12: Deeper understanding
Q10. Find the mistake
A beginner writes this query:
None
SELECT
name,
marks,
CASE
WHEN marks >= 40 THEN 'Pass'
WHEN marks < 40 THEN 'Fail'
ELSE 'Not Available'
AS result
FROM students;
Identify the syntax mistake and rewrite the query correctly.
Q11. Understanding CASE evaluation
Consider this query:
None
SELECT
name,
marks,
CASE
WHEN marks >= 40 THEN 'Pass'
WHEN marks >= 80 THEN 'Excellent'
ELSE 'Fail'
END AS result
FROM students;
Answer:
1.​ What happens when marks are 90?
2.​ Does SQL check every WHEN condition after finding a match?
3.​ Why might the order of conditions change the result?
4.​ How would you arrange the conditions to make Excellent and Pass both work
correctly?
Q12. CASE and NULL values
A table employees contains:
employee_id name salary
1 Aman 50000
2 Riya NULL
3 Rahul 25000
Consider this query:
None
SELECT
name,
salary,
CASE
WHEN salary >= 40000 THEN 'High'
WHEN salary < 40000 THEN 'Low'
ELSE 'Unknown'
END AS salary_category
FROM employees;
Answer:
1.​ What category will Aman receive?
2.​ What category will Rahul receive?
3.​ What category will Riya receive?
4.​ Why does the ELSE branch handle the NULL salary?
*/

-- Q10
SELECT name, marks, 
CASE
    WHEN marks >= 40 THEN 'Pass'
    WHEN marks < 40 THEN 'Fail'
    ELSE 'Not Available'
END AS result
FROM students;

-- Q11
/*
CASE evaluates WHEN conditions from top to bottom.
It returns the result of the first matching condition.
Once a condition matches, remaining conditions are ignored.
Place higher thresholds before lower thresholds to avoid 
incorrect results.
*/

-- Q12
/*
NULL represents a missing or unknown value. 
Comparisons with NULL return UNKNOWN, not TRUE or FALSE. 
CASE executes ELSE when no WHEN condition is TRUE. 
Therefore, NULL salary receives the category 'Unknown'.
*/

/*
Questions 13–14: Mixed problems
Q13. CASE with filtering and sorting
A table students contains:
student_id, name, marks, city
Write a query that:
●​ Includes only students from Delhi or Mumbai.
●​ Creates a performance column:
1.​ Marks 80 or above → Excellent
2.​ Marks 60 or above → Good
3.​ Marks 40 or above → Average
4.​ Otherwise → Fail
●​ Sorts students by performance in this order:
1.​ Excellent
2.​ Good
3.​ Average
4.​ Fail
Within each performance category, sort by marks from highest to lowest.
Q14. Combining CASE with aggregate functions
A table orders contains:
order_id, customer_id, order_amount, order_status
The manager wants a report showing:
Each customer_id
Total number of orders
Total order amount
A customer category:
○​ Total spending above ₹50,000 → High Value
○​ Total spending above ₹20,000 → Medium Value
○​ Otherwise → Low Value
Write a query that groups the records by customer and creates the category based on each
customer's total spending.
*/

-- Q13
SELECT student_id, name, marks, city,
CASE
    WHEN marks >= 80 THEN 'Excellent'
    WHEN marks >= 60 THEN 'Good'
    WHEN marks >= 40 THEN 'Average'
    ELSE 'Fail'
END AS performance
FROM students
WHERE city IN ('Delhi', 'Mumbai')
ORDER BY
    CASE
        WHEN marks >= 80 THEN 1
        WHEN marks >= 60 THEN 2
        WHEN marks >= 40 THEN 3
        ELSE 4
    END ASC,
    marks DESC;