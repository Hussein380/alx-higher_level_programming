-- creates the database hbtn_Od_2  and the user user_0d_2.
-- creates a database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
-- Creates a user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grants SELECT privileges to a use
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
