SELECT 
    DISTINCT player_id, 
    FIRST_VALUE(event_date) OVER(PARTITION BY player_id ORDER BY event_date) AS first_login
FROM activity;

SELECT 
    DISTINCT player_id, 
    min(event_date) AS first_login
FROM activity
GROUP BY player_id;

SELECT 
    rank_table.player_id,
    rank_table.event_date AS first_login
FROM
(SELECT 
    player_id,
    event_date,
    dense_rank() OVER(PARTITION BY player_id ORDER BY event_date) AS ranking
FROM activity) rank_table
WHERE rank_table.ranking=1

