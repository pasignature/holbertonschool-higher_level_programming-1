-- List all show wtihout the comedy genre
SELECT d.title
FROM (SELECT a.title, c.name
     FROM tv_shows a
     LEFT JOIN tv_show_genres b
     ON a.id = b.show_id
     LEFT JOIN tv_genres c
     ON b.genre_id = c.id) d
WHERE d.name != 'Comedy' OR d.name IS NULL
GROUP BY d.title
ORDER BY d.title ASC;
