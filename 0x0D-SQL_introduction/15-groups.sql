-- Select count and grouping
-- The list should be sorted by the number of records (descending)
-- Execute: cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
