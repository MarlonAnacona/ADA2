from entradas import leer_archivo_txt
from itertools import product
import copy
from collections import defaultdict

matriz_combinaciones = []
calculoInteres={}


def inicio(nombre_archivo):
    k, r, M, E = leer_archivo_txt(nombre_archivo)
    rocPD(k, r, M, E)

def rocPD(k, r, M, E):

    #asignacionMaterias(convertirMateriasACupos(M),    convertirEstudiantesMateriasVectores(E,M))
    nuevo_estudiantes={}
    estudiantes=convertirEstudiantesMateriasVectores(E,M)

    asignaciones = [[m for m in est] for est in estudiantes.values()]
    indice=0
  #  asignacionMaterias(convertirMateriasACupos(M),estudiantes)
    
    for i in convertirMateriasACupos(M):
        print(asignar_materia( estudiantes,i, asignaciones,len(estudiantes)-1,indice))
        indice=indice+1
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

# def asignar_materia(estudiantes, materias, asignaciones, est_index,indice):
#     keys = list(estudiantes.keys()) 
#     # Usa una clave única para representar el estado actual de las materias y el índice del estudiante
#     key = (tuple(materias), est_index)  # tupla (tuple(materias), est_index)
#     #Copia de las asingaciones originales
#     asignaciones_copy = [list(asig) for asig in asignaciones]
#     #donde se guardara las insatifaciones
#     ins = []
#     # Si el resultado ya ha sido calculado, retórnalo
#     if key in memo:
#         return memo[key]
    
#     if est_index == 0 :
#         if indice==0:
#             result = calcular_insatisfaccion(asignaciones, estudiantes)
#             memo[key] = result
#             return  memo[key]  
#         else:    
#             result = calcular_insatisfaccion(asignaciones, estudiantes)
#             memo[key] = result
#             return  memo[key]      
        
#     if  sum(materias)==0:
#         result = calcular_insatisfaccion(asignaciones, estudiantes)
#         memo[key] = result
#         if indice==0:
#             ins.append(asignar_materia(estudiantes,materias, asignaciones_copy,est_index-1,indice)) 
#             result = min(ins)
#             return result

#         else:
#             return  memo[key]
       
    
#     asignaciones_copy = [list(asig) for asig in asignaciones]
#     ins = []
#     for i, materia in enumerate(materias):
#         if est_index >= 0:
#             if materia > 0:
#                 if estudiantes[keys[est_index]][i] != -1:
#                     materias[i] -= 1
#                     asignaciones_copy[est_index][i] = 0
#                     promedio_actual= (asignar_materia(estudiantes, materias, asignaciones_copy, est_index -1,indice))
#                     estudianteInsatifacion=calcularInsatisfaccion(asignaciones_copy[est_index])
#                     suma_total = promedio_actual * est_index
#                     nuevo_total = suma_total + estudianteInsatifacion
#                     nuevo_promedio = nuevo_total / (est_index+1)
#                     materias[i] += 1
#                     asignaciones_copy[est_index][i] =estudiantes[keys[est_index]][i]
#                 else:
#                     ins.append(asignar_materia(estudiantes, materias, asignaciones_copy, est_index -1,indice))
#             else:
#                 continue

#     result = min(ins)
#     memo[key] = result
#     return result


# def asignar_materia(estudiantes, materias, asignaciones, est_index=None):
#     if est_index is None:
#         est_index = len(estudiantes) - 1  # iniciar desde el último estudiante

#     if est_index < 0:
#         return calcular_insatisfaccion(asignaciones, estudiantes)

#     asignaciones_copy = [list(asig) for asig in asignaciones]
#     ins = []
#     estudiantes_keys = list(estudiantes.keys()) 
#     for i, materia in enumerate(materias):
#         clave_actual = estudiantes_keys[est_index]
#         if materia > 0 and estudiantes[clave_actual][i] != -1:
#             materias[i] -= 1
#             asignaciones_copy[est_index][i] = 0
#             ins.append(asignar_materia(estudiantes, materias, asignaciones_copy, est_index - 1))
#             # backtracking
#             materias[i] += 1
#             asignaciones_copy[est_index][i] = estudiantes[clave_actual][i]
#         else:
#             ins.append(asignar_materia(estudiantes, materias, asignaciones_copy, est_index - 1))
#     return min(ins)


# def asignar_materia(estudiantes, materias, asignaciones, est_index=0):
#     keys = list(estudiantes.keys())  # Lista de claves del diccionario estudiantes
#     if est_index == len(estudiantes):
#         return calcular_insatisfaccion(asignaciones, estudiantes)
#     asignaciones_copy = [list(asig) for asig in asignaciones]
#     ins = []
#     for i, materia in enumerate(materias):
#         if materia > 0 and estudiantes[keys[est_index]][i] != -1:  # Usa keys[est_index] para acceder a la clave correcta
#             materias[i] -= 1
#             asignaciones_copy[est_index][i] = 0
#             ins.append(asignar_materia(estudiantes, materias, asignaciones_copy, est_index + 1))
#             # backtracking
#             materias[i] += 1
#             asignaciones_copy[est_index][i] = estudiantes[keys[est_index]][i]  # Usa keys[est_index] para acceder a la clave correcta
#         else:
#             ins.append(asignar_materia(estudiantes, materias, asignaciones_copy, est_index + 1))
#     return min(ins)

# Llama a la función inicio para empezar


def asignar_materia():
    print("santi")

def asignar_materia2(estudiantes,materias,indiceEstudiante,indiceMateria):
    cantidadMa=0
    cantidadMs=0
    sumatoriaPriorizadaMn=0
    capacidadPriorizacion=0
    calculoInteres[str(cantidadMa)+str(cantidadMs)+str(sumatoriaPriorizadaMn)]
    insatisfacion=calculoInsatifacion2(cantidadMa,cantidadMs,sumatoriaPriorizadaMn,capacidadPriorizacion)
    insatisfacion=insatisfacion+asignar_materia2(estudiantes,materias,indiceEstudiante+1,indiceMateria)
    
    
def calculoInsatifacion2(cantidadMa,cantidadMs,sumatoriaPriorizadaMn,capacidadPriorizacion):
    insatisfaccion = (1 - cantidadMa/ cantidadMs) * (sumatoriaPriorizadaMn / capacidadPriorizacion)
    return insatisfaccion

inicio("./Pruebas/e_3_5_5.txt")


    
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
