create database parking_management_system;
use parking_management_system;
CREATE TABLE parking_info (
  name varchar(100) NOT NULL,
  uid_no int NOT NULL,
  ph_no decimal(10,0) DEFAULT NULL,
  timein varchar(15) DEFAULT NULL,
  timeout varchar(15) DEFAULT NULL,
  park_loc varchar(5) NOT NULL,
  token_number varchar(15) NOT NULL,
  vehicle_number varchar(15) NOT NULL,
  vehicle_type varchar(15) NOT NULL,
  PRIMARY KEY (uid_no),
  UNIQUE KEY token_number (token_number),
  UNIQUE KEY vehicle_number (vehicle_number),
  UNIQUE KEY ph_no (ph_no)
) ;
CREATE TABLE login (
  name varchar(100) NOT NULL,
  uid_no int NOT NULL,
  ph_no decimal(12,0) NOT NULL,
  vehicle_number varchar(15) NOT NULL,
  vehicle_type varchar(15) NOT NULL,
  PRIMARY KEY (uid_no),
  UNIQUE KEY ph_no (ph_no),
  UNIQUE KEY vehicle_number (vehicle_number)
) ;
CREATE TABLE history_logs (
  name varchar(100) DEFAULT NULL,
  uid_no int DEFAULT NULL,
  ph_no int DEFAULT NULL,
  timein varchar(15) DEFAULT NULL,
  timeout varchar(15) DEFAULT NULL,
  park_loc varchar(5) DEFAULT NULL,
  token_number varchar(15) DEFAULT NULL,
  vehicle_number varchar(15) DEFAULT NULL,
  vehicle_type varchar(15) DEFAULT NULL
) ;