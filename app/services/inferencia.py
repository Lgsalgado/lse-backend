import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp
import os

# Cargar modelo entrenado
modelo = tf.keras.models.load_model("app/services/modelo_lse.h5")

# Cargar las clases desde archivo externo
def cargar_clases(path="app/services/clases.txt"):
    if not os.path.exists(path):
        return ["Clase_desconocida"]
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]

frases = cargar_clases()

# Procesamiento de video y predicción de la seña
def procesar_video(video_path):
    mp_hands = mp.solutions.hands
    manos = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret or frame_count >= 30:
            break

        frame = cv2.resize(frame, (64, 64))  # Normalizar tamaño
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = manos.process(frame_rgb)

        if results.multi_hand_landmarks:
            frames.append(frame)
            frame_count += 1

    cap.release()
    manos.close()

    if len(frames) < 30:
        return "No se detectaron suficientes señas claras en el video."

    entrada = np.array(frames[:30]) / 255.0
    entrada = entrada.reshape(1, 30, 64, 64, 3)

    pred = modelo.predict(entrada)
    clase = np.argmax(pred)

    return frases[clase] if clase < len(frases) else "Clase no reconocida"
