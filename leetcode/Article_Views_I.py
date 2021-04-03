# https://leetcode.com/problems/article-views-i/
# Write your MySQL query statement below
# here it is important to use "DISTINCT" to remove dup AND "ORDER BY id" to make sort it.
SELECT DISTINCT
    viewer_id as id
FROM
    Views
WHERE
    author_id = viewer_id
ORDER BY id
