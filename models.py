from pydantic import BaseModel
from typing import List

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

class Pedido(BaseModel):
    id: int
    usuario_id: int
    productos: List[int]
