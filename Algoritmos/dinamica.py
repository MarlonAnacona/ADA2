# from entradas import leer_archivo_txt
import copy
from collections import defaultdict

import itertools

matriz_combinaciones = []
calculoInteres={}


# def inicio(nombre_archivo):
#     k, r, M, E = leer_archivo_txt(nombre_archivo)
#     rocPD(k, r, M, E)



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
  return matrices_estudiantes
        

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
   

memo = {}  # Diccionario para almacenar resultados previos

respuesta=[]

def asignar_materia(estudiante, vectorCupos, memo={}):

    if len(estudiante) == 0:
        return 0, []
    
    last_key = next(reversed(estudiante.keys()))
    last_value = estudiante[last_key]

    key = (last_key, tuple(vectorCupos)) 

    if key in memo:
        return memo[key]
    
    if sum(vectorCupos) == 0:
        return 1, []

    estudianteCopy = estudiante.copy()
    estudianteCopy.popitem()

    ins = []
    caminos_completos = []

    for camino in calcularCaminosPosibles(last_value, vectorCupos):
        result = restar_unidad_si_condicion(camino, vectorCupos)

        ins_actual, camino_anterior = asignar_materia(estudianteCopy, result, memo)
        
        if len(estudiante) == 1:
            insG = (calcularInsatisfaccion(camino) + (ins_actual * len(estudiante))) / len(estudiante)
        else:
            insG = (calcularInsatisfaccion(camino) + (ins_actual * (len(estudiante)-1))) / len(estudiante)

        ins.append(insG)
        caminos_completos.append([{last_key: camino}] + camino_anterior)  # Añadir el camino actual al camino anterior como un diccionario
        
    min_ins = min(ins)
    min_index = ins.index(min_ins)
    
    # Guardar el resultado en memo
    memo[key] = (min_ins, caminos_completos[min_index])
    return memo[key]




    
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
    si vector1[i] es 0, resta 1 a vector2[i]. Si vector1[i] es diferente de 0,
    no modifica vector2[i].

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
        # Si el elemento en vector1 es 0...
        if vector1[i] == 0:
            # ...y el elemento correspondiente en result_vector es mayor que 0...
            if result_vector[i] > 0:
                # ...resta 1 al elemento en result_vector.
                result_vector[i] -= 1
            # Si el elemento en result_vector ya es 0 o negativo, lo mantiene como está
            else:
                result_vector[i] = result_vector[i]
        # Si el elemento en vector1 es diferente de 0, no modifica result_vector[i]
        else:
            result_vector[i] = result_vector[i]
    
    return result_vector

# estudiante={
#      1000: [3, 2, -1],
#  1001: [1, 2, 5],
#      1003: [3, -1, 2],
# }
# print(asignar_materia(estudiante,[2,0,0]))


# inicio("./Pruebas/e_3_5_5.roc")

def resultado(resultado1, resultado2):
    # Crear un diccionario que mapea las materias a sus asignaciones
    asignaciones = {}
    for i, asignacion in enumerate(resultado1[1]):
        materia = list(asignacion.keys())[0]
        ceros = asignacion[materia]
        asignaciones[materia] = [resultado2[j] for j in range(len(ceros)) if ceros[j] == 0]

    # Construir la lista de resultados en el formato deseado
    resultado_final = []
    for i, asignacion in enumerate(resultado1[1]):
        materia = list(asignacion.keys())[0]
        asignados = asignaciones[materia]
        resultado_final.append({materia: asignados})
    resultado_invertido = resultado_final[::-1]

    salida = [(resultado1[0], resultado_invertido)]

    return salida


# k, r, M, E = leer_archivo_txt("./Pruebas/e_3_5_5.roc")
# estudiantes=convertirEstudiantesMateriasVectores(E,M)
# cupos = list(M.values())
# resultado1 = asignar_materia(estudiantes, cupos)
# resultado2 = list(M.keys())
# resultado_final = resultado(resultado1, resultado2)
# print(resultado_final)


def guardar_resultado_como_txt(resultado):
    resultado_txt = ""
    for tupla in resultado:
        valor = tupla[0]
        asignaciones = tupla[1]

        # Agregar el valor a la cadena de texto
        resultado_txt += f'{valor}\n'

        # Iterar a través de las asignaciones y agregarlas a la cadena de texto
        for asignacion in asignaciones:
            materia = list(asignacion.keys())[0]
            asignados = asignacion[materia]

            # Agregar la materia y la cantidad de asignados a la cadena de texto
            resultado_txt += f'{materia},{len(asignados)}\n'

            # Agregar cada asignado en líneas separadas a la cadena de texto
            for asignado in asignados:
                resultado_txt += f'{asignado}\n'

    # Retornar la cadena de texto resultante
    return resultado_txt

# resultado_txt = guardar_resultado_como_txt(resultado_final)


def rocPD(k, r, M, E):

    estudiantes=convertirEstudiantesMateriasVectores(E,M)
    cupos = list(M.values())
    resultado1 = asignar_materia(estudiantes, cupos)
    resultado2 = list(M.keys())
    
    return guardar_resultado_como_txt(resultado(resultado1, resultado2))
