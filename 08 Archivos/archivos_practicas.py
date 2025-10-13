def main():
#1- Crear archivo inicial con productos:
    lineas = [
        "lapicera,120.5,30\n",
        "regla,180.0,12\n",
        "tijera,250.0,20\n"
    ]
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)
    #2-Leer y mostrar productos:

    print("\nMostrando el archivo productos.txt:\n")
    leer_mostrar(lineas)

    #3- Llamar a la función agregar productos desde teclado:
    agregar_productos()

    #4- Cargar productos en una lista de diccionarios:
    productos = cargar_productos()    

    #4-1. Mostrar la lista de diccionarios:
   
    print("\nLista de productos en memoria:\n")
    for p in productos:
        print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    
    #5- Llamar a la funcion buscar producto.
    buscar_producto(productos)
    #6. Llamando a la función sobrescribir el archivo productos.txt 
    sobrescribir_archivo(productos)
    leer_mostrar(productos)

#2- Función leer mostrar lista de productos  
def leer_mostrar(lineas):
    with open("productos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(",")
            nombre, precio, cantidad = partes
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}") 
#3- Función agregar productos desde teclado:
def agregar_productos():
    with open("productos.txt", "a", encoding="utf-8") as archivo:
        while True:
            nombre = input("\nIngrese el nombre del producto que desea agregar: ")
            if not nombre:
                print("Nombre no puede estar vacío")
                continue
            try:

                precio = float(input("Ingrese el precio del producto: "))
                cantidad= int(input("Ingrese la cantidad: "))
            except ValueError:
                print("Ingrese valores numéricos válidos para precio y cantidad.")
                continue

            archivo.write(f"{nombre},{precio},{cantidad}\n")
            print(f"\nProducto '{nombre}' agregado correctamente.")

            continuar = input("\n¿Desea ingresar otro producto? (s/n): ").strip().lower()
            if continuar != "s":
                break 
#4- Cargar productos en una lista de diccionarios:            
def cargar_productos():
    productos = []
    with open("productos.txt", "r", encoding="utf-8") as archivo: 

        for linea in archivo:
            nombre,precio,cantidad = linea.strip ().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
                })
    return productos

#5- Función, buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto.
   
def buscar_producto(productos):
    nombre_producto = input("\nIngrese el nombre del producto que desea buscar: ")
    producto_encontrado = None

    for producto in productos:       
        
        if nombre_producto.lower() == producto["nombre"].lower():
            producto_encontrado = producto
            break  

    if producto_encontrado:
        print(f"\nProducto encontrado: \n{producto_encontrado}")
    else:
        print("Error, el producto no existe en la lista")
#6- Función sobrescribir el archivo productos.txt: Guardando los productos actualizados: 
def sobrescribir_archivo(productos):
    with open("productos.txt", "w", encoding="utf-8") as archivo:         
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("\nNuevo archivo de texto: \n")

              
  
main()                 
