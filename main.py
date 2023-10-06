import tkinter as tk
from tkinter import filedialog
from entradaPD import leer_archivo_txt
from entradaFB import Entrada
from entradaV import readFile
import os
import shutil
import time
from Algoritmos import dinamica,fuerza_bruta,voraz

# Función de procesamiento según el tipo seleccionado
def procesar_archivo():
    tipo_programacion = tipo_programacion_var.get()
    contenido = texto_entrada.get(1.0, tk.END)
    
    if tipo_programacion == "Fuerza Bruta":
        inicio = time.time()
        # Realizar el procesamiento utilizando Fuerza Bruta
        resultado = procesamiento_fuerza_bruta(contenido)
        fin = time.time()
        tiempo_ejecucion = fin - inicio  # Calcula el tiempo de ejecución
        # resultado = f"Resultado de Programación Fuerza bruta\nTiempo de ejecución: {tiempo_ejecucion:.6f} segundos\n{resultado}"
    elif tipo_programacion == "Dinámica":
        inicio = time.time()
        # Realizar el procesamiento utilizando Programación Dinámica
        resultado = procesamiento_dinamica(contenido)

        fin = time.time()
        tiempo_ejecucion = fin - inicio  # Calcula el tiempo de ejecución
        # resultado = f"Resultado de Programación Dinámica\nTiempo de ejecución: {tiempo_ejecucion:.6f} segundos\n{resultado}"
    elif tipo_programacion == "Voraz":
        inicio = time.time()
        # Realizar el procesamiento utilizando Algoritmo Voraz
        resultado = procesamiento_voraz(contenido)
        fin = time.time()
        tiempo_ejecucion = fin - inicio  # Calcula el tiempo de ejecución
        # resultado = f"Resultado de Programación Voraz\nTiempo de ejecución: {tiempo_ejecucion:.6f} segundos\n{resultado}"
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

        # llamado a la función leer_archivo_txt y mostrar los resultados en la interfaz
        k, r, M, E = leer_archivo_txt(destino_path)
        return k, r, M, E # Retorna los datos del archivo para que puedan ser utilizados en la función procesar_archivo


# Función para cargar un archivo y mostrar su contenido version 2
def cargar_archivo2():
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

        # llamado a la función Entrada y mostrar los resultados en la interfaz
        cupos, materias, asignacion = Entrada(destino_path)
        return cupos, materias, asignacion # Retorna los datos del archivo para que puedan ser utilizados en la función procesar_archivo

# Función para cargar un archivo y mostrar su contenido version 3
def cargar_archivo3():
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

        k, r, M, E = readFile(destino_path)
        return k, r, M, E # Retorna los datos del archivo para que puedan ser utilizados en la función procesar_archivo

# Funciones de procesamiento de ejemplo
def procesamiento_fuerza_bruta(contenido):
    cupos, materias, asignacion = cargar_archivo2()
    contenido = fuerza_bruta.rocFB(cupos, materias, asignacion)
    return "Resultado de Fuerza Bruta \n" + str(contenido)

def procesamiento_dinamica(contenido):
    k, r, M, E = cargar_archivo()  # Llama a cargar_archivo para obtener los valores
    contenido = dinamica.rocPD(k,r,M,E)  # Llama a rocPD con los valores
    return "Resultado de Programación Dinámica: " + str(contenido)

def procesamiento_voraz(contenido):
    k, r, M, E = cargar_archivo3()
    contenido = voraz.rocV(k, r, M, E)
    return "Resultado de Algoritmo Voraz \n" + str(contenido)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Asignación de cupos")

# Área de texto 
aviso = tk.Label(ventana, text="Por favor primero seleccione una técnica de programación y luego suba un archivo de texto.")

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

# Posicionar los elementos en la ventana
aviso.pack(pady=10)
opciones_programacion_label.pack(pady=10)
for radio in opciones_programacion_radios:
    radio.pack()
etiqueta_nombre_archivo.pack(pady=10)
boton_procesar.pack(pady=10)

# Función para crear una barra de desplazamiento para un área de texto
def crear_barra_desplazamiento(area_texto, contenedor):
    scrollbar = tk.Scrollbar(contenedor)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar.config(command=area_texto.yview)
    area_texto.config(yscrollcommand=scrollbar.set)

# Crear un marco para el área de texto de entrada
marco_entrada = tk.Frame(ventana)
marco_entrada.pack(padx=10, pady=10)
texto_entrada = tk.Text(marco_entrada, wrap=tk.WORD, width=40, height=10)
texto_entrada.insert(tk.END, "Aquí se mostrará el contenido del archivo de entrada.")
texto_entrada.pack(side=tk.LEFT)
crear_barra_desplazamiento(texto_entrada, marco_entrada)

# Crear un marco para el área de texto de salida
marco_salida = tk.Frame(ventana)
marco_salida.pack(padx=10, pady=10)
texto_salida = tk.Text(marco_salida, wrap=tk.WORD, width=40, height=10)
texto_salida.insert(tk.END, "Aquí se mostrará el resultado del procesamiento.")
texto_salida.pack(side=tk.LEFT)
crear_barra_desplazamiento(texto_salida, marco_salida)
texto_entrada.pack(padx=10, pady=10)
texto_salida.pack(padx=10, pady=10)

ventana.mainloop()


