from proyecto1 import *
from Gui import *

explorador = Gestor()
explorador.arbol_directorios.add_node("C:\\Prueba")


# Crear una instancia de la clase GUI pasando el gestor como argumento
gui = GUI(explorador)

# Ejecutar la interfaz gráfica
gui.run()

# explorador.explorar("C:\\Prueba", "C:\\Prueba")
# explorador.renombrar("C:\\Prueba\\pruebarenombrada", "pruebarenombrar")
# explorador.eliminar("C://Prueba\\pruebaeliminar")
# print(explorador.arbol_directorios.find_node("C://Prueba\\PruebaEliminar"))
# explorador.explorar("C://Prueba", "C://Prueba")