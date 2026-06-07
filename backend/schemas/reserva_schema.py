from pydantic import BaseModel
from datetime import date, time


class ReservaCrear(BaseModel):
    id_usuario: int
    id_pista: int
    fecha: date
    hora_inicio: time
    hora_fin: time