-- Write your SQL query here
select
 customer,
COUNT(product) as total_orders, 
SUM(amount) as total_spent
    
from orders
group by customer
having total_orders >=2


order by
total_spent
desc;
