# ----EJERCICIO 1----
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# PROGRAMA PRINCIPAL.
# Solicitamos al usuario que ingrese un numero.
numero = int(input("Ingrese un numero positivo: "))
while numero <= 0:
    print("Numero inválido. Ingrese otro")
    numero = int(input())
# Mostramos el factorial de todos los numero hasta el numero ingresado.
for i in range(1, numero + 1):
    print(f"Factorial del numero {i}: {factorial(i)}")

# ----EJERCICIO 2----


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)


# PROGRAMA PRINCIPAL.
# Solicitamos al usuario que ingrese un numero.
numero = int(input("Ingrese un numero mayor o igual a 0: "))
while numero < 0:
    print("Numero inválido. Ingrese otro")
    numero = int(input())
# Mostramos las posiciones de todos los numeros hasta el numero ingresado de la serie fibonacci.
for i in range(numero + 1):
    print(f"Valor en la posicion {i} de la serie de Fibonacci: {fibonacci(i)}")

# ----EJERCICIO 3----


def calculo_potencia(base, exponente):
    if exponente == 1:
        return base
    else:
        return base * calculo_potencia(base, exponente - 1)


# PROGRAMA PRINCIPAL.
# Solicitamos al usuario que ingrese una base y un exponente positivos.
base = int(input("Ingrese una base positiva: "))
while base <= 0:
    print("Base incorrecta. Ingrese otra")
    base = int(input())
exponente = int(input("Ingrese un exponente positivo: "))
while exponente <= 0:
    print("Exponente incorrecto. Ingrese otro")
    exponente = int(input())
# Calculamos la potencia con la ayuda de la funcion.
print(f"{base} ^ {exponente} = {calculo_potencia(base, exponente)}")

# ----EJERCICIO 4----


def convertir_binario(num):
    if num == 1:
        return "1"
    else:
        return convertir_binario(num // 2) + str(num % 2)


# PROGRAMA PINCIPAL.
num = int(input("Ingrese un numero positivo: "))
while num < 1:
    print("Numero Incorecto. Ingese otro")
    num = int()
print(f"{num} en binario es: {convertir_binario(num)}")

# ----EJERCICIO 5----


def es_palindromo(palabra, izquierda, derecha):
    if palabra[izquierda] != palabra[derecha]:
        return False
    elif izquierda == derecha:
        return True
    else:
        return es_palindromo(palabra, izquierda+1, derecha-1)


# PROGRAMA PRINCIPAL.
palabraCorrecta = False
while palabraCorrecta == False:
    palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
    palabraCorrecta = True
    for letra in palabra:
        if letra == " " or letra in "áéíóú":
            print("Palabra inválida.")
            palabraCorrecta = False
            break
izquierda = 0
derecha = len(palabra) - 1
print(
    f"¿La palabra {palabra} es palindromo? {es_palindromo(palabra, izquierda, derecha)}")

# ----EJERCICIO 6----


def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return suma_digitos(n // 10) + n % 10


# PROGRAMA PRINCIPAL.
n = int(input("Ingrese un numeor positivo: "))
while n < 1:
    print("Numero inválido. Ingrese otro")
    n = int()
print(f"La suma de los digitos de {n} es: {suma_digitos(n)}")

# ----EJERCICIO 7----


def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n-1)


# PROGRAMA PRINCIPAL.
n = int(input("Ingrese una cantidad de bloques: "))
while n < 1:
    print("Cantidad de bloques inválida. Ingrese otra")
    n = int()
print(
    f"La cantidad total de bloques que necesita para contruir la pirámide es de: {contar_bloques(n)}")

# ----EJERCICIO 8----


def contar_digito(n, digit):
    if n == 0:
        return 0
    elif n % 10 == digit:
        return 1 + contar_digito(n//10, digit)
    else:
        return contar_digito(n//10, digit)


# PROGRAMA PRINCIPAL
n = int(input("Ingrese un numero: "))
while n < 1:
    print("Numeo inválido. Ingrese otro")
    n = int()
digit = int(input("Ingrese un digito del 1 a 10: "))
while digit < 1 or digit > 10:
    print("Digito inválido. Ingrese otro")
    digit = int()
print(
    f"La cantidad de veces que aparece {digit} en {n} es: {contar_digito(n, digit)}")
