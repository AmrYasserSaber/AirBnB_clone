import json
from os import path


"""
File Storage: this is a file storage class that used to
store all file object as a json object
"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            return the object that contains all other object stored in it.
        """
        return self.__objects

    def new(self, obj):
        """
            save a new object
        """
        key = f"{obj.__class__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
            Make a seralize for object
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            data = {key: value.to_dict()
                    for key, value in self.__objects.items()}
            print(data)
            json.dump(data, f)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """
        if path.exists(self.__file_path) is True:

            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for obj in data.values():
                    cls = obj["__class__"]
                    self.new(eval(cls)(**obj))
