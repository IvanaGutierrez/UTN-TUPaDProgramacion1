"""
Obtener ruta de mis ficheros, con recursividad
"""

import os


def listar_archivos(directorio, lista):
    for elemento in os.listdir(directorio):
        ruta = os.path.join(directorio, elemento)
        if os.path.isdir(ruta):
            # si es una carpeta, llamamos recursivamente
            print(f"Directorio padre: {ruta}")
            print("-----------------------------------")
            listar_archivos(ruta, lista)
        else:
            # si es un archivo, lo mostramos
            lista.append(ruta)
            print(ruta)


if __name__ == "__main__":
    lista = []
    listar_archivos(r"C:\Users\Ivana Gutierrez\Documents\GitHub", lista)
    print(lista)
