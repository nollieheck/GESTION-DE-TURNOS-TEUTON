from sqlalchemy import create_engine, text

SERVER = "DESKTOP-QPBN81K"
DATABASE = "Prueba"

connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM Usuarios"))
        return result.scalar()