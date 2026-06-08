from pydantic import BaseModel


class PistaResponse(BaseModel):
    id: int
    nombre: str
    activa: bool