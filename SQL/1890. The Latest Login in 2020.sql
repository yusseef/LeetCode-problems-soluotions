# Write your MySQL query statement below
SELECT DISTINCT user_id, MAX(time_stamp) AS last_stamp FROM logins 
GROUP BY user_id
WHERE year(time_stamp) = '2020''