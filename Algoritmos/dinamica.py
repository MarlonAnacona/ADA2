from entradas import leer_archivo_txt


matriz_combinaciones = []

def inicio(nombre_archivo):
    k, r, M, E = leer_archivo_txt(nombre_archivo)
    rocPD(k, r, M, E)

def rocPD(k, r, M, E):

    asignacionMaterias(convertirMateriasACupos(M),    convertirEstudiantesMateriasVectores(E,M))
    return 0 

def convertirEstudiantesMateriasVectores(E,M):
  matrices_estudiantes = {}
  for codigo, (num_materias, materias) in E.items():
        # Crear una matriz para el estudiante actual, en caso de no haberla pedido dará -1
        matriz_estudiante = [-1] * len(M)
        for materia, valor in materias:
            # Usar el orden de la materia en el diccionario base para determinar la posición en la matriz
            indice = list(M.keys()).index(materia)
            matriz_estudiante[indice] = valor
        matrices_estudiantes[codigo] = matriz_estudiante

    # Imprimir las matrices de los estudiantes
  for codigo, matriz in matrices_estudiantes.items():
        print(f"Estudiante {codigo}: {matriz}")
  return matrices_estudiantes
        
        
def convertirMateriasACupos(materias):
    claves = list(materias.keys())
    valores = list(materias.values())
    return cuposUnicos(claves,valores)
    
def cuposUnicos(claves,valores):
    contadores = [0] * len(claves)
    
    # Inicializa una matriz vacía para almacenar las combinaciones
    
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
        
    return matriz_combinaciones
    
def obtenerCombinacionDeMatriz(matriz_combinaciones, indice):
    try:
        return matriz_combinaciones[indice]  # Retorna la combinación en la posición dada.
    except IndexError:
        return None  # Retorna None si el índice está fuera de rango.




def calcularInsatisfaccion(  prioridades):
    calculo=calcularmateriasAsignadasYSolicitadas(prioridades)
    factor = (3 * calculo[0]) - 1
    prioridad_total = calculo[2]
    insatisfaccion = (1 - calculo[1] / calculo[0]) * (prioridad_total / factor)
    return insatisfaccion



def calcularmateriasAsignadasYSolicitadas (prioridades):
    solicitadas = 0
    asignadas = 0
    suma= 0
    for elemento in prioridades:
        if elemento >= 0:
            solicitadas += 1
        if elemento == 0:
            asignadas += 1
        if isinstance(elemento, int) and elemento > 0:
            suma += elemento
    return solicitadas,asignadas,suma
   
   
   
def asignacionMaterias(materias,estudiantes):
   for indice in range(len(materias)):
    # Obtén la fila correspondiente usando la función
    fila = obtenerCombinacionDeMatriz(materias, indice)
    # Si la fila no es None, continúa
    if fila is not None:
        # Itera sobre cada estudiante en el diccionario
        for estudiante, valores in estudiantes.items():
            # Itera sobre cada elemento en la fila y los valores del estudiante
            for j, (valor_matriz, valor_estudiante) in enumerate(zip(fila, valores)):
                # Verifica la condición especificada
                if valor_matriz > 0 and valor_estudiante > -1:
                    # Asigna 0 al valor correspondiente del estudiante
                    estudiantes[estudiante][j] = 0

   for estudiante, valores in estudiantes.items():
    print(f"{estudiante}: {valores}") 

inicio("./Pruebas/e_3_5_5.txt")



