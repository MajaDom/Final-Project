CREATE USER 'finalproject'@'localhost' IDENTIFIED BY 'finalproject_pass';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD
on *.* TO 'finalproject'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS company_resources;