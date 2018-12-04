-- List all shows and all genres linked to that show from the DB
SELECT a.title, c.name
FROM tv_shows a
LEFT JOIN tv_show_genres b
ON a.id = b.show_id
LEFT JOIN tv_genres c
ON c.id = b.genre_id
ORDER BY a.title ASC;
