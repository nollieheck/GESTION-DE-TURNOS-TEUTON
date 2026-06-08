from fastapi import FastAPI
from database import test_connection

from repositorios.usuarios_repositorio import (
    obtener_cantidad_usuarios,
    obtener_todos_los_usuarios
)

from repositorios.reservas_repositorio import obtener_todas_las_reservas

from routers.usuarios_router import router as usuarios_router
from routers.reservas_router import router as reservas_router
from routers.pistas_router import router as pistas_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios_router)
app.include_router(reservas_router)
app.include_router(pistas_router)

@app.get("/")
def inicio():
    return {"mensaje": "Prueba API funcionando"}

@app.get("/test-db")
def test_db():
    cantidad = obtener_cantidad_usuarios()
    return {"usuarios": cantidad}
