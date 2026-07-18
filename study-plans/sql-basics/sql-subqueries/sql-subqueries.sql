-- Write your SQL query here
select
    distinct name, price,
    ROUND(price - ( select AVG(price) as avg  from products ),2) as vs_avg
from products p 
inner join sales s
on p.id = s.product_id

order by
vs_avg desc,
name asc;