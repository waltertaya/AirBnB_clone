from models.base_model import BaseModel


class Review(BaseModel):
    """Class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
