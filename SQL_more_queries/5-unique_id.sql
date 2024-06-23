-- Task 5: Create the table 'unique_id' with 'id' column that must be unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
