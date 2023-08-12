#!/usr/bin/python3
""" This module contains a class HBNBCommand """
import cmd
import shlex
import sys
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

    def do_quit(self, line):
        """Quits if the user types in quit or crtl+D(EOF)\n"""
        return True

    def do_EOF(self, line):
        """Quits the program\n"""
        return True

    def emptyline(self):
        """Does nothing when Enter is pressed on emptyline"""
        pass

    def do_create(self, name):
        """Creates a new instance of BaseModel, saves it to a JSON file
        and prints the id
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
        """ Deletes an instance """
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
        print can be specified by passing the name of the instance """
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
        updating an attribute and saves the changes """
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
        storage.save()
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
