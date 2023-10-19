#!/usr/bin/env python3
"""
    implement of console file that manage all my action in this project
"""


import cmd
import sys
from models.base_model import BaseModel
from models import storage


my_models = {"BaseModel": BaseModel}
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    doc_header = """Documented commands (type help <topic>):"""

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "Quit command to exit the program"
        return True

    def postloop(self):
        "print new line after each command"
        print("")

    def emptyline(self):
        "over Write one empty line method"
        pass
    def do_create(self, model_name):
        if not model_name:
            print("** class name missing **")
        elif model_name not in my_models.keys():
            print("** class doesn't exist **")
        else:
            new_instance = my_models[model_name]()
            new_instance.save()
            print(new_instance.id)
    






if __name__ == '__main__':
    HBNBCommand().cmdloop()
