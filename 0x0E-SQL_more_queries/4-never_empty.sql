-- creates the table id_not_null on your MySQL server.
-- id_not_null description: id INT with the default value 1, name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the table id_not_null already exists, your script should not fail
-- Execute: cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
