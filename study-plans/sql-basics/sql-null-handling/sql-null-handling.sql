-- Write your SQL query here
select
name,  
COALESCE(email, 'N/A') as display_email, 

CASE
  WHEN deactivated_at IS NULL THEN 'active'
  ELSE 'inactive'
END as status
 

from customers
where phone is not null


order by
name asc;