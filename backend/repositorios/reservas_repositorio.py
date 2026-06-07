from sqlalchemy import text
from database import engine
from datetime import time


def obtener_todas_las_reservas():
    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT
                    IdReserva,
                    IdUsuario,
                    IdPista,
                    Fecha,
                    HoraInicio,
                    HoraFin,
                    Estado,
                    FechaCreacion
                FROM Reservas
            """)
        )

        reservas = []

        for fila in result:
            reservas.append({
                "id_reserva": fila.IdReserva,
                "id_usuario": fila.IdUsuario,
                "id_pista": fila.IdPista,
                "fecha": str(fila.Fecha),
                "hora_inicio": str(fila.HoraInicio),
                "hora_fin": str(fila.HoraFin),
                "estado": fila.Estado,
                "fecha_creacion": str(fila.FechaCreacion)
            })

        return reservas



def obtener_reserva_por_id(id_reserva):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT
                    IdReserva,
                    IdUsuario,
                    IdPista,
                    Fecha,
                    HoraInicio,
                    HoraFin,
                    Estado,
                    FechaCreacion
                FROM Reservas
                WHERE IdReserva = :id
            """),
            {"id": id_reserva}
        )

        fila = result.fetchone()

        if fila is None:
            return None

        return {
            "id_reserva": fila.IdReserva,
            "id_usuario": fila.IdUsuario,
            "id_pista": fila.IdPista,
            "fecha": str(fila.Fecha),
            "hora_inicio": str(fila.HoraInicio),
            "hora_fin": str(fila.HoraFin),
            "estado": fila.Estado,
            "fecha_creacion": str(fila.FechaCreacion)
        }



def crear_reserva(reserva):
    with engine.connect() as conn:

        # Validar que existe el usuario
        # Se busca en la tabla usuarios si existe el id de usuario
        
        usuario_existe = conn.execute(
            text("""
                SELECT COUNT(*)
                FROM Usuarios
                WHERE IdUsuario = :id_usuario
            """),
            {
                "id_usuario": reserva.id_usuario
            }
        ).scalar()

        if usuario_existe == 0:
            return {
                "error": "El usuario no existe"
            }

        # Validar que la reserva este dentro del horario
        # Rango horario: 10:00 a 21:00

        if reserva.hora_inicio < time(10, 0):
            return {
            "error": "La pista abre a las 10:00"
        }

        if reserva.hora_fin > time(21, 0):
            return {
                "error": "La pista cierra a las 21:00"
            }

        # Validar que no exista una reserva para ese horario
        # Se tiene en cuenta que no haya superposicion de horarios

        conflicto = conn.execute(
            text("""
                SELECT COUNT(*)
                FROM Reservas
                WHERE IdPista = :id_pista
                AND Fecha = :fecha
                AND HoraInicio < :hora_fin
                AND HoraFin > :hora_inicio
            """),
            {
                "id_pista": reserva.id_pista,
                "fecha": reserva.fecha,
                "hora_inicio": reserva.hora_inicio,
                "hora_fin": reserva.hora_fin
            }
        ).scalar()

        if conflicto > 0:
            return {
                "error": "Ya existe una reserva para ese horario"
            }

        # Crear la reserva
        # Se asume que las fechas y horas son validas, ya que fueron validadas en el schema

        conn.execute(
            text("""
                INSERT INTO Reservas
                (
                    IdUsuario,
                    IdPista,
                    Fecha,
                    HoraInicio,
                    HoraFin
                )
                VALUES
                (
                    :id_usuario,
                    :id_pista,
                    :fecha,
                    :hora_inicio,
                    :hora_fin
                )
            """),
            {
                "id_usuario": reserva.id_usuario,
                "id_pista": reserva.id_pista,
                "fecha": reserva.fecha,
                "hora_inicio": reserva.hora_inicio,
                "hora_fin": reserva.hora_fin
            }
        )

        conn.commit()

        return {
            "mensaje": "Reserva creada correctamente"
        }

