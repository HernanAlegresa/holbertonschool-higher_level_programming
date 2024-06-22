-- Task 15: List the number of records with the same score in 'second_table'
-- The result should be: score and number of records for this score
-- The list should be sorted by the number of records (descending)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
