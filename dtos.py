from pydantic import BaseModel

class Product(BaseModel):
    name:str
    price:float=0
    category:str
    rating:float = 0
    stock:int = 0