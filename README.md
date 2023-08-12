# 0x00. AirBnB clone - The console

This project is a console for the AirBnB clone. It handles serialization, deserialization and storage of instances of AirBnb.
These instances include: `User`, `BaseModel`, `Amenity`, `Place`, `State`, `City` and `Review`.
It was created using the python Cmd module.
### How to start the console

- Clone this repository. Open your terminal and run this command: `./console.py`
	- This command will start the console in interactive mode


- Alternatively, you can also run this console in non-interactive mode by piping or redirecting shell commands and files to it.
	- for example, running this command: `echo "cat" | ./console.py` will pass the word "cat" to the console.


### Cmd commands:
-   `create`: Creates a new instance of  a class, saves it and prints the `id`.
	- Execute this command: `create BaseModel`
		 - This creates  an instance of BaseModel and saves it

-   `show`: Prints the string representation of an instance based on the class name and `id`.
	- Execute this command: `show BaseModel 1234-1234-1234`.
	    -   If the class name is missing, it prints `** class name missing **`
	    -   If the class name doesn’t exist, it prints `** class doesn't exist **` (e.g if you run this command: `show MyModel`)
	    -   If the `id` is missing, it prints `** instance id missing **` (e.g if you run this command: `show BaseModel`)
	    -   If the instance of the class name doesn’t exist for the `id`, it prints `** no instance found **`
-   `destroy`: Deletes an instance based on the class name and `id` . 	for example, if you execute this command: `destroy BaseModel 1234-1234-1234`
    -   If no instance of the class name exists for the `id`, an error message:`** no instance found **` will be displayed.
-   `all`: Prints all string representation of all instances based or not on the class name. Run this command: `$ all BaseModel` or `$ all`.
	- example output:
 ```(hbnb) all```
```["[User] (b12-12-12-12) {'id': 'b12-12-12-12', 'created_at': datetime.datetime(2023, 8, 12, 22, 22, 51, 660748), 'updated_at': datetime.datetime(2023, 8, 12, 22, 22, 51, 660767)}"]```


-   `update`: Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
    -   Usage: `update <class name> <id> <attribute name> "<attribute value>"`
    -   Only one attribute can be updated at a time
    - example output:
	    - before updating:
```(hbnb) all User```
```["[User] (b12-12-12-12) {'id': 'b12-12-12-12', 'created_at': datetime.datetime(2023, 8, 12, 22, 22, 51, 660748), 'updated_at': datetime.datetime(2023, 8, 12, 22, 22, 51, 660767)}"]```
		- after updating( I ran this command:  `update User b12-12-12-12 email "aibnb@mail.com"`):
	```(hbnb) all User```
	```["[User] (b12-12-12-12) {'id': 'b12-12-12-12', 'created_at': datetime.datetime(2023, 8, 12, 22, 22, 51, 660748), 'updated_at': datetime.datetime(2023, 8, 12, 22, 29, 15, 591041), 'email': 'aibnb@mail.com'}"]```
			- As you can see, the time that I updated the class also reflected in the `updated_at` key in the instance representation.


