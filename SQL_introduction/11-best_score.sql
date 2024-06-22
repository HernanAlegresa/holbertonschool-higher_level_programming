-- Task 11: List all records with score >= 10 from 'second_table'
-- Results ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
