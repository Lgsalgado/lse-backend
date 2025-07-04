from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import procesar_router

app = FastAPI()

# Orígenes permitidos (ajusta según tu entorno)
origins = [
    "http://localhost:63343",  # JetBrains IDE
    "http://127.0.0.1:63343",
    # Puedes agregar más orígenes si lo necesitas
]

# Configurar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # Puedes usar ["*"] si es solo desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers
app.include_router(procesar_router.router, prefix="/api")

@app.get("/")
def root():
    return {"mensaje": "API de reconocimiento de LSE funcionando"}
