-- Write your SQL query here

select
username,
segment,
engagement_score,
ROW_NUMBER() OVER ( PARTITION BY segment 
                    ORDER BY engagement_score DESC, username ASC) AS activity_rank 


from user_activity

order by
segment asc,
activity_rank asc;
