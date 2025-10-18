-- Select the correct database
USE alx_book_store;

-- Retrieve full description of the 'Books' table using INFORMATION_SCHEMA
SELECT COLUMN_NAME, COLUMN_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
  AND TABLE_NAME = 'Books';
