CREATE DATABASE helping_hands;

use helping_hands;
CREATE TABLE admin (username char(8) not null, password varchar(30) not null);
INSERT into admin VALUES ('ADM001','Enigma');

CREATE TABLE empid_list (emp_id char(8), PRIMARY KEY(emp_id));

CREATE TABLE user_details (emp_id char(8), name varchar(25) not null, phone_number char(10) not null, date_of_birth date not null, password varchar(30) not null, gender varchar(6) not null, branch_id char(7), dept_id char(7), security_question varchar(50),security_answer varchar(20),PRIMARY KEY(emp_id));

CREATE TABLE branch(branch_id varchar(7), branch_name varchar(30) not null, branch_location varchar(100) not null, PRIMARY KEY(branch_id));

CREATE TABLE department(branch_id char(7), dept_id char(7), dept_name varchar(30) not null, total_jobs integer default 0, vacant_jobs integer default 0, PRIMARY KEY(dept_id));

    ALTER TABLE user_details ADD FOREIGN KEY (branch_id) REFERENCES branch(branch_id);

ALTER TABLE user_details ADD FOREIGN KEY (dept_id) REFERENCES department(dept_id);

ALTER TABLE department ADD FOREIGN KEY (branch_id) REFERENCES branch(branch_id);