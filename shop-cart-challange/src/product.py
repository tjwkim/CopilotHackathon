from pydantic import BaseModel
from typing import List, Dict

class Product(BaseModel):
    id: int
    name: str
    description: str
    image_url: str
    price: float
    manufacturer: str
    model_compatibility: List[str]
    part_number: str
    stock: int
    specifications: Dict[str, str]