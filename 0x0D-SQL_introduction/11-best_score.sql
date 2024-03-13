-- list all record in the table second_table with a score >= 10 in MYSQL server.
-- Records are ordered by descending score
SELECT 'score', 'name' 
FROM 'second_table'
WHERE 'score' >= 10
ORDER BY 'score' DESC;
