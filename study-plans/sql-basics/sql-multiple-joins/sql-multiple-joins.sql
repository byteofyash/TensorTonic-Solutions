-- Write your SQL query here
select
    username,
    experiment_name,
    variant,
    revenue
from users u

INNER JOIN  experiment_assignments e
ON u.id = e.user_id
 
INNER JOIN  conversions c
ON u.id = c.user_id
    

ORDER by
    experiment_name ASC,
    revenue DESC,
    username ASC;