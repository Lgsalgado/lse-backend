from app.database import engine
from app.models import models

print("Creando las tablas en la base de datos...")

# Esto crea todas las tablas definidas en models.py
models.Base.metadata.create_all(bind=engine)

print("¡Tablas creadas exitosamente!")
