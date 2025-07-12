import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp
import time
import os

# Cargar modelo y clases
modelo = tf.keras.models.load_model("app/services/modelo_lse.h5")

with open("app/services/clases.txt", "r") as f:
    clases = [line.strip() for line in f.readlines()]

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
manos = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

# Inicializar cámara
cap = cv2.VideoCapture(0)

frames = []
frame_buffer = 30  # cantidad de frames por predicción

print("🎥 Iniciando reconocimiento en tiempo real... Presiona Q para salir.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    imagen = cv2.flip(frame, 1)
    img_resized = cv2.resize(imagen, (64, 64))
    rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
    resultado = manos.process(rgb)

    if resultado.multi_hand_landmarks:
        frames.append(img_resized)

        # Si acumulamos 30 frames, predecimos
        if len(frames) == frame_buffer:
            entrada = np.array(frames) / 255.0
            entrada = entrada.reshape(1, 30, 64, 64, 3)
            pred = modelo.predict(entrada)
            clase = np.argmax(pred)
            frase = clases[clase]

            cv2.putText(imagen, f"Frase: {frase}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            frames = []  # reiniciar buffer
    else:
        frames = []

    cv2.imshow("Traducción de Señas - LSE", imagen)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
