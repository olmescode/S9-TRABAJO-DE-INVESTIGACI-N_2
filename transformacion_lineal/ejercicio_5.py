import numpy as np
from modulo_principal.transformacion_lineal import es_transformacion_lineal

def transformacion_5(v):
    return np.array([0, v[1]])

def resolver_ejercicio_5():
    resultado = es_transformacion_lineal(transformacion_5, 3, 2)
    print(f"Ejercicio 5: La transformación es {'lineal' if resultado else 'no lineal'}")

if __name__ == "__main__":
    resolver_ejercicio_5()
