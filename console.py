#!/usr/bin/env python3
import cmd
import sys

"""
    implement of console file that manage all my action in this project
"""


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
        print("")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
