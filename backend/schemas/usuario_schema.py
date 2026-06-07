from pydantic import BaseModel


class UsuarioCrear(BaseModel):
    nombre: str
    apellido: str
    dni: str
    telefono: str
    email: str