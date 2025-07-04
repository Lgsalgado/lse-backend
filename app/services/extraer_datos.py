import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

def cargar_datos_desde_videos(ruta_dataset, max_frames=30, img_size=64):
    X, y = [], []
    etiquetas = sorted(os.listdir(ruta_dataset))
    etiqueta_a_idx = {et: i for i, et in enumerate(etiquetas)}

    for etiqueta in etiquetas:
        carpeta = os.path.join(ruta_dataset, etiqueta)
        for video_nombre in os.listdir(carpeta):
            ruta_video = os.path.join(carpeta, video_nombre)
            frames = extraer_frames(ruta_video, max_frames, img_size)
            if frames is not None:
                X.append(frames)
                y.append(etiqueta_a_idx[etiqueta])

    X = np.array(X)
    y = to_categorical(np.array(y), num_classes=len(etiquetas))

    return train_test_split(X, y, test_size=0.2), etiquetas

def extraer_frames(video_path, max_frames, img_size):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret or len(frames) >= max_frames:
            break
        frame = cv2.resize(frame, (img_size, img_size))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)
    cap.release()
    if len(frames) < max_frames:
        return None  # No usar videos con pocos frames
    return np.array(frames)
