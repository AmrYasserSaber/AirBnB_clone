#!/usr/bin/env python3
"""
    implement of console file that manage all my action in this project
"""


import cmd
import sys
import json
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
        "create an instance of a passed class"
        if not model_name:
            print("** class name missing **")
        elif model_name not in my_models.keys():
            print("** class doesn't exist **")
        else:
            new_instance = my_models[model_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg=None):
        "Show the string implementation of the class"
        storage.reload()
        all_model = storage.all()
        class_name_id = arg.split(" ")
        
    
        # print("start", id, class_name)
        if  len(class_name_id) == 0:
            print("** class name missing **")
        elif class_name_id[0] not in my_models.keys():
            print("** class doesn't exist **")
        elif len(class_name_id) > 2:
            print("** instance id missing **")
        # else:
        #     key = class_name + " '>."+id
        #     print(key)
        #     print(all_model.keys())
        #     if key in all_model.keys():
        #         obj = str(all_model[key])
        #         print(obj)
        #     else:
        #         print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
