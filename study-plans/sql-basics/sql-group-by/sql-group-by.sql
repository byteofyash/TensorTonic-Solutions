-- Write your SQL query here
select
customer,
COUNT(product) as total_orders,
SUM(amount) as total_spent

from orders
    
group by customer
    
order by
    total_spent DESC;