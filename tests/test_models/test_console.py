import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """
        Test the 'create' command of HBNBCommand.
        """
        cmd = HBNBCommand()

        # Test case 1: Missing class name
        cmd.onecmd("create")
        self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

        # Test case 2: Non-existing class name
        cmd.onecmd("create MyModel")
        self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

        # Test case 3: Create an instance and check the ID
        cmd.onecmd("create BaseModel")
        output = mock_stdout.getvalue()
        self.assertTrue(len(output) == 36)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """
        Test the 'show' command of HBNBCommand.
        """
        cmd = HBNBCommand()

        # Test case 1: Missing class name
        cmd.onecmd("show")
        self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

        # Test case 2: Non-existing class name
        cmd.onecmd("show MyModel")
        self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

        # Test case 3: Missing instance id
        cmd.onecmd("show BaseModel")
        self.assertEqual("** instance id missing **\n", mock_stdout.getvalue())

        # Test case 4: Non-existing instance id
        cmd.onecmd("show BaseModel 1234")
        self.assertEqual("** no instance found **\n", mock_stdout.getvalue())

        # Test case 5: Show an existing instance (assuming an instance with id 'test_id' exists)
        cmd.onecmd("show BaseModel test_id")
        output = mock_stdout.getvalue()
        self.assertTrue(output.startswith("[BaseModel] (test_id)"))


if __name__ == '__main__':
    unittest.main()
