#!/usr/bin/env python3
"""
    implement of console file that manage all my action in this project
"""


import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage
import shlex


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

    def do_show(self, args=None):
        "Show the string implementation of the class"
        storage.reload()
        all_model = storage.all()
        class_name_id = shlex.split(args)
        # print(class_name_id)
        # print(all_model)

        if len(class_name_id) == 0:
            print("** class name missing **")
        elif class_name_id[0] not in my_models.keys():
            print("** class doesn't exist **")
        elif len(class_name_id) < 2:
            print("** instance id missing **")
        else:
            curr_key = f"{class_name_id[0]}'>.{class_name_id[1]}"
            # print(key)
            # print(all_model.keys())
            # print("#" * 50)
            check = True
            for key in all_model.keys():
                if curr_key in key:
                    print(all_model[key])
                    check = False
                    break
            if check:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)."""
        storage.reload()
        all_model = storage.all()
        class_name_id = shlex.split(args)


        if len(class_name_id) == 0:
            print("** class name missing **")
        elif class_name_id[0] not in my_models.keys():
            print("** class doesn't exist **")
        elif len(class_name_id) < 2:
            print("** instance id missing **")
        else:
            key = f"{class_name_id[0]}.{class_name_id[1]}"
            check = True
            if key in all_model:
                del all_model[key]
                storage.save()
                check = False
            if check:
                print("** no instance found **")

    def do_all(self, model_name):
        storage.reload()
        models = storage.all()
        check = False

        for key in models.keys():
            if model_name in key:
                check = True
        if check:
            for key in models:
                print(models[key])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""
        storage.reload()
        all_model = storage.all()
        class_name_id = shlex.split(args)

        if len(class_name_id) == 0:
            print("** class name missing **")
        elif class_name_id[0] not in all_model.keys():
            print("** class doesn't exist **")
        elif len(class_name_id) < 2:
            print("** instance id missing **")
        else:
            curr_key = f"{class_name_id[0]}.{class_name_id[1]}"
            check = True
            for key in all_model.keys():
                if curr_key in key:
                    check = False
            if check:
                print("** no instance found **")
            elif len(class_name_id) < 3:
                print("** attribute name missing **")
            elif len(class_name_id) < 4:
                print("** value missing **")


