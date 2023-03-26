# Write your MySQL query statement below

SELECT email FROM person
GROUP BY email
HAVING count(email) > 1