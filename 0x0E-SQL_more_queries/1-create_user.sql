-- creates the MySQL server user
CREATE USER IF NOT EXISTS 'Tester_user'@'localhost' IDENTIFIED BY 'petchrix1';
GRANT ALL PRIVILEGES ON *.* TO 'chrixsaint' @'localhost';
GRANT ALL PRIVILEGES ON hotelDb.* TO 'Tester_user' @'localhost';

//how to drop a user from a database
DROP USER "Tester_user" @'localhost';


