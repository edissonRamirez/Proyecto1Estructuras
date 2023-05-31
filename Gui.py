import tkinter as tk
import sys
from tkinter import filedialog, simpledialog
from proyecto1 import *

class GUI:
    def __init__(self, gestor):
        self.gestor = gestor
        
        self.root = tk.Tk()
        self.root.title("Gestor de Archivos")
        self.root.geometry("1000x400")


        # Obtener las dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular el ancho y alto de los cuadros
        results_width = int(screen_width * 0.7)
        results_height = int(screen_height * 0.8)
        instructions_width = int(screen_width * 0.3)
        instructions_height = int(screen_height * 0.8)

        # Calcular las coordenadas para centrar los cuadros verticalmente
        x = (screen_width - results_width) // 2
        y = (screen_height - results_height) // 2

        # Establecer el color de fondo de la interfaz
        self.root.configure(bg='#152a38')

        # Crear un marco para contener el cuadro de resultados
        result_frame = tk.Frame(self.root, width=results_width, height= results_height, bg='white')
        result_frame.grid(row=0, column=0, padx=50, pady=20, sticky="nsew")
        result_frame.grid_rowconfigure(0, weight=1)  # Configuración para expansión vertical
        result_frame.grid_columnconfigure(0, weight=1)  # Configuración para expansión horizontal

        # Crear un cuadro de texto para mostrar los resultados
        self.result_text = tk.Text(result_frame, wrap = "word")
        self.result_text.grid(row=0, column=0, padx=10, pady=10)

        # Crear un marco para contener el cuadro de instrucciones
        instructions_frame = tk.Frame(self.root, width=instructions_width, height=instructions_height, bg='white')
        instructions_frame.grid(row=0, column=1, padx=50, pady=20, sticky="nsew")
        instructions_frame.grid_rowconfigure(0, weight=1)  # Configuración para expansión vertical
        instructions_frame.grid_columnconfigure(0, weight=1)  # Configuración para expansión horizontal

        # Crear un cuadro de texto para mostrar las instrucciones
        self.instructions_text = tk.Text(instructions_frame, wrap = "word")
        self.instructions_text.grid(row=0, column=0, padx=10, pady=10)

        # Agregar las instrucciones al cuadro de texto de las instrucciones
        self.instructions_text.insert(tk.END, "--- IMPORTANTE --- \n \n")
        self.instructions_text.insert(tk.END, "Para que el programa funcione, primero debe presionar el botón 'Explorar' \n \n")
        self.instructions_text.insert(tk.END, "1. Presionar el botón de explorar para ver todos los directorios y archivos de un directorio \n \n")
        self.instructions_text.insert(tk.END, "2. Para usar el botón 'Renombrar', selecciona la carpeta o archivo y proporciona un nuevo nombre \n \n")
        self.instructions_text.insert(tk.END, "3. El botón 'Eliminar' sirve para borrar directorios con su contenido\n \n")
        self.instructions_text.insert(tk.END, "4. El botón 'Eliminar archivo' permite seleccionar para eliminar únicamente un archivo")
        

        # Configurar la alineación de los cuadros al centro
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Crear un scrollbar para el cuadro de texto
        scrollbar = tk.Scrollbar(result_frame)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Asociar el scrollbar con el cuadro de texto
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)

        # Redirigir la salida estándar a la función de actualización del cuadro de texto
        sys.stdout = StdoutRedirector(self.result_text)

        # Crear un marco para contener los botones
        button_frame = tk.Frame(self.root, bg='#152a38')
        button_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        # Crear los botones
        self.explorar_button = tk.Button(button_frame, text="Explorar", command=self.explorar, width=20, bg='#556e53')
        self.explorar_button.grid(row=0, column=0, pady=5, padx=10)
        
        self.renombrar_button = tk.Button(button_frame, text="Renombrar", command=self.renombrar, width=20, bg='#556e53')
        self.renombrar_button.grid(row=0, column=1, pady=10, padx=5)
        
        self.eliminar_button = tk.Button(button_frame, text="Eliminar", command=self.eliminar, width=20, bg='#556e53')
        self.eliminar_button.grid(row=0, column=2, pady=10, padx=10)

        self.eliminar_archivo_button = tk.Button(button_frame, text="Eliminar Archivo", command=self.eliminar_archivo, width=20, bg='#556e53')
        self.eliminar_archivo_button.grid(row=0, column=3, pady=10, padx=10)

        # Configurar la alineación de los botones al centro
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_rowconfigure(1, weight=1)
        button_frame.grid_rowconfigure(2, weight=1)
        button_frame.grid_rowconfigure(3, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        
    def explorar(self):
        ruta_inicial = filedialog.askdirectory(title="Seleccionar directorio")
        self.gestor.arbol_directorios.add_node(ruta_inicial)
        if ruta_inicial:
            resultado = f"{os.path.basename(ruta_inicial)}"
            self.result_text.insert("end", resultado + "\n")
            self.result_text.see("end")
            self.gestor.explorar(ruta_inicial, "   ",ruta_inicial)
    
    def renombrar(self):
        ruta_original = filedialog.askdirectory(title="Seleccionar directorio original")
        nuevo_nombre = simpledialog.askstring("Nuevo nombre", "Ingrese el nuevo nombre:") 
        self.gestor.renombrar(ruta_original, nuevo_nombre)
    
    def eliminar(self):
        locacion = filedialog.askdirectory(title="Seleccionar directorio o archivo para eliminar")
        if locacion:
            self.gestor.eliminar(locacion)

    def eliminar_archivo(self):
        archivo = filedialog.askopenfilename(title="Seleccionar archivo para eliminar")
        if archivo:
            self.gestor.eliminar(archivo)
    
    def run(self):
        self.root.mainloop()
class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert("end", message)
        self.text_widget.see("end")