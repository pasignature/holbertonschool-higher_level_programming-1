-- Creates a user user_0d_1 on the mysql server
CREATE USER IF NOT EXISTS user_0d_1@localhost;
GRANT ALL ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
