"""
Realizar una funcion recursiva que resiva un numero y una frase 
y la repita el numero de veces ingresado
"""


def repetir_frase(num, frase):
    if num >= 1:
        print(frase)
        repetir_frase(num-1, frase)


if __name__ == "__main__":
    # esto lo imprime si ejecutamos desde este archivo
    repetir_frase(3, "Ivana")
