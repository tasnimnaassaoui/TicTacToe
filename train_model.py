from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

# Charger les données
data = np.load("tictactoe_data.npz")
X = data["X"]
y = data["y"]

# Créer le modèle
model = Sequential([
    Dense(128, activation='relu', input_shape=(9,)),
    Dense(128, activation='relu'),
    Dense(9, activation='softmax')
])

model.compile(optimizer=Adam(0.001), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=20, batch_size=32, validation_split=0.2)

# Sauvegarde
model.save("tictactoe_model.h5")
print("Modèle entraîné et sauvegardé sous 'tictactoe_model.h5'")
