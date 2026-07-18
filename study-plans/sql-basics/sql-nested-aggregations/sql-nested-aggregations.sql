-- Write your SQL query herew
WITH daily_sums AS (
    SELECT order_date, 
            SUM(amount) AS daily_total,
            COUNT(*) as daily_order
    FROM orders
    GROUP BY order_date
)
SELECT 
    ROUND(AVG(daily_order),2) AS avg_daily_orders,
    ROUND(AVG(daily_total),2) AS avg_daily_revenue,
    MAX(daily_order) as busiest_day_orders
    

FROM daily_sums;
 