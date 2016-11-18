CREATE DATABASE IF NOT EXISTS TheSeed;
USE TheSeed;

CREATE TABLE IF NOT EXISTS Users
(
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    fname varchar(255),
    lname varchar(255),
    email varchar(255),
    pass varchar(255)
);

CREATE TABLE IF NOT EXISTS Retailers
(
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name varchar(255),
    url varchar(2047)
);

CREATE TABLE IF NOT EXISTS Products
(
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name varchar(255),
    quantity int,
    dateCreated date,
    dateScraped date,
    price double precision,
    source varchar(2047)
);

CREATE TABLE IF NOT EXISTS GardenFreshBoxes
(
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
);

CREATE TABLE IF NOT EXISTS PodOrderForms
(
    id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
);
