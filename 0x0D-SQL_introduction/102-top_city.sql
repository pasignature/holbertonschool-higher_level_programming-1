-- Displays the top 3 cities temps during July and August ordered by temp desc
SELECT city, AVG(value) as avg_temp FROM temperatures where month IN (7, 8) GROUP BY CITY ORDER BY avg_temp DESC LIMIT 3;
