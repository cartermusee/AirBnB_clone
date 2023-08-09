#!/usr/bin/python3
""" This module contains a class HBNBCommand """
import cmd
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

    prompt = "(hbnb) "
    classes = ["User", "Amenity", "BaseModel", "City", "Place", "Review", "State"]

    def do_quit(self, line):
        """Quits if the user types in quit or crtl+D(EOF)\n"""
        return True

    def do_EOF(self, line):
        """Quits the program\n"""
        return True

    def emptyline(self):
        """Does nothing when Enter is pressed on emptyline"""
        pass

    def do_create(self, name=None):
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
        storage.save()

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

    def do_all(self, name=None):
        """ Prints string representation of all instances, an instance to
        print can be specified by passing the name of the instance """
        dict_all = storage.all()

        if name is not None or name != "":
            if name not in self.classes:
                print("** class doesn't exist **")

            if name is not None:
                if name in dict_all:
                    inst = []
                    if dict_all[name]:
                        inst.append(str(dict_all[name]))
                        print(inst)
            else:
                inst = []
                inst.append(str(dict_all))
                print(inst)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
