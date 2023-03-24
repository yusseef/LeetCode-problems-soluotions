# Write your MySQL query statement below
WITH cte AS
(SELECT customer_number, COUNT(order_number) AS OrderNum
FROM ORDERS
GROUP BY customer_number)

SELECT customer_number
FROM cte 
WHERE OrderNum = (SELECT MAX(OrderNum) FROM cte);