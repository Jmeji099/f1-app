DROP DATABASE IF EXISTS f1App;

CREATE DATABASE f1App;

USE f1App;

DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS User_info;
DROP TABLE IF EXISTS Scores;
DROP TABLE IF EXISTS Friends;

CREATE TABLE Users (
    ID int NOT NULL AUTO_INCREMENT,
    username varchar(30) NOT NULL,
    password_hash varchar(30) NOT NULL,
    CONSTRAINT UC_User UNIQUE(ID,username),
    PRIMARY KEY (ID)
);

CREATE TABLE User_info (
    user_ID int,
    first_name varchar(20),
    last_name varchar(20),
    email varchar(20) NOT NULL DEFAULT '',
    UNIQUE(email),
    FOREIGN KEY (user_ID) REFERENCES Users(ID)
);

CREATE TABLE Scores(
    user_ID int,
    time_score VARCHAR(12),
    FOREIGN KEY (user_ID) REFERENCES Users(ID)
);

CREATE TABLE Friends(
    member1ID int,
    member2ID int, 
    Created datetime NOT NULL,
    FOREIGN KEY (Member1ID) REFERENCES Users(ID),
    FOREIGN KEY (Member2ID) REFERENCES Users(ID)
);


INSERT INTO Users (username,password_hash)
VALUES ('user1','hashedpassword'),
('user2', 'anotherhashedpassword');

INSERT INTO User_info (user_ID, first_name,last_name,email)
VALUES (1, 'Juan', 'Mejia', 'myemail@email.com'),
(2, 'Bob', 'User', 'user2@email.com');

INSERT INTO Scores (user_ID, time_score)
VALUES (1, '00:00:00:00');

INSERT INTO Friends (member1ID, member2ID,Created)
VALUES (1,2,curdate());
