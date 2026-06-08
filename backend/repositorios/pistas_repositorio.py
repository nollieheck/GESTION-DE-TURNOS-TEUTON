from sqlalchemy import text
from database import engine


def obtener_todas_las_pistas():

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT
                    IdPista,
                    Nombre,
                    Activa
                FROM Pistas
            """)
        )

        pistas = []

        for fila in result:

            pistas.append({
                "id": fila.IdPista,
                "nombre": fila.Nombre,
                "activa": fila.Activa
            })

        return pistas