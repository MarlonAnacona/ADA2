import tkinter as tk
from tkinter import filedialog
from entradas import leer_archivo_txt
import os
import shutil
from Algoritmos import dinamica

# Función de procesamiento según el tipo seleccionado
def procesar_archivo():
    tipo_programacion = tipo_programacion_var.get()
    contenido = texto_entrada.get(1.0, tk.END)
    
    if tipo_programacion == "Fuerza Bruta":
        # Realizar el procesamiento utilizando Fuerza Bruta
        resultado = procesamiento_fuerza_bruta(contenido)
    elif tipo_programacion == "Dinámica":
        # Realizar el procesamiento utilizando Programación Dinámica
        resultado = procesamiento_dinamica(contenido)
    elif tipo_programacion == "Voraz":
        # Realizar el procesamiento utilizando Algoritmo Voraz
        resultado = procesamiento_voraz(contenido)
    else:
        resultado = "Tipo de programación no válido"

    texto_salida.delete(1.0, tk.END)  # Borra el contenido actual
    texto_salida.insert(tk.END, resultado)  # Muestra el resultado en el área de salida.

# Función para cargar un archivo y mostrar su contenido
def cargar_archivo():
    archivo_path = filedialog.askopenfilename(title="Seleccionar archivo de entrada", filetypes=[("Archivos de texto", "*.txt;*.roc")])
    if archivo_path:
        nombre_archivo = os.path.basename(archivo_path)  # Obtiene el nombre del archivo
        
        # Define la ruta de destino en la carpeta "pruebas"
        carpeta_pruebas = "./pruebas"
        destino_path = os.path.join(carpeta_pruebas, nombre_archivo)
        
        # Copia el archivo seleccionado a la carpeta "pruebas"
        shutil.copy(archivo_path, destino_path)
        
        etiqueta_nombre_archivo.config(text="Nombre del archivo: " + nombre_archivo)  # Actualiza la etiqueta con el nombre del archivo
        
        with open(destino_path, "r") as archivo:
            contenido = archivo.read()
            texto_entrada.delete(1.0, tk.END)  # Borra el contenido actual
            texto_entrada.insert(tk.END, contenido)  # Inserta el contenido del archivo

        # Aquí puedes llamar a la función leer_archivo_txt del otro script y mostrar los resultados en la interfaz
        k, r, M, E = leer_archivo_txt(destino_path)
        return k, r, M, E # Retorna los datos del archivo para que puedan ser utilizados en la función procesar_archivo


# Funciones de procesamiento de ejemplo (reemplaza con tus propias implementaciones)
def procesamiento_fuerza_bruta(contenido):
    # Implementa la lógica de Fuerza Bruta aquí
    return "Resultado de Fuerza Bruta"

def procesamiento_dinamica(contenido):
    k, r, M, E = cargar_archivo()  # Llama a cargar_archivo para obtener los valores
    contenido = dinamica.rocPD(k,r,M,E)  # Llama a rocPD con los valores
    return "Resultado de Programación Dinámica: " + str(contenido)

def procesamiento_voraz(contenido):
    # Implementa la lógica de Algoritmo Voraz aquí
    return "Resultado de Algoritmo Voraz"

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Asignación de cupos")

# Área de texto 
aviso = tk.Label(ventana, text="Por favor primero seleccione una técnica de programación y luego suba un archivo de texto. Luego de subido puede probarlo con los tres tipos de algoritmos para probar con otro archivo distinto reinicie la interfaz.")

# Crear opciones de programación
tipo_programacion_var = tk.StringVar()
tipo_programacion_var.set("Fuerza Bruta")  # Valor predeterminado
opciones_programacion = ["Fuerza Bruta", "Dinámica", "Voraz"]
opciones_programacion_label = tk.Label(ventana, text="Selecciona el tipo de programación:")
opciones_programacion_radios = [tk.Radiobutton(ventana, text=opcion, variable=tipo_programacion_var, value=opcion) for opcion in opciones_programacion]

# Etiqueta para mostrar el nombre del archivo
etiqueta_nombre_archivo = tk.Label(ventana, text="Nombre del archivo: ")
# Botón para procesar el archivo
boton_procesar = tk.Button(ventana, text="Subir archivo y procesar", command=procesar_archivo)

# Área de texto para mostrar el contenido del archivo de entrada
texto_entrada = tk.Text(ventana, wrap=tk.WORD, width=40, height=10)
texto_entrada.insert(tk.END, "Aquí se mostrará el contenido del archivo de entrada.")

# Área de texto para mostrar el resultado
texto_salida = tk.Text(ventana, wrap=tk.WORD, width=40, height=10)
texto_salida.insert(tk.END, "Aquí se mostrará el resultado del procesamiento.")

# Posicionar los elementos en la ventana
aviso.pack(pady=10)
opciones_programacion_label.pack(pady=10)
for radio in opciones_programacion_radios:
    radio.pack()
etiqueta_nombre_archivo.pack(pady=10)
boton_procesar.pack(pady=10)
texto_entrada.pack(padx=10, pady=10)
texto_salida.pack(padx=10, pady=10)

ventana.mainloop()


