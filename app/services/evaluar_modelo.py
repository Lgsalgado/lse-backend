
import os
import json
from app.services.inferencia import procesar_video

# Directorio donde están los videos a evaluar
EVALUATION_DIR = "evaluacion_videos/"
# Archivo donde se guardará el reporte de resultados
RESULTADOS_PATH = "evaluacion_resultados.json"

# Diccionario para almacenar resultados
resultados = []

# Evaluar todos los archivos .mp4 en la carpeta
for archivo in os.listdir(EVALUATION_DIR):
    if archivo.endswith(".mp4"):
        ruta_video = os.path.join(EVALUATION_DIR, archivo)

        # Suponemos que el nombre del archivo indica la frase esperada (ej: buenos_dias_01.mp4)
        esperado = archivo.split("_")[0]  # puedes mejorar esto si usas otro formato

        predicho = procesar_video(ruta_video)

        resultado = {
            "video": archivo,
            "esperado": esperado,
            "predicho": predicho,
            "acierto": esperado.lower() == predicho.lower()
        }

        print(f"✔ Evaluado: {archivo} → Esperado: {esperado}, Predicho: {predicho}")
        resultados.append(resultado)

# Guardar resultados en JSON
with open(RESULTADOS_PATH, "w") as f:
    json.dump(resultados, f, indent=2)

print(f"📄 Evaluación completada. Resultados guardados en: {RESULTADOS_PATH}")
