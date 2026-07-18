-- Write your SQL query here
select
account,
txn_date, 
    amount,
    SUM(amount) OVER(partition by account order by txn_date) as running_total 

from transactions

order by
account asc,
    txn_date asc,  
    id asc;