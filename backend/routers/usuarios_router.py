from fastapi import APIRouter
from schemas.usuario_schema import UsuarioCrear
from repositorios.usuarios_repositorio import (
    obtener_todos_los_usuarios,
    obtener_usuario_por_id,
    crear_usuario
)

router = APIRouter()

@router.get("/usuarios")
def listar_usuarios():
    return obtener_todos_los_usuarios()

@router.get("/usuarios/{id_usuario}")
def obtener_usuario(id_usuario: int):
    usuario = obtener_usuario_por_id(id_usuario)

    if usuario is None:
        return {"error": "Usuario no encontrado"}

    return usuario

@router.post("/usuarios")
def crear_nuevo_usuario(usuario: UsuarioCrear):
    return crear_usuario(usuario)