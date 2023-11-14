-- Lists rows with name value
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
-- Execute: cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;
