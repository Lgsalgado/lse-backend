import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, LSTM, TimeDistributed, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
import numpy as np
import os

from app.services.extraer_datos import cargar_datos_desde_videos

# Construcción del modelo CNN + LSTM
def construir_modelo(input_shape=(30, 64, 64, 3), num_clases=20):
    modelo = Sequential()
    modelo.add(TimeDistributed(Conv2D(32, (3, 3), activation='relu'), input_shape=input_shape))
    modelo.add(TimeDistributed(MaxPooling2D((2, 2))))
    modelo.add(TimeDistributed(BatchNormalization()))
    modelo.add(TimeDistributed(Flatten()))
    modelo.add(LSTM(64, return_sequences=False))
    modelo.add(Dropout(0.5))
    modelo.add(Dense(64, activation='relu'))
    modelo.add(Dense(num_clases, activation='softmax'))
    modelo.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    return modelo

# Entrenamiento
def entrenar_modelo():
    dataset_path = "app/dataset"  # <== ajusta esta ruta a la tuya
    (X_train, X_val, y_train, y_val), clases = cargar_datos_desde_videos(dataset_path)

    modelo = construir_modelo(input_shape=X_train.shape[1:], num_clases=len(clases))
    history = modelo.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=30,
        batch_size=8
    )

    # Guardar el modelo entrenado
    modelo.save("app/services/modelo_lse.h5")
    print("✅ Modelo guardado como 'modelo_lse.h5'")

    # Guardar etiquetas/clases
    with open("app/services/clases.txt", "w") as f:
        for clase in clases:
            f.write(clase + "\n")
    print("📄 Clases guardadas en 'clases.txt'")

    return history

if __name__ == "__main__":
    entrenar_modelo()
