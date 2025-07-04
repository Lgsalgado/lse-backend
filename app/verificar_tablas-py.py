from sqlalchemy import inspect
from app.database import engine

inspector = inspect(engine)
tablas = inspector.get_table_names()

print("Tablas encontradas en la base de datos:")
for tabla in tablas:
    print(f"- {tabla}")
