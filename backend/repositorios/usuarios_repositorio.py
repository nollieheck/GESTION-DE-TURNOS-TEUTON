from sqlalchemy import text
from database import engine


def obtener_cantidad_usuarios():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT COUNT(*) FROM Usuarios")
        )

        return result.scalar()


def obtener_todos_los_usuarios():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT
                    IdUsuario,
                    Nombre,
                    Apellido,
                    Email
                FROM Usuarios
            """)
        )

        usuarios = []

        for fila in result:
            usuarios.append({
                "id": fila.IdUsuario,
                "nombre": fila.Nombre,
                "apellido": fila.Apellido,
                "email": fila.Email
            })

        return usuarios


def obtener_usuario_por_id(id_usuario):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT
                    IdUsuario,
                    Nombre,
                    Apellido,
                    Email
                FROM Usuarios
                WHERE IdUsuario = :id
            """),
            {"id": id_usuario}
        )

        fila = result.fetchone()

        if fila is None:
            return None

        return {
            "id": fila.IdUsuario,
            "nombre": fila.Nombre,
            "apellido": fila.Apellido,
            "email": fila.Email
        }

# Crear un usuario commiteando 

def crear_usuario(usuario):
    with engine.connect() as conn:

        conn.execute(
            text("""
                INSERT INTO Usuarios
                (
                    Nombre,
                    Apellido,
                    DNI,
                    Telefono,
                    Email
                )
                VALUES
                (
                    :nombre,
                    :apellido,
                    :dni,
                    :telefono,
                    :email
                )
            """),
            {
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "dni": usuario.dni,
                "telefono": usuario.telefono,
                "email": usuario.email
            }
        )

        conn.commit() # to much

        return {
            "mensaje": "Usuario creado correctamente"
        }

