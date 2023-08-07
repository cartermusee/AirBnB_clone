# 0x00. AirBnB clone - The console

This project is a console for the AirBnB clone.

### Cmd commands:
-   `create`: Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`.
- Execute this command: `create BaseModel`
    -   If the class name is missing, it prints `** class name missing **`
    -   If the class name doesn’t exist, it prints `** class doesn't exist **`


-   `show`: Prints the string representation of an instance based on the class name and `id`.
- Ex: `$ show BaseModel 1234-1234-1234`.
    -   If the class name is missing, it prints `** class name missing **`
    -   If the class name doesn’t exist, it prints `** class doesn't exist **` (ex: `$ show MyModel`)
    -   If the `id` is missing, print `** instance id missing **` (ex: `$ show BaseModel`)
    -   If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ show BaseModel 121212`)
-   `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file). Ex: `$ destroy BaseModel 1234-1234-1234`.
    -   If the class name is missing, print `** class name missing **` (ex: `$ destroy`)
    -   If the class name doesn’t exist, print `** class doesn't exist ** (ex:`$ destroy MyModel`)`
    -   If the `id` is missing, print `** instance id missing **` (ex: `$ destroy BaseModel`)
    -   If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `$ destroy BaseModel 121212`)
-   `all`: Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` or `$ all`.
    -   The printed result must be a list of strings (like the example below)
    -   If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ all MyModel`)
-   `update`: Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
    -   Usage: `update <class name> <id> <attribute name> "<attribute value>"`
    -   Only one attribute can be updated at a time

    -   The attribute value must be casted to the attribute type
    -   If the class name is missing, print `** class name missing **` (ex: `$ update`)
    -   If the class name doesn’t exist, it prints `** class doesn't exist **` (ex: `$ update MyModel`)
    -   If the `id` is missing, it prints `** instance id missing **` (ex: `$ update BaseModel`)
    -   If the instance of the class name doesn’t exist for the `id`, it prints `** no instance found **` (ex: `$ update BaseModel 121212`)
    -   If the attribute name is missing, it prints `** attribute name missing **` (ex: `$ update BaseModel existing-id`)
    -   If the value for the attribute name doesn’t exist, it prints `** value missing **` (ex: `$ update BaseModel existing-id first_name`)
    -   All other arguments should not be used (Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"` = `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`)

