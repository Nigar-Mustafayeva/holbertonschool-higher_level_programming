-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply changes immediately
FLUSH PRIVILEGES;
