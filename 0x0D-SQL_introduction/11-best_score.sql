-- Lists all records of the table second_table
-- of the database hbtn_0c_0 in your MySQL server
-- Displays both the score and the name (in this order)
-- and ordered by score

SELECT score, name FROM second_table
WHERE score >= 10 
ORDER BY score DESC;
