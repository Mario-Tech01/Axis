# test_db.py
from sqlalchemy import text
from axis.infraestructure.database.connection import SessionLocal

def test_connection():
    print("🔄 Intentando conectar a la base de datos...")
    session = SessionLocal()
    try:
        # Ejecutamos una consulta de control nativa muy simple
        resultado = session.execute(text("SELECT 1")).scalar()
        if resultado == 1:
            print("✅ ¡Conexión exitosa! El proyecto se comunica con PostgreSQL perfectamente.")
    except Exception as e:
        print("❌ Error de conexión. Revisa tus credenciales en el .env")
        print(f"Detalle del error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    test_connection()