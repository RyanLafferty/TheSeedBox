CREATE DATABASE IF NOT EXISTS TheSeed;
USE TheSeed;

CREATE TABLE IF NOT EXISTS users
(
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fname varchar(255),
    lname varchar(255),
    email varchar(255),
    pass varchar(255),

);
