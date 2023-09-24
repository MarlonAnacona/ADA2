from entradas import leer_archivo_txt

def inicio(nombre_archivo):
    k, r, M, E = leer_archivo_txt(nombre_archivo)
    rocPD(k, r, M, E)

def rocPD(k, r, M, E):
    #convertirMateriasACupos(M)
    convertirEstudiantesMateriasVectores(E,M)
    # El código sigue aquí...
    return 0 

def convertirEstudiantesMateriasVectores(E,M):
  matrices_estudiantes = {}
  for codigo, (num_materias, materias) in E.items():
        # Crear una matriz para el estudiante actual
        matriz_estudiante = [0] * len(M)
        for materia, valor in materias:
            # Usar el orden de la materia en el diccionario base para determinar la posición en la matriz
            indice = list(M.keys()).index(materia)
            matriz_estudiante[indice] = valor
        matrices_estudiantes[codigo] = matriz_estudiante

    # Imprimir las matrices de los estudiantes
  for codigo, matriz in matrices_estudiantes.items():
        print(f"Estudiante {codigo}: {matriz}")
        
        
def convertirMateriasACupos(materias):
    claves = list(materias.keys())
    valores = list(materias.values())
    cuposUnicos(claves,valores)
    
def cuposUnicos(claves,valores):
    contadores = [0] * len(claves)
    
    # Inicializa una matriz vacía para almacenar las combinaciones
    matriz_combinaciones = []
    
    # Bucle para generar todas las combinaciones posibles
    while True:
        # Añade la combinación actual a la matriz
        matriz_combinaciones.append(list(contadores))  # Añade una copia de los contadores actuales
    
        # Incrementa los contadores
        for i in range(len(contadores) - 1, -1, -1):
            if contadores[i] < valores[i]:
                contadores[i] += 1
                break
            else:
                contadores[i] = 0
    
        # Verifica si todos los contadores han vuelto a 0, lo que indica que todas las combinaciones posibles se han generado
        if all(c == 0 for c in contadores):
            break
        
    # Imprime la matriz
    for fila in matriz_combinaciones:
        print(fila)

def calcularInsatisfaccion(materias_asignadas, materias_solicitadas, prioridades):
    factor = 3 * materias_solicitadas - 1
    prioridad_total = sum(prioridades)
    
    insatisfaccion = (1 - materias_asignadas / materias_solicitadas) * (prioridad_total / factor)
    return insatisfaccion

# prioridades = [0, 1, 2, 0]
# materias_solicitadas = 3
# materias_asignadas = 3  

# insatisfaccion = calcularInsatisfaccion(materias_asignadas, materias_solicitadas, prioridades)
# print("Insatisfacción:", insatisfaccion)


inicio("./Pruebas/e_3_5_5.txt")