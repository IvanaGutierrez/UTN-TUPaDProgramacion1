""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. """
#ciclo for desde 0 hasta 101 ya que el ultimo parametro no se imprime
for i in range(101):
    print(i)

""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene. """

# Solicitamos al usuario un número entero (se guarda como cadena de texto)
numero_entero = input("Ingrese un número entero: ")

# Inicializamos un contador en 0 para llevar la cantidad de dígitos
contador = 0

# Recorremos cada carácter (dígito) del número ingresado
for dig in numero_entero:
    contador += 1   # Por cada dígito, sumamos 1 al contador

# Mostramos la cantidad total de dígitos
print(f"La cantidad de dígitos es: {contador}")


""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores """

# Pedimos al usuario dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Inicializamos la suma
suma = 0

# Sumamos todos los números entre numero1 y numero2 (excluyendo los ingresados)
for i in range(numero1 + 1, numero2):
    suma += i

# Mostramos el resultado
print(suma)


""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0. """
# Inicializamos un acumulador en 0 para guardar la suma de los números ingresados
suma = 0

# Inicializamos la variable numero_ingresado con un valor distinto de 0
numero_ingresado = 1

# Bucle infinito que se repetirá hasta que el usuario ingrese 0
while True:
    # Solicitamos al usuario un número distinto de 0
    numero_ingresado = int(input("Ingrese un número distinto de 0: "))

    # Verificamos si el número ingresado es 0
    if numero_ingresado == 0:
        break   # Si es 0, salimos del bucle
    else:
        # Si el número es distinto de 0, lo sumamos al acumulador
        suma += numero_ingresado

# Mostramos el total de la suma de todos los números ingresados
print(suma)    
""" 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. """

import random   # Importamos la librería random para generar números aleatorios

intento = 1     # Contador de intentos, arranca en 1
numero_ingresado = 0   # Inicializamos la variable que guardará el número del usuario

# Generamos un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0,9)

print(numero_aleatorio)  
# Esto imprime el número aleatorio (sirve para probar el programa)
# Si fuera un juego real, este print debería quitarse para que el usuario no vea el número

# Bucle infinito que solo terminará cuando adivinemos el número
while True:
    # Solicitamos al usuario un número entre 0 y 9
    numero_ingresado = int(input("Ingrese un número entre 0 y 9: "))

    # Verificamos si el número ingresado coincide con el aleatorio
    if numero_ingresado == numero_aleatorio:
        break   # Si son iguales, salimos del bucle
    else:
        intento += 1   # Si no acertó, aumentamos en 1 el contador de intentos

# Mostramos la cantidad de intentos que necesitó el usuario para adivinar
print(intento)


""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente. """

#con un ciclo for con rago desde 100 hasta -1 ya que queremos q imprimir hasta el cero 
#con decremento -2 ya que queremoe numeros pares

for i in range(100, -1, -2):
    print(i)

""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario """

# Pedimos al usuario un número entero positivo hasta el cual queremos sumar
numero_ingresado = int(input("Ingrese hasta que numero desea sumar: "))

# Inicializamos un acumulador en 0, donde iremos guardando la suma
suma = 0

# Recorremos todos los números desde 0 hasta numero_ingresado - 1
for i in range(numero_ingresado):
    # En cada iteración sumamos el valor de i al acumulador
    suma += i 

# Mostramos el resultado final de la suma
print(suma)

""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio). """

#cantidad de números a socitar
cantidad = 3
#inicializamos las variables en 0
pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el numero: {i+1}: "))
 # Pares e impares
    if numero %2 == 0:
        pares += 1
    else:
        impares += 1
# Positivos y negativos (excluimos el 0)
    if numero > 0:
        positivos += 1  
    elif numero < 0:
        negativos += 1     
#Mostramos resutados        
print("--- Resutados: ---")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor). """

#cantidad de números a socitar
cantidad = 3 
#inicializo en cero la variable promedio
promedio = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el numero: {i+1}: "))
    suma += numero   # acumulo todos los números

promedio = suma / cantidad   # calculo el promedio 

#Mostramos resutados    
print("--- Resutados: ---")
print(f"Proomedio: {promedio}")

""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. """

# Pedimos al usuario que ingrese un número (queda guardado como cadena de texto)
numero = input("Ingrese el numero: ")

# Inicializamos una variable vacía que usaremos para ir construyendo el número invertido
numero_invertido = ""

# Recorremos cada caracter (dígito) del número ingresado
for digito in numero:
    # En cada vuelta ponemos el nuevo dígito al inicio de numero_invertido
    numero_invertido = digito + numero_invertido

# Mostramos el número invertido
print(numero_invertido)

    