# main.py

# Importamos la función de entrenamiento de nuestro módulo
from scr.model_training import train_linear_model
import numpy as np
from sklearn.model_selection import train_test_split

# 1. Creamos datos de ejemplo (Simulación de ETL)
np.random.seed(42)
X = np.arange(100)  # Input: [0, 1, 2, ..., 99]
# Output: y = 2*X + ruido
y = 2 * X + np.random.normal(0, 10, 100) 

# 2. Dividimos datos para simular un proceso real
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. LLAMADA MODULAR: Entrenamos el modelo
# El main.py NO sabe cómo funciona el entrenamiento, solo llama a la función.
modelo_entrenado = train_linear_model(X_train, y_train)

# 4. Usamos el modelo para predecir y mostramos el resultado
predicciones = modelo_entrenado.predict(X_test.reshape(-1, 1))

print("--- Resultado del Módulo ---")
print(f"Coeficiente (pendiente) del modelo: {modelo_entrenado.coef_[0]:.2f}")
print(f"Intercepto: {modelo_entrenado.intercept_:.2f}")
print(f"Predicción para X={X_test[0]}: {predicciones[0]:.2f}")