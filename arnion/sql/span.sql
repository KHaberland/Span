CREATE DATABASE IF NOT EXISTS span;
USE span;
DROP TABLE IF EXISTS `departments`;
CREATE TABLE IF NOT  EXISTS `departments` (
    `department_id` INT(11) NOT NULL AUTO_INCREMENT,
    `department_name` VARCHAR(250) NOT NULL DEFAULT '',
    PRIMARY KEY (`department_id`)
 ) ENGINE=MYISAM DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `employees`;
CREATE TABLE IF NOT  EXISTS `employees` (
    `employee_id` INT(11) NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(100) NOT NULL DEFAULT '',
    `middle_name` VARCHAR(100) NOT NULL DEFAULT '',
    `last_name` VARCHAR(100) NOT NULL DEFAULT '',
    `department_id` INT(11) NOT NULL DEFAULT 0,
    PRIMARY KEY (`employee_id`)
 ) ENGINE=MYISAM DEFAULT CHARSET=utf8;

INSERT INTO departments (department_id, department_name)
VALUES (1, 'Бухгалтерия');

INSERT INTO departments (department_id, department_name)
VALUES (2, 'Отдел программирования');

INSERT INTO departments (department_id, department_name)
VALUES (3, 'Служба поддержки клиентов');

INSERT INTO employees (first_name, middle_name, last_name, department_id)
VALUES ('Артем', 'Юрьевич', 'Валентинов', 1);

INSERT INTO employees (first_name, middle_name, last_name, department_id)
VALUES ('Галина', 'Руслановна', 'Маргаритова', 1);

INSERT INTO employees (first_name, middle_name, last_name, department_id)
VALUES ('Артем', 'Николаевич', 'Григорин', 2);

INSERT INTO employees (first_name, middle_name, last_name, department_id)
VALUES ('Игорь', 'Павлович', 'Лепетун', 2);

INSERT INTO employees (first_name, middle_name, last_name, department_id)
VALUES ('Андрей', 'Валентинович', 'Горский', 3);

INSERT INTO employees (first_name, middle_name, last_name, department_id)
VALUES ('Сергей', 'Петрович', 'Королев', 3);