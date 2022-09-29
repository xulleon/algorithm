# https://leetcode.com/problems/customer-order-frequency/
# Write your MySQL query statement below
# Solution One:
SELECT
    C.customer_id as CUSTOMER_ID,
    name as NAME
FROM
    Customers C,
    Product P,
    Orders O
WHERE
    C.customer_id=O.customer_id
    AND
    P.product_id=O.product_id

GROUP BY
    O.customer_id
HAVING
    SUM(CASE WHEN LEFT(order_date, 7)='2020-06' THEN quantity * price ELSE 0 END) >= 100
    AND
    SUM(CASE WHEN LEFT(order_date, 7)='2020-07' THEN quantity * price ELSE 0 END) >= 100

# Solution Two
SELECT
    C.customer_id as CUSTOMER_ID,
    name as NAME
FROM
    Customers C,
    Product P,
    Orders O
WHERE
    C.customer_id=O.customer_id
    AND
    P.product_id=O.product_id

GROUP BY
    O.customer_id
HAVING
    SUM(IF(LEFT(order_date, 7)='2020-06', quantity, 0) * price) >= 100
    AND
    SUM(IF(LEFT(order_date, 7)='2020-07', quantity, 0) * price) >= 100

# Solution Three
SELECT C.customer_id as CUSTOMER_ID,
       name as NAME
FROM Customers C
JOIN Orders O
ON C.customer_id=O.customer_id
JOIN Product P
ON P.product_id=O.product_id
GROUP BY
    C.customer_id
HAVING
    SUM(CASE WHEN LEFT(order_date, 7)='2020-06' THEN quantity * price ELSE 0 END) >= 100
    AND
    SUM(CASE WHEN LEFT(order_date, 7)='2020-07' THEN quantity * price ELSE 0 END) >= 100
