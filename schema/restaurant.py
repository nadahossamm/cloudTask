from pydantic import BaseModel


class Restaurant(BaseModel):
    name: str
    type: str
    location: str

