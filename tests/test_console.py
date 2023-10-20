import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def test_do_show(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **\n",
                             mock_stdout.getvalue())

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show InvalidClassName")
            self.assertEqual("** class doesn't exist **\n",
                             mock_stdout.getvalue())

        # You can add more test cases here for valid "show" commands.

    def test_do_destroy(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             mock_stdout.getvalue())

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("destroy InvalidClassName")
            self.assertEqual("** class doesn't exist **\n",
                             mock_stdout.getvalue())

        # You can add more test cases here for valid "destroy" commands.

    def test_do_all(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("all")
            self.assertEqual("** class doesn't exist **\n",
                             mock_stdout.getvalue())

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("all InvalidClassName")
            self.assertEqual("** class doesn't exist **\n",
                             mock_stdout.getvalue())

        # You can add more test cases here for valid "all" commands.

    def test_do_update(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update")
            self.assertEqual("** class name missing **\n",
                             mock_stdout.getvalue())

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("update InvalidClassName")
            self.assertEqual("** class doesn't exist **\n",
                             mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
