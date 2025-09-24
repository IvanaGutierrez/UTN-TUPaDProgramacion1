""" 1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal. """
def imprimir_hola_mundo():
    print("Hola mundo!")

#programa principal
imprimir_hola_mundo()

""" 2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario. """
def saludar_usuario(nombre):
    return (f"Hola {nombre}")

#programa principal
print(saludar_usuario(nombre = input("Ingrese su nombre: ")))

""" 3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
pedir los datos al usuario y llamar a esta función con los valores ingresados."""
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#programa principal
nombre = input("Ingrese su nombre: ") 
apellido = input("Ingrese su apellido: ")
edad = input("Cual es su edad: ") 
residencia = input("Cual es su domicilio: ")
informacion_personal(nombre,apellido,edad,residencia)

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados. """
import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
   
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#programa principal
radio = int(input("Ingrese el radio del círculo: "))
print(f"El area del círculo es: {round(calcular_area_circulo(radio),2)}")
print(f"El perímetro del círculo es: {round(calcular_perimetro_circulo(radio),2)}")

""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función. """
def segundos_a_horas(segundos):
    return segundos/60

#programa principal
print(segundos_a_horas(segundos = int(input("Ingrese la cantidad de segundos: "))))

""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función. """
def tabla_multiplicar(numero):
    resultado = 0
    for i in range(1,11):
       resultado = numero * i
       print(f"{numero} * {i} = {resultado}")
#programa principal
tabla_multiplicar(numero = int(input("Ingrese su numero: ")))

""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara. """
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    tupla= (suma, resta, multiplicacion, division)
    return tupla

#programa principal
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
resultados = operaciones_basicas(num1, num2)
print(f"Suma: {resultados[0]} Resta: {resultados[1]} Multiplicacion: {resultados[2]} División: {round(resultados[3],2)}")

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
para mostrar el resultado con dos decimales. """
def calcular_imc(peso, altura):
    return peso / (altura)**2
    

#programa principal
peso = float(input("Ingrese su peso en kilogramos: ")) 
altura = float(input("Ingrese su altura en metros: ")) 
print(f"Su índice de masa corporral es: {round(calcular_imc(peso, altura),2)}")

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función. """
def celsius_a_fahrenheit(celsius):
    return celsius * 1.8  + 32

#programa principal
celsius = float(input("Ingrese cuantos grados celsius hacen: "))
print(f"Los {celsius}°C en fahrenheit equivalen a {round(celsius_a_fahrenheit(celsius),2)}°F")

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función. """
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#programa principal
num1 = int(input("Ingrese su primer número: "))
num2 = int(input("Ingrese su segundo número: "))
num3 = int(input("Ingrese su tercer número: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los numeros ingresados es: {round(promedio,2)}")
