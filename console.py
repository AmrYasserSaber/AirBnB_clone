#!/usr/bin/env python3
import cmd, sys
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    doc_header = """
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb)
    """
    def postcmd(self, stop, line):
        print()
    def do_exit(self, line):
        'Exit'
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()