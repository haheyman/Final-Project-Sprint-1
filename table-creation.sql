-- Show the code used to create the tables needed for this assignment

-- Create the facility table
CREATE TABLE if not exists facility (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create the classroom table
CREATE TABLE if not exists classroom (
    id INT AUTO_INCREMENT PRIMARY KEY,
    capacity INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    facility_id INT,
    FOREIGN KEY (facility_id) REFERENCES facility(id)
);

-- Create the teacher table
CREATE TABLE if not exists teacher (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    room INT,
    FOREIGN KEY (room) REFERENCES classroom(id)
);

-- Create the child table
CREATE TABLE if not exists child (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    room INT,
    FOREIGN KEY (room) REFERENCES classroom(id)
);
