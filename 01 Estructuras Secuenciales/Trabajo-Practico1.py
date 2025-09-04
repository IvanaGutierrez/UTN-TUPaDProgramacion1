#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo")
#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre = input("¿Como te llamas?")
print(f"Hola, me llamo {nombre}")
#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apelido? ")
edad = int(input("Dime tu edad "))
domicilio = input("Dime tu país de resdencia ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {domicilio}")
#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
radio = int(input("Ingrese el radio del círculo"))
perimetro = 2 * 3.1416 * radio
area = 3.1416 * radio * radio
print(f"El perimetro del círculo de acuerdo al radio ingresado es: {perimetro} y su área es: {area}" )
#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos = int(input("Dime la cantidad de segudos"))
horas = float(segundos/3600)
print(f"tu tiempo en horas es: {horas}")
#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
multiplicando = int(input("Dígame el mutiplicando"))
print("Aquí tiene su tabla")
for multiplicador in range (1,11):
    resultado = multiplicando * multiplicador   
    print(f"{multiplicador} * {multiplicando} = {resultado} ")
#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
while True:
  num1 = int(input("Ingrese un número distinto de 0"))
  if num1 != 0 :
    break  
  print("El número no puede ser 0")
 #Pedimos el segundo numero 
while True:
  num2 = int(input("Ingrese el segudo valor distinto de 0"))
  if num2 != 0 :
    break  
  print("El numero no puede ser 0")
#Mostramos resultados 
print(f"Resultados de las operaciones entre {num1} y {num2}")
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Mutiplicacón: {num1 * num2}")
print(f"División: {num1 / num2}")
#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo
altura = float(input("Ingerese su altura: "))
peso = float(input("Ingerese su peso: "))
print(f"Su índice de masa corporal es: {peso / (altura * altura)}")
#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
tempGradosCelsius = float(input("Ingrese la temperatura en grados Celsius"))
tempGradosFahrenheit = float((9/5)*tempGradosCelsius+32)
print(f"La equivalencia en grados fahrenheit es: {tempGradosFahrenheit} °F")
#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números
valor1 = float(input("Ingrese el primer valor"))  
valor2 = float(input("Ingrese el segundo valor"))
valor3 = float(input("Ingrese el tercer valor"))
promedio = float((valor1+valor2+valor3)/3)
print(f"El promedio de los valores ingresados es: {promedio}")