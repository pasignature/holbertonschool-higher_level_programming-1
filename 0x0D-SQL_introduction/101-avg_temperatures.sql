-- import into hbtn_c0_0 temp database and display average temp
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
