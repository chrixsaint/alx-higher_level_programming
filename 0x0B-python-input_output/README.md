
0x0B. Python - Input/Output
Tasks
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
•	Prototype: def read_file(filename=""):
•	You must use the with statement
•	You don’t need to manage file permission or file doesn't exist exceptions.
•	You are not allowed to import any module
guillaume@ubuntu:~/0x0B$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

guillaume@ubuntu:~/0x0B$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ 
No test cases needed
Repo:
•	GitHub repository: alx-higher_level_programming
•	Directory: 0x0B-python-input_output
•	File: 0-read_file.py
 Done? Help Check your code Get a sandbox
1. Write to a file
mandatory
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
•	Prototype: def write_file(filename="", text=""):
•	You must use the with statement
•	You don’t need to manage file permission exceptions.
•	Your function should create the file if doesn’t exist.
•	Your function should overwrite the content of the file if it already exists.
•	You are not allowed to import any module
guillaume@ubuntu:~/0x0B$ cat 1-main.py
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

guillaume@ubuntu:~/0x0B$ ./1-main.py
29
guillaume@ubuntu:~/0x0B$ cat my_first_file.txt
This School is so cool!
guillaume@ubuntu:~/0x0B$ 
No test cases needed
Repo:
•	GitHub repository: alx-higher_level_programming
•	Directory: 0x0B-python-input_output
•	File: 1-write_file.py
2. Append to a file
mandatory
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
•	Prototype: def append_write(filename="", text=""):
•	If the file doesn’t exist, it should be created
•	You must use the with statement
•	You don’t need to manage file permission or file doesn't exist exceptions.
•	You are not allowed to import any module
3. To JSON string
mandatory
Write a function that returns the JSON representation of an object (string):
•	Prototype: def to_json_string(my_obj):
•	You don’t need to manage exceptions if the object can’t be serialized.
4. From JSON string to Object
mandatory
Write a function that returns an object (Python data structure) represented by a JSON string:
•	Prototype: def from_json_string(my_str):
•	You don’t need to manage exceptions if the JSON string doesn’t represent an object.
5. Save Object to a file
mandatory
Write a function that writes an Object to a text file, using a JSON representation:
•	Prototype: def save_to_json_file(my_obj, filename):
•	You must use the with statement
•	You don’t need to manage exceptions if the object can’t be serialized.
•	You don’t need to manage file permission exceptions.
6. Create object from a JSON file
mandatory
Write a function that creates an Object from a “JSON file”:
•	Prototype: def load_from_json_file(filename):
•	You must use the with statement
•	You don’t need to manage exceptions if the JSON string doesn’t represent an object.
•	You don’t need to manage file permissions / exceptions.
7. Load, add, save
mandatory
Write a script that adds all arguments to a Python list, and then save them to a file:
•	You must use your function save_to_json_file from 5-save_to_json_file.py
•	You must use your function load_from_json_file from 6-load_from_json_file.py
•	The list must be saved as a JSON representation in a file named add_item.json
•	If the file doesn’t exist, it should be created
•	You don’t need to manage file permissions / exceptions.
8. Class to JSON
mandatory
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
•	Prototype: def class_to_json(obj):
•	obj is an instance of a Class
•	All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
•	You are not allowed to import any module
9. Student to JSON
mandatory
Write a class Student that defines a student by:
•	Public instance attributes:
o	first_name
o	last_name
o	age
•	Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
•	Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
•	You are not allowed to import any module
10. Student to JSON with filter
mandatory
Write a class Student that defines a student by: (based on 9-student.py)
•	Public instance attributes:
o	first_name
o	last_name
o	age
•	Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
•	Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
o	If attrs is a list of strings, only attribute names contained in this list must be retrieved.
o	Otherwise, all attributes must be retrieved
•	You are not allowed to import any module
11. Student to disk and reload
mandatory
Write a class Student that defines a student by: (based on 10-student.py)
•	Public instance attributes:
o	first_name
o	last_name
o	age
•	Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
•	Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
o	If attrs is a list of strings, only attributes name contain in this list must be retrieved.
o	Otherwise, all attributes must be retrieved
•	Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
o	You can assume json will always be a dictionary
o	A dictionary key will be the public attribute name
o	A dictionary value will be the value of the public attribute
•	You are not allowed to import any module
Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)
12. Pascal's Triangle
mandatory
Technical interview preparation:
•	You are not allowed to google anything
•	Whiteboard first
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
•	Returns an empty list if n <= 0
•	You can assume n will be always an integer
•	You are not allowed to import any module
