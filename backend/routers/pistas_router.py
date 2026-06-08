from fastapi import APIRouter

from repositorios.pistas_repositorio import (
    obtener_todas_las_pistas
)

from schemas.pistas_schema import (
    PistaResponse
)

router = APIRouter(
    prefix="/pistas",
    tags=["Pistas"]
)


@router.get(
    "",
    response_model=list[PistaResponse]
)
def listar_pistas():

    return obtener_todas_las_pistas()