-- Lists all tv shows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
GROUP BY tv_shows.title, tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
