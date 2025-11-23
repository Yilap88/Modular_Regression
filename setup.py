# setup.py
from setuptools import setup, find_packages

setup(
    name='modular_regression',  # Nombre de tu proyecto/paquete
    version='0.1.0',
    description='Proyecto modular de regresión lineal simple para aprender packaging.',
    author='Yilmer (Yilap88)',
    # Indica a setuptools que busque subcarpetas que contengan código
    packages=find_packages(where='src'), 
    package_dir={'': 'src'}, # Mapea la carpeta raíz a src
    install_requires=[
        'numpy',
        'scikit-learn',
    ],
)