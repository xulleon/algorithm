# https://leetcode.com/problems/find-users-with-valid-e-mails/
# Write your MySQL query statement below
# select user_id, name, mail from Users
# where mail REGEXP '^[A-Za-z]+[A-Za-z0-9_.-]*@leetcode\.com$'
# order by user_id

SELECT
    user_id, name, mail
FROM Users
WHERE mail REGEXP '^[:alpha:]+[[:alnum:]_.-]*@leetcode.com$'
ORDER BY user_id
