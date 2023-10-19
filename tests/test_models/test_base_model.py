import time
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.my_number, 89)
        self.assertEqual(model.name, "My First Model")

    def test_str(self):
        model = BaseModel()
        str_representation = str(model)
        self.assertIn("BaseModel", str_representation)
        self.assertIn(model.id, str_representation)

    def test_save(self):
        model = BaseModel()
        original_updated_at = model.updated_at

        # Introduce a small delay to ensure the updated_at value changes
        time.sleep(1)  # Sleep for 1 second
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['my_number'], 89)
        self.assertEqual(model_dict['name'], "My First Model")
        self.assertEqual(model_dict['__class__'], "BaseModel")
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIsInstance(model_dict['id'], str)
        self.assertIsInstance(model_dict['created_at'], str)


if __name__ == '__main__':
    unittest.main()
