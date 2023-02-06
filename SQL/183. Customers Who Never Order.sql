# Write your MySQL query statement below

SELECT Customers.name as Customers from Customers
LEFT JOIN Orders
on Customers.id = Orders.customerId
WHERE Orders.customerId is NULL;