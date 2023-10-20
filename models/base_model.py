#!/usr/bin/python3
from datetime import datetime
import uuid
import models


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """used to create the object and to covert dict to its obj"""

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self,
                            key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))

                elif key != "__class__":
                    setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    """should be called when any change occurred to the obj """

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    """updating __dict__"""

    def to_dict(self):
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__

        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()

        return dict
