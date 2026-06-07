from fastapi import APIRouter
from schemas.reserva_schema import ReservaCrear
from repositorios.reservas_repositorio import (
    obtener_todas_las_reservas,
    obtener_reserva_por_id,
    crear_reserva,
    obtener_disponibilidad
)

router = APIRouter()

@router.get("/reservas")
def listar_reservas():
    return obtener_todas_las_reservas()


@router.get("/reservas/{id_reserva}")
def obtener_reserva(id_reserva: int):
    reserva = obtener_reserva_por_id(id_reserva)

    if reserva is None:
        return {"error": "Reserva no encontrada"}

    return reserva


@router.post("/reservas")
def crear_nueva_reserva(reserva: ReservaCrear):
    return crear_reserva(reserva)


@router.get("/disponibilidad")
def disponibilidad(fecha: str, id_pista: int):
    return obtener_disponibilidad(fecha, id_pista)