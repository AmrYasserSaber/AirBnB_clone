from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.__dict__)
