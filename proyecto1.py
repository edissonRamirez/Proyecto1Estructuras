import os
import shutil
from NaryTree import NaryTree, NaryTreeNode

class Gestor:
    def __init__(self):
        self.arbol_directorios = NaryTree()

    def explorar(self, ruta_actual, ident="", padre = None):
        lista_archivos = os.listdir(ruta_actual)
        for archivo in lista_archivos:
                ruta_completa = ruta_actual +"/"+ archivo 
                nodo = NaryTreeNode(ruta_completa)
                self.arbol_directorios.add_node(ruta_completa, ruta_actual)
                nombre = os.path.basename(nodo.data)
                if os.path.isdir(ruta_completa):
                    print(f"{ident}{nombre}/")
                    self.explorar(ruta_completa, ident + "   ",nodo.data)
                else:
                    print(f"{ident}{nombre}")
    def renombrar(self, ruta_original, nombre):
        padre=self.arbol_directorios._find_parent(ruta_original, self.arbol_directorios.root)
        if padre:
            ruta_nueva = padre.data+ "/"+nombre
            try:
                os.rename(ruta_original, ruta_nueva)
                self.arbol_directorios.rename_node(ruta_original, ruta_nueva)
                print(self.arbol_directorios.find_node(ruta_nueva))
                print("El archivo/carpeta se ha renombrado exitosamente.")
            except:
                print("Error al renombrar el archivo/carpeta.")
        else:
            print("No se encontró la ubicación original del archivo/carpeta.")
        
        
    def eliminar(self, locacion):
        if os.path.isdir(locacion):
            # Eliminar directorio y su contenido
            try:
                for item in os.listdir(locacion):
                    item_path = os.path.join(locacion, item)
                    self.eliminar(item_path)
                os.rmdir(locacion)
                print(f"Directorio eliminado: {locacion}")
            except OSError as e:
                print(f"No se pudo eliminar el directorio {locacion}: {e}")
        elif os.path.isfile(locacion):
            # Eliminar archivo
            try:
                os.remove(locacion)
                print(f"Archivo eliminado: {locacion}")
            except OSError as e:
                print(f"No se pudo eliminar el archivo {locacion}: {e}")
        else:
            print(f"Ubicación inválida: {locacion}")

        