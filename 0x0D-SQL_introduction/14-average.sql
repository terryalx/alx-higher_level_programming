-- Print the average score
-- column name should be average
-- Execute: cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT AVG(score) AS average FROM second_table;
