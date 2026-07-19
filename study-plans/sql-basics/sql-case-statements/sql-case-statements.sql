-- Write your SQL query here
select
username,
session_count,
case 
    when us.session_count >=50 then 'Power'
    when us.session_count >=10 then 'Casual'
    else 'Dormant'
end as activity_level,

case 
    when us.platform in('ios','android') then 'Mobile'
    when us.platform in('web','desktop') then 'Desktop'
    else 'Other'
end as platform_type
    

from user_sessions us


ORDER BY 
CASE
    WHEN activity_level = 'Power' THEN 1
    WHEN activity_level = 'Casual' THEN 2
    WHEN activity_level = 'Dormant' THEN 3
END,
username asc;







