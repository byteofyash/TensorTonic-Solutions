-- Write your SQL query here
SELECT 
    u.username ,
    COALESCE(r.username, 'organic') AS referrer_name
FROM user_referrals AS u
LEFT JOIN user_referrals AS r
ON u.referred_by = r.id
    
ORDER by
    u.username ASC;