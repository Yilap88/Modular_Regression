# src/model_training.py

from sklearn.linear_model import LinearRegression
import numpy as np

def train_linear_model(X: np.ndarray, y: np.ndarray):
    """
    Entrena un modelo de regresión lineal simple.

    Args:
        X: Array de NumPy con las características (Inputs).
        y: Array de NumPy con el target (Output).
    
    Returns:
        El objeto LinearRegression entrenado.
    """
    # Scikit-learn espera que X sea 2D, incluso para una sola feature
    X = X.reshape(-1, 1) 
    
    # Crea y entrena el modelo
    model = LinearRegression()
    model.fit(X, y)
    
    return model