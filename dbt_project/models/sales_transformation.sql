SELECT
customer_id,
SUM(price * quantity) AS total_sales
FROM raw_sales
GROUP BY customer_id
