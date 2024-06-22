-- Task 16: List all records from 'second_table' where name is not null
-- Results should display: score and name
-- Records should be listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
