#!/usr/bin/python3
""" This module contains a class HBNBCommand """
import cmd
import shlex
import sys
import json
import re
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """This initializes a class HBNBCommand"""
    if sys.__stdin__.isatty():
        prompt = "(hbnb) "
    else:
        prompt = ""

    classes = ["User", "Amenity", "BaseModel", "City", "Place", "Review",
               "State"]

    def preloop(self):
        """ Prints starting prompt in non-interactive mode """
        if not sys.__stdin__.isatty():
            print("(hbnb)")

    def postloop(self):
        """ Prints stopping prompt in non-interactive mode """
        if not sys.__stdin__.isatty():
            # moves the cursor up one line
            sys.stdout.write("\033[F")
            # flushes buffer to ensure that cursor moved
            sys.stdout.flush()
            print("(hbnb)")

    def default(self, line):
        """ Handles function calls """
        try:
            args = line.split("(")
        except Exception:
            super().default(line)
        if len(args) == 2:
            namefunc = args[0]
            id = args[1].strip("')\"")

            if "." in namefunc and namefunc.split(".")[1] == "destroy":
                name = namefunc.split(".")[0]

                if name not in self.classes:
                    print("** class doesn't exist **")
                    return
                self.do_destroy(name + " " + id)

            elif "." in namefunc and namefunc.split(".")[1] == "show":
                name = namefunc.split(".")[0]
                if name not in self.classes:
                    print("** class doesn't exist **")
                    return
                self.do_show(name + " " + id)

        elif len(args) == 3:
            namefunc = args[0]
            id_attr_value = args[1].strip(')')
            if "." in namefunc and namefunc.split(".")[1] == "update":
                name = namefunc.split(".")[0]
                id, attr, value = shlex.split(id_attr_value)
                if value.startswith('{') and value.endswith('}'):
                    value = json.loads(value)
                self.do_update(f"{name} {id} {attr} '{value}'")
        else:
            super().default(line)

    def do_quit(self, line):
        """Quits if the user types in quit or crtl+D(EOF)
        arg:
            line:arg passed eg quit"""
        return True

    def do_EOF(self, line):
        """Quits the program
        arg:
            line:argument pass to cmd"""
        return True

    def emptyline(self):
        """Does nothing when Enter is pressed on emptyline"""
        pass

    def do_create(self, name):
        """Creates a new instance of BaseModel, saves it to a JSON file
        and prints the id
        arg:
            name:name passed to create
        """
        if name == "" or name is None:
            print("** class name missing **")
            return
        elif name not in self.classes:
            print("** class doesn't exist **")
            return

        if name == "User":
            name = User()
        elif name == "Amenity":
            name = Amenity()
        elif name == "City":
            name = City()
        elif name == "Place":
            name = Place()
        elif name == "Review":
            name = Review()
        elif name == "State":
            name = State()
        else:
            name = BaseModel()
        storage.save()
        print(name.id)

    def do_show(self, nameid=None):
        """Prints the string representation of an instance based on class
        name and id
        arg:
            nameid:name of claa passed
        """
        if nameid == "" or nameid is None:
            print("** class name missing **")
            return

        if " " not in nameid and nameid not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            name, id = nameid.split(" ")

        except Exception:
            print("** instance id missing **")
            return

        if name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{name}.{id}"
        dict_all = storage.all()

        if key not in dict_all:
            print("** no instance found **")
            return
        else:
            instance = dict_all[key]
            print(instance)

    def do_destroy(self, nameid=None):
        """ Deletes an instance
        arg:
            nameid:name passed as para"""
        if nameid == "" or nameid is None:
            print("** class name missing **")
            return

        if " " not in nameid and nameid not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            name, id = nameid.split(" ")

        except Exception:
            print("** instance id missing **")
            return

        if name not in self.classes:
            print("** class doesn't exist **")
            return

        key = f"{name}.{id}"
        dict_all = storage.all()

        if key not in dict_all:
            print("** no instance found **")
            return
        else:
            del dict_all[key]
            storage.save()
            return

    def do_all(self, name):
        """ Prints string representation of all instances, an instance to
        print can be specified by passing the name of the instance
        arg:
            name:name passed as parameter"""
        dict_all = storage.all()
        if not name:
            instances = [str(obj) for obj in dict_all.values()]
            print(instances)

        else:
            namecls = name.split()
            if namecls[0] not in self.classes:
                print("** class doesn't exist **")
                return

            instances = [str(obj) for obj in dict_all.values()
                         if obj.__class__.__name__ == namecls[0]]
            print(instances)

    def do_update(self, arg):
        """ Updates an instance based on class name and id by adding or
        updating an attribute and saves the changes
        args:
            arg:the name passed"""
        dict_all = storage.all()
        if not arg or arg == "":
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if args[0] == "":
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2 or args[1] == "":
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in dict_all:
            print("** no instance found **")
            return

        elif len(args) < 3 or args[2] == "":
            print("** attribute name missing **")
            return
        elif len(args) < 4 or args[3] == "":
            print("** value missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in dict_all:
            print("** no instance found **")
            return

        instance = dict_all[key]
        setattr(instance, args[2], args[3])
        BaseModel.save(instance)
        storage.save()
        return

    def default(self, name):
        """is used handle a case where users enter <class_name>.method
        arg:
            name:name of class"""
        try:
            namecls = name.split(".")
            if len(namecls) == 2 and namecls[1] == "all()":
                self.do_all(namecls[0])
            if len(namecls) == 2 and namecls[1] == "count()":
                self.do_count(namecls[0])
        except Exception:
            super().default(name)

        try:
            args = name.split("(")
        except Exception:
            super().default(name)
        if len(args) == 2:
            namefunc = args[0]
            id = args[1].strip("')\"")

            if "." in namefunc and namefunc.split(".")[1] == "destroy":
                name = namefunc.split(".")[0]

                if name not in self.classes:
                    print("** class doesn't exist **")
                    return
                self.do_destroy(name + " " + id)

            elif "." in namefunc and namefunc.split(".")[1] == "show":
                name = namefunc.split(".")[0]
                if name not in self.classes:
                    print("** class doesn't exist **")
                    return
                self.do_show(name + " " + id)

        else:
            namefunc = args[0]
            id = args[1].strip("')\"")

            if "." in namefunc and namefunc.split(".")[1] == "update":
                name = namefunc.split(".")[0]
                id_attr_value = args[2]
                if id_attr_value[-1] == ',':
                    id_attr_value = id_attr_value[:-1]
                id_attr_value = id_attr_value.strip()

                if name not in self.classes:
                    print("** class doesn't exist **")
                    return
                self.do_update(f"{name} {id} {id_attr_value}")

    def do_count(self, name):
        """Update your command interpreter (console.py) to
        retrieve the number of instances of a
        class: <class name>.count()
        arg:
            name:name of class"""
        if not name or name == "":
            print("** class name missing **")
            return
        if name not in self.classes:
            print("** class doesn't exist **")
            return
        count = 0
        for value in storage.all().values():
            if value.__class__.__name__ == name:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
