-- Write your SQL query here
select
    department,
count(status) as total_tickets,
count(case when status = 'open' then 1 end) as open_count,
count(case when status = 'in_progress' then 1  end) as in_progress_count,
count(case when status = 'closed' then 1  end) as closed_count

from tickets

group by department

order by
 total_tickets desc, 
    department asc;


