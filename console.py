#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import re
import json
from models import file_storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
import cmd

current_classes = {'BaseModel': BaseModel, 'User': User,
                   'Amenity': Amenity, 'City': City, 'State': State,
                   'Place': Place, 'Review': Review}

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the project"""

    prompt = "(hbnb) "
    file = None

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_help(self, line):
        """Updated help command to list all available commands"""
        cmd.Cmd.do_help(self, line)

    def emptyline(self):
        """Empty line shouldn't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
