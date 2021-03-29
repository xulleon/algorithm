# https://leetcode.com/problems/reformat-department-table/
# Write your MySQL query statement below
select id,
    SUM(CASE WHEN month='Jan' THEN revenue ELSE Null END) AS 'Jan_Revenue',
    SUM(CASE WHEN month='Feb' THEN revenue ELSE Null END) AS 'Feb_Revenue',
    SUM(CASE WHEN month='Mar' THEN revenue ELSE Null END) AS 'Mar_Revenue',
    SUM(CASE WHEN month='Apr' THEN revenue ELSE Null END) AS 'Apr_Revenue',
    SUM(CASE WHEN month='May' THEN revenue ELSE Null END) AS 'May_Revenue',
    SUM(CASE WHEN month='Jul' THEN revenue ELSE Null END) AS 'Jul_Revenue',
    SUM(CASE WHEN month='Jun' THEN revenue ELSE Null END) AS 'Jun_Revenue',
    SUM(CASE WHEN month='Aug' THEN revenue ELSE Null END) AS 'Aug_Revenue',
    SUM(CASE WHEN month='Sep' THEN revenue ELSE Null END) AS 'Sep_Revenue',
    SUM(CASE WHEN month='Oct' THEN revenue ELSE Null END) AS 'Oct_Revenue',
    SUM(CASE WHEN month='Nov' THEN revenue ELSE Null END) AS 'Nov_Revenue',
    SUM(CASE WHEN month='Dec' THEN revenue ELSE Null END) AS 'Dec_Revenue'
FROM Department
GROUP BY id;
