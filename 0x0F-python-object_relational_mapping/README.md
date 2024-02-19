0x0F. Python - Object-relational mapping
Tasks
0. Get all states
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all states from the database hbtn_0e_0_usa:
•	Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
•	You must use the module MySQLdb (import MySQLdb)
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Results must be sorted in ascending order by states.id
•	Results must be displayed as they are in the example below
•	Your code should not be executed when imported
1. Filter states
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
•	Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
•	You must use the module MySQLdb (import MySQLdb)
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Results must be sorted in ascending order by states.id
•	Results must be displayed as they are in the example below
•	Your code should not be executed when imported
2. Filter states by user input
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
•	Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
•	You must use the module MySQLdb (import MySQLdb)
•	Your script should connect to a MySQL server running on localhost at port 3306
•	You must use format to create the SQL query with the user input
•	Results must be sorted in ascending order by states.id
•	Results must be displayed as they are in the example below
•	Your code should not be executed when imported
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
No test cases needed
Repo:
•	GitHub repository: alx-higher_level_programming
•	Directory: 0x0F-python-object_relational_mapping
•	File: 2-my_filter_states.py
 Done? Help Check your code Ask for a new correction Get a sandbox QA Review
3. SQL Injection...
mandatory
Score: 0.0% (Checks completed: 0.0%)
Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 
What? Empty?
Yes, it’s an SQL injection to delete all records of a table…
Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
•	Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
•	You must use the module MySQLdb (import MySQLdb)
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Results must be sorted in ascending order by states.id
•	Results must be displayed as they are in the example below
•	Your code should not be executed when imported
4. Cities by states
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all cities from the database hbtn_0e_4_usa
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module MySQLdb (import MySQLdb)
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Results must be sorted in ascending order by cities.id
•	You can use only execute() once
•	Results must be displayed as they are in the example below
•	Your code should not be executed when imported
5. All cities by state
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
•	Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
•	You must use the module MySQLdb (import MySQLdb)
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Results must be sorted in ascending order by cities.id
•	You can use only execute() once
•	The results must be displayed as they are in the example below
•	Your code should not be executed when imported
6. First state model
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a python file that contains the class definition of a State and an instance Base = declarative_base():
•	State class:
o	inherits from Base Tips
o	links to the MySQL table states
o	class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
o	class attribute name that represents a column of a string with maximum 128 characters and can’t be null
•	You must use the module SQLAlchemy
•	Your script should connect to a MySQL server running on localhost at port 3306
•	WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)
7. All states via SQLAlchemy
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all State objects from the database hbtn_0e_6_usa
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module SQLAlchemy
•	You must import State and Base from model_state - from model_state import Base, State
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Results must be sorted in ascending order by states.id
•	The results must be displayed as they are in the example below
•	Your code should not be executed when imported
8. First state
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that prints the first State object from the database hbtn_0e_6_usa
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module SQLAlchemy
•	You must import State and Base from model_state - from model_state import Base, State
•	Your script should connect to a MySQL server running on localhost at port 3306
•	The state you display must be the first in states.id
•	You are not allowed to fetch all states from the database before displaying the result
•	The results must be displayed as they are in the example below
•	If the table states is empty, print Nothing followed by a new line
•	Your code should not be executed when imported
guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/0x0F$ 
No test cases needed
Repo:
•	GitHub repository: alx-higher_level_programming
•	Directory: 0x0F-python-object_relational_mapping
•	File: 8-model_state_fetch_first.py
 Done? Help Check your code Ask for a new correction Get a sandbox QA Review
9. Contains `a`
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module SQLAlchemy
•	You must import State and Base from model_state - from model_state import Base, State
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Results must be sorted in ascending order by states.id
•	The results must be displayed as they are in the example below
•	Your code should not be executed when imported
guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/0x0F$ 
No test cases needed
Repo:
•	GitHub repository: alx-higher_level_programming
•	Directory: 0x0F-python-object_relational_mapping
•	File: 9-model_state_filter_a.py
 Done? Help Check your code Ask for a new correction Get a sandbox QA Review
10. Get a state
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
•	Your script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
•	You must use the module SQLAlchemy
•	You must import State and Base from model_state - from model_state import Base, State
•	Your script should connect to a MySQL server running on localhost at port 3306
•	You can assume you have one record with the state name to search
•	Results must display the states.id
•	If no state has the name you searched for, display Not found
•	Your code should not be executed when imported
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/0x0F$ 
No test cases needed
Repo:
•	GitHub repository: alx-higher_level_programming
•	Directory: 0x0F-python-object_relational_mapping
•	File: 10-model_state_my_get.py
 Done? Help Check your code Ask for a new correction Get a sandbox QA Review
11. Add a new state
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module SQLAlchemy
•	You must import State and Base from model_state - from model_state import Base, State
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Print the new states.id after creation
•	Your code should not be executed when imported
guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
No test cases needed
Repo:
•	GitHub repository: alx-higher_level_programming
•	Directory: 0x0F-python-object_relational_mapping
•	File: 11-model_state_insert.py
 Done? Help Check your code Ask for a new correction Get a sandbox QA Review
12. Update a state
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that changes the name of a State object from the database hbtn_0e_6_usa
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module SQLAlchemy
•	You must import State and Base from model_state - from model_state import Base, State
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Change the name of the State where id = 2 to New Mexico
•	Your code should not be executed when imported
13. Delete states
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module SQLAlchemy
•	You must import State and Base from model_state - from model_state import Base, State
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Your code should not be executed when imported
14. Cities in state
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.
•	City class:
o	inherits from Base (imported from model_state)
o	links to the MySQL table cities
o	class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
o	class attribute name that represents a column of a string of 128 characters and can’t be null
o	class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
•	You must use the module SQLAlchemy
Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module SQLAlchemy
•	You must import State and Base from model_state - from model_state import Base, State
•	Your script should connect to a MySQL server running on localhost at port 3306
•	Results must be sorted in ascending order by cities.id
•	Results must be display as they are in the example below (<state name>: (<city id>) <city name>)
•	Your code should not be executed when imported
15. City relationship
#advanced
Score: 0.0% (Checks completed: 0.0%)
Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py:
•	City class:
o	No change
•	State class:
o	In addition to previous requirements, the class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
•	You must use the module SQLAlchemy
Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module SQLAlchemy
•	Your script should connect to a MySQL server running on localhost at port 3306
•	You must use the cities relationship for all State objects
•	Your code should not be executed when imported
16. List relationship
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module SQLAlchemy
•	The connection to your MySQL server must be to localhost on port 3306
•	You must only use one query to the database
•	You must use the cities relationship for all State objects
•	Results must be sorted in ascending order by states.id and cities.id
•	Results must be displayed as they are in the example below
•	Your code should not be executed when imported
17. From city
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all City objects from the database hbtn_0e_101_usa
•	Your script should take 3 arguments: mysql username, mysql password and database name
•	You must use the module SQLAlchemy
•	Your script should connect to a MySQL server running on localhost at port 3306
•	You must use only one query to the database
•	You must use the state relationship to access to the State object linked to the City object
•	Results must be sorted in ascending order by cities.id
•	Results must be displayed as they are in the example below
•	Your code should not be executed when imported
