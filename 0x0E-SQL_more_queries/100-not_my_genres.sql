-- List all shows not linked to Dexter
SELECT a.name
FROM tv_genres a
JOIN tv_show_genres b
ON a.id = b.genre_id
JOIN tv_shows c
ON c.id = b.show_id
WHERE c.title != 'Dexter'
GROUP BY a.name
ORDER BY a.name ASC;
