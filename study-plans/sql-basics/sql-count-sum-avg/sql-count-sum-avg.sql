-- Write your SQL query here
select
    category,
COUNT(category) as total_sales,
SUM(amount) as total_revenue,
AVG(discount) as avg_discount

from sales
group by category
order by
total_revenue desc,
category asc;
