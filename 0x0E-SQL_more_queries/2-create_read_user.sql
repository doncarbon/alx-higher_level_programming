-- SQL script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS `hbtn_0c_2`;

CREATE USER IF NOT EXISTS user_0d_2@hostname IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0c_2.* TO user_0d_2@localhost;
