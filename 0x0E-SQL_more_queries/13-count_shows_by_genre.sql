-- A script that lists all genres from the database hbtn_0d_tvshows along with the number of
-- it displays shows linked to each.
-- it does not display genres without linked shows.
-- the records are ordered by descending number of shows linked.
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
