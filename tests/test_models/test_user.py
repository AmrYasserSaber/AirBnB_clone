import time
import unittest
from datetime import datetime
from models.user import User


class TestUserModel(unittest.TestCase):
    def test_init(self):
        model = User()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.email, "")
        self.assertEqual(model.password, "")
        self.assertEqual(model.first_name, "")
        self.assertEqual(model.last_name, "")

    def test_str(self):
        model = User()
        str_representation = str(model)
        self.assertIn("User", str_representation)
        self.assertIn(model.id, str_representation)

    def test_save(self):
        model = User()
        original_updated_at = model.updated_at

        # Introduce a small delay to ensure the updated_at value changes
        time.sleep(1)  # Sleep for 1 second
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        model = User()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['email'], "")
        self.assertEqual(model_dict['password'], "")
        self.assertEqual(model_dict['first_name'], "")
        self.assertEqual(model_dict['last_name'], "")
        self.assertEqual(model_dict['__class__'], "User")
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIsInstance(model_dict['id'], str)
        self.assertIsInstance(model_dict['created_at'], str)
