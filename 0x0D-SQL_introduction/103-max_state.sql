-- displays the max temperature of each state (ordered by State name).
-- Execute: cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
