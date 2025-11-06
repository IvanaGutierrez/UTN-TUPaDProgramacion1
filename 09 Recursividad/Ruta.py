from RutaFichero import listar_archivos
# Usamos una cadena raw (cruda) con r delante ya que Python intenta leer \U como algo especial y se rompe.
lista_rutas = []
ruta = r"C:\Users\Ivana Gutierrez\Documents\Aprendiendo a programar"

listar_archivos(ruta, lista_rutas)

# print(lista_rutas)
