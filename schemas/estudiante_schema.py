from typing import Optional
from pydantic import BaseModel


class EstudianteSchema(BaseModel):
    id: Optional[int]
    cedula: str
    nombre: str
    apellido: str
    edad: int
    email: str
    genero: str
