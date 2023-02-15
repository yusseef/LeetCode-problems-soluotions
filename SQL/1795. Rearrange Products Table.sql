SELECT product_id, 'store1' AS store, store1 as price FROM products WHERE store1 IS NOT NULL
UNION 
SELECT product_id, 'store2' AS store, store2 as price FROM products WHERE store2 IS NOT NULL
UNION 
SELECT product_id, 'store3' AS store, store3 as price From products WHERE store3 IS NOT NULL
ORDER BY 1,2 ASC;