CREATE DATABASE apartment_db;
USE apartment_db;

CREATE TABLE flats (
    flat_no VARCHAR(10) PRIMARY KEY,
    floor INT,
    bhk INT,
    owner_name VARCHAR(100),
    owner_phone VARCHAR(15),
    status ENUM('Occupied', 'Vacant') DEFAULT 'Vacant'
);

CREATE TABLE residents (
    resident_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    email VARCHAR(100),
    flat_no VARCHAR(10),
    type ENUM('Owner', 'Tenant'),
    move_in_date DATE,
    FOREIGN KEY (flat_no) REFERENCES flats(flat_no) ON DELETE SET NULL
);

CREATE TABLE visitors (
    visitor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    flat_no VARCHAR
