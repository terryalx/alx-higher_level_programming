-- Print all privileges of USER
-- user_0d_1 | user_0d_2
-- Execute: cat 0-privileges.sql | mysql -hlocalhost -uroot -p
SHOW GRANTS FOR `user_0d_1`@`localhost`;
SHOW GRANTS FOR `user_0d_2`@`localhost`;
