from entradas import leer_archivo_txt
import copy
from collections import defaultdict

import itertools

matriz_combinaciones = []
calculoInteres={}


def inicio(nombre_archivo):
    k, r, M, E = leer_archivo_txt(nombre_archivo)
    rocPD(k, r, M, E)

def rocPD(k, r, M, E):

    #asignacionMaterias(convertirMateriasACupos(M),    convertirEstudiantesMateriasVectores(E,M))
    nuevo_estudiantes={}
    estudiantes=convertirEstudiantesMateriasVectores(E,M)
    cupos = list(M.values())
    print(asignar_materia(estudiantes,cupos))
   


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
   
   
def matricular(cupos, solicitudes, materia=0, estado=None):
    if estado is None:
        estado = {est: list(valores) for est, valores in solicitudes.items()}  # Inicialización con valores iniciales

    if materia == len(cupos):
        yield copy.deepcopy(estado)
        return

    estudiantes_posibles = [e for e in solicitudes.keys()]
    for estudiante in estudiantes_posibles:
        if cupos[materia] > 0 and estado[estudiante][materia] != -1:  # Usando estado en lugar de valores_iniciales
            cupos[materia] -= 1
            valor_original = estado[estudiante][materia]  # Guardar el valor original
            estado[estudiante][materia] = 0  # Matriculado
            yield from matricular(cupos, solicitudes, materia, estado)
            cupos[materia] += 1
            estado[estudiante][materia] = valor_original  # Restaurar el valor original

    yield from matricular(cupos, solicitudes, materia + 1, estado)

   
def asignacionMaterias(materias, estudiantes):
    matriz_insatisfacciones = []  # Matriz para almacenar la insatisfacción para cada combinación
    estudiantes_acumulados = {}
    insatisfaccion_promedio=0
    print (estudiantes)
    for indice in range(len(materias)):
        estudiantes_acumulados.clear()
        fila = obtenerCombinacionDeMatriz(materias, indice)
        for estudiante, valores in estudiantes.items():
            estudiantes_acumulados.update({estudiante:valores})
            if fila is not None:
                total_insatisfaccion = 0
                total_estudiantes = 0
                menorPromedio=[]
                combinaciones=list(matricular(fila,estudiantes_acumulados))
                for i, combinacion in enumerate(combinaciones, 1):
                    total_insatisfaccion = 0
                    total_estudiantes = 0
                    for estudiante, materiasEstudiante in combinacion.items():
                        insatisfaccion = calcularInsatisfaccion(materiasEstudiante)
                        total_insatisfaccion += insatisfaccion
                        total_estudiantes += 1
                    insatisfaccion_promedio = total_insatisfaccion / total_estudiantes
                    menorPromedio.append(insatisfaccion_promedio)
                print(min(menorPromedio))
            matriz_insatisfacciones.append(insatisfaccion_promedio)


def calcular_insatisfaccion(asignaciones, estudiantes):
    ins_general = 0
    num_estudiantes = len(estudiantes)
    for estudiante, materias in zip(estudiantes, asignaciones):
       ins_general+=calcularInsatisfaccion(materias) 
    return ins_general / num_estudiantes

memo = {}  # Diccionario para almacenar resultados previos



def asignar_materia(estudiante, vectorCupos, memo={}):

    if len(estudiante) == 0:
        return 0
    
    last_key = next(reversed(estudiante.keys()))
    last_value = estudiante[last_key]

    # Usar tupla para que sea hashable y se pueda usar como clave en dict
    key = (last_key, tuple(vectorCupos)) 

    # Chequear si el resultado ya fue calculado
    if key in memo:
        return memo[key]
    
    if sum(vectorCupos) == 0:
        return 1
    

    
   
    estudianteCopy = estudiante.copy()
    last_item=estudianteCopy.popitem()
    for camino in calcularCaminosPosibles(last_value, vectorCupos):
        result = restar_unidad_si_condicion(camino, vectorCupos)
        ins = []

        if(len(estudiante)>0):
            if(len(estudiante)==1):
                insG = (
                    calcularInsatisfaccion(camino)
                    + ((asignar_materia(estudianteCopy, result, memo)) * (len(estudiante)))
                ) / len(estudiante)
            else:
                insG = (
                    calcularInsatisfaccion(camino)
                    + ((asignar_materia(estudianteCopy, result, memo)) * (len(estudiante)-1))
                ) / len(estudiante)
            ins.append(insG)
        
    
    # Guardar el resultado en el diccionario antes de retornar
    memo[key] = min(ins)
    return min(ins)

    
def calcularCaminosPosibles(estudiante,cupos):
    non_neg_one_positions = [i for i, x in enumerate(estudiante) if x != -1 and cupos[i] != 0]

# Generamos todas las combinaciones posibles de esas posiciones
    for length in range(len(non_neg_one_positions) + 1):
        for subset in itertools.combinations(non_neg_one_positions, length):
            new_vector = estudiante.copy()
            for index in subset:
                new_vector[index] = 0
            yield new_vector


def restar_unidad_si_condicion(vector1, vector2):
    """
    Esta función recibe dos vectores y, para cada posición i, 
    si vector1[i] > 0 y vector2[i] > 0, resta 1 a vector2[i].

    :param vector1: list, primer vector para chequear la condición.
    :param vector2: list, segundo vector para restar las unidades.
    :return: list, vector2 modificado.
    """
    # Asegurarte de que los vectores tienen la misma longitud
    if len(vector1) != len(vector2):
        raise ValueError("Los vectores deben tener la misma longitud")

    # Crear una copia de vector2 para no modificar el original
    result_vector = vector2.copy()
    
    for i in range(len(vector1)):
        # Si el elemento en vector1 es mayor que 0...
        if vector1[i] > 0:
            # ...y el elemento correspondiente en result_vector es mayor que 0...
            if result_vector[i] > 0:
                # ...resta 1 al elemento en result_vector.
                result_vector[i] -= 1
            # Si el elemento en result_vector ya es 0, lo mantiene como está
            else:
                result_vector[i] = 0
    
    return result_vector

estudiante={
     1000: [3, 2, -1],
 1001: [1, 2, 5],
     1003: [3, -1, 2],
}
print(asignar_materia(estudiante,[2,0,0]))


#inicio("./Pruebas/e_3_5_5.txt")


    
    # for i, sublista in enumerate(vectorCupos):
    #     for j, elemento in enumerate(sublista):
    #         if elemento > 0 and estudiantes[est_index][j] != -1:
    #             materias[i] -= 1
    #             asignaciones_copy[est_index][i] = 0
    #             #En caso de que matricule
    #             if(i-1<0):
    #                ins.append(asignar_materia(estudiantes, asignaciones_copy,vectorCupos, est_index -1,vectorCupos[i])) 
    #             else:
    #                 ins.append(asignar_materia(estudiantes, asignaciones_copy,vectorCupos, est_index -1,vectorCupos[i-1]))    
                
    #             materias[i] += 1
    #             asignaciones_copy[est_index][i] = estudiantes[est_index][i]
    #         else:
    #             #En caso de que no
    #             ins.append(asignar_materia(estudiantes, asignaciones_copy,vectorCupos, est_index -1,materias))
