from fastapi import APIRouter, UploadFile, File
from app.services.inferencia import procesar_video
import shutil
import os

router = APIRouter()

@router.post("/procesar")
async def procesar_senia(file: UploadFile = File(...)):
    video_path = f"temp_video_{file.filename}"
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resultado = procesar_video(video_path)

    # Eliminar el archivo temporal después de usarlo
    os.remove(video_path)

    return {"traduccion": resultado}
