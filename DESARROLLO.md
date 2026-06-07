1. Crear carpeta del proyecto.
2. Crear entorno virtual (venv).
3. Activar entorno virtual.
4. Instalar dependencias:
   - fastapi
   - uvicorn
   - sqlalchemy
   - pyodbc
   - python-dotenv
5. Crear main.py con un endpoint de prueba.

(aca empezamos a usar los esquemas de datos, para validarlos)
Para crear una reserva se tiene en cuenta:
Verificar que exista el usuario.
Verificar que exista la pista.
Verificar que la pista esté activa.
Verificar que el horario esté dentro de:
10:00 - 21:00
Verificar que no exista otra reserva superpuesta.

