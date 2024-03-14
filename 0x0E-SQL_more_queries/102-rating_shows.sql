-- lists all shows from hbtn_0d_tvshows_rate by their rating
-- lists all rows of a table by the sum of a linked row
SELECT tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
