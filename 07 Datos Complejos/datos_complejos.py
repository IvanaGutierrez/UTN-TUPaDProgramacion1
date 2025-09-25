""" 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300 """

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Diccionario antes de agregar elementos: {precios_frutas}") 
precios_frutas.update({'Naranja' : 1200, 'Manzana' : 1500, 'Pera' : 2300 })
print(f"Diccionario después de agregar los elementos: {precios_frutas}")

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado
 en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800 """
precios_frutas.update({'Banana' : 1330, 'Manzana' : 1700, 'Melón' : 2800})
print(f"Diccionario después de actualizar precios: {precios_frutas}")

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en
el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. """

lista_precios_frutas = ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']
print(f"Lista de frutas sin precios: {lista_precios_frutas}") 

""" 4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe. """
numeros_tefonicos = {

}
for i in range(0,4):
    clave = input("Ingrese el nombre: ")
    valor = input("Ingrese el numero: ")
    numeros_tefonicos[clave] = valor
print(numeros_tefonicos)
nombre = input("Ingrese un nombre: ")
if (numeros_tefonicos[nombre]) :
    print(numeros_tefonicos[nombre])
else:
    print("no existe")

""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra. """
frase = input("Ingrese una frase: ")
palabras = frase.split(" ")
palabras_unicas = set(palabras)
print(palabras_unicas)
diccionario_palabras = {}
for palabra in palabras_unicas:
   diccionario_palabras[palabra] = palabras.count(palabra)
print(diccionario_palabras)

""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. """
notas_alumnos = {}
for i in range(0,3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = input("Ingrese las notas separadas por ,: ")
    lista = notas.split(",")
    tupla = tuple(lista)
    notas_alumnos[nombre] = tupla

for alumno, notas in notas_alumnos.items():
    promedio = 0
    for nota in notas: 
        promedio += int(nota)
    promedio = promedio / len(notas)
    print("alumno ", alumno, "promedio ", round(promedio,2))

""" 7)Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). """
parcial1 = {4, 6, 7, 9, 10}
parcial2 = {5, 6, 8, 9, 8}

aprobados1 = set()
for nota in parcial1:
    if nota >= 6:
        aprobados1.add(nota)

aprobados2 = set()
for nota in parcial2:
    if nota >= 6:
        aprobados2.add(nota)

print("Aprobaron ambos:", aprobados1 & aprobados2)
print("Aprobaron solo uno:", aprobados1 ^ aprobados2)
print("Aprobaron al menos uno:", aprobados1 | aprobados2)

""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe. """