-- Task 3: Create the table 'force_name' with 'name' column that can't be null
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
