from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
