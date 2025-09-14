""" 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range. """

for i in range(0,101,4):
    #if i % 4== 0:
     print(i)

""" 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!
 """
#creando lista
frutas = ["banana", "naranja","manzana", "mandarina", "pomelo"]
for i in [-2]:   # recorro solo el índice -2
    print(frutas[i])

""" 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = [] """

lista_vacia =[]
lista_vacia.append("mar")
lista_vacia.append("sol")
lista_vacia.append("arena")
print(lista_vacia)

""" 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos! """

animales = ["perro", "gato", "conejo", "pez"]
animales[-2] = "loro"
animales[-1] = "oso"
print(animales)

""" 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. """
""" numeros = [8, 15, 3, 22, 7]

numeros.remove(max(numeros))
print(numeros) """

#este codigo busca el valor maximo de la lista y lo quita de la misma

""" 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros """

#creando la lista y rellendo 
lista_numeros = [10, 15, 20, 25, 30]
for i in [0, 1]:
    print(lista_numeros[i])

#creando la lista y rellendo con for
lista = []
#rellenando del 10 al 30 incluido de 5 en 5
for i in range(10, 31, 5):
    lista.append(i)#añadiendo con append elementos a la lista
#mostrando los 2 primeros elementos
print(lista[:2])
#mostrando lista completa para ver q se lleno correctamente
print(lista)

""" 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera."""

autos = ["sedan", "polo", "suran", "gol"] 
autos[1] = "amarok"
autos[2] = "tera"
print(autos) 

""" 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla. """

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles) 

""" 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla """

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

""" 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla. """

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False],]
print(lista_anidada)
mi_lista = {1,2,2,3,3,3}
print(mi_lista)