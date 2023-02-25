SELECT name FROM SalesPerson
WHERE sales_id NOT IN(SELECT sales_id 
FROM Company c INNER JOIN Orders o
ON c.com_id=o.com_id WHERE name="RED");