from fastapi import APIRouter, UploadFile, File
from app.services.inferencia import procesar_video
import shutil
import os
from datetime import datetime

router = APIRouter()

@router.post("/procesar")
async def procesar_senia(file: UploadFile = File(...)):
    # Generar nombre único con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    original_name = file.filename.rsplit(".", 1)[0]  # sin extensión
    extension = file.filename.rsplit(".", 1)[-1]
    temp_path = f"temp_video_{timestamp}.{extension}"
    eval_dir = "evaluacion_videos"
    eval_filename = f"{original_name}_{timestamp}.{extension}"
    eval_path = os.path.join(eval_dir, eval_filename)

    # Asegurar que exista el directorio de evaluación
    os.makedirs(eval_dir, exist_ok=True)

    # Guardar archivo temporal y copia para evaluación
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    shutil.copy(temp_path, eval_path)

    # Procesar el video con el modelo
    resultado = procesar_video(temp_path)

    # Eliminar el archivo temporal después de usarlo
    os.remove(temp_path)

    return {"traduccion": resultado}
