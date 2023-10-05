import time
# materias ={}
# asignacion = {}
# cantidadEstudiantesA = 0
# cupos = 0
# nombre_archivo_abrir = './Pruebas/e_3_5_5.roc'

# Función que calcula la inconformidad individual de un estudiante con respecto a su asignación de asignaturas.
def inconformidadIndividual(estudiante, distribucion, solicitudes):

    solicitud = list(solicitudes[estudiante])
    asignacion = list(distribucion[estudiante])
    no_asignadas = [materia for materia in solicitud if materia not in asignacion]
    puntos_prioridad = 3 * findLength(solicitud) - 1
    puntos_no_asignados = 0



    if findLength(no_asignadas) <= findLength(solicitud) // 2:
        puntos_no_asignados = sum(solicitudes[estudiante][materia] for materia in no_asignadas)
    else:
        puntos_no_asignados = puntos_prioridad
        puntos_no_asignados -= sum(solicitudes[estudiante][materia] for materia in asignacion)

    inconformidad = (1 - findLength(asignacion) / findLength(solicitud)) * (puntos_no_asignados / puntos_prioridad)

    return inconformidad


# Función que calcula la inconformidad total promedio entre todos los estudiantes en una posible asignación de asignaturas.
def inconformidadTotal(cantidadEstudiantes, posibleAsignacion, solicitudes):
    inconformidadGeneral = 0
    totalEstudiantes = 0

    for estudiante in solicitudes:
        inconformidadGeneralEstudiante = inconformidadIndividual(estudiante, posibleAsignacion, solicitudes)
        inconformidadGeneral += inconformidadGeneralEstudiante
        totalEstudiantes += 1

    return inconformidadGeneral / totalEstudiantes

# Función que genera todas las permutaciones posibles de un conjunto de elementos.
def permutacion(*args):
    
    if not args:
        return [()]
    
    result = [[]]
    for iterable in args:
        new_result = []
        for combination in result:
            for item in iterable:
                new_result.append(combination + [item])
        result = new_result
    
    return [tuple(combination) for combination in result]


# Función que implementa la funcionalidad de combinaciones sin repetición.
def combinations(iterable, r):
    items = list(iterable)
    n = len(items)
    
    if r > n:
        return []

    indices = list(range(r))
    combinations_list = [tuple(items[i] for i in indices)]

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return combinations_list

        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1

        combinations_list.append(tuple(items[i] for i in indices))

    
# Función que genera combinaciones de asignaturas para un curso específico.
def combinacionesAsignatura(materia, asignaturas, solicitudes):

  elementos = [e for e, asignacion in solicitudes.items() if materia in asignacion]
  combinaciones = []

  if asignaturas[materia] > findLength(elementos):
    combinaciones.append(tuple(elementos)) 
  else:
    combinaciones = list(combinations(elementos, asignaturas[materia]))
  
  return combinaciones

# Función que genera todas las combinaciones posibles de asignaturas para todos los cursos.
def combinacionesPosibles(asignaturas, solicitudes):

  clavesAsignaturas = list(asignaturas.keys())
  opcionesCombinar = []

  for asignatura in clavesAsignaturas:
    opcionesCombinar.append(combinacionesAsignatura(asignatura, asignaturas, solicitudes))

  opciones = list(permutacion(*opcionesCombinar))
  return opciones

import time

# Función que implementa el algoritmo de fuerza bruta para encontrar la asignación óptima.
def rocFB(cantidadAsignaturas, cantidadEstudiantes, asignaturas, solicitudes):
    tiempo_inicio = time.time()
    clavesAsignaturas = list(asignaturas.keys())
    opciones = combinacionesPosibles(asignaturas, solicitudes)

    mejorOpcion = {}
    inconformidad = 1

    for opcion in range(0, findLength(opciones)):
        posibleOpcion = {estudiante: [] for estudiante in solicitudes}

        for asignatura in range(0, cantidadAsignaturas):
            for estudiante in list(opciones[opcion][asignatura]):
                posibleOpcion[estudiante].append(clavesAsignaturas[asignatura])

        posibleInconformidad = inconformidadTotal(cantidadEstudiantes, posibleOpcion, solicitudes)

        if posibleInconformidad < inconformidad:
            mejorOpcion = posibleOpcion
            inconformidad = posibleInconformidad
    
    tiempo_fin = time.time()
    tiempo_ejecucion = tiempo_fin - tiempo_inicio
    print(f"Tiempo de ejecución de rocFB: {tiempo_ejecucion} segundos")
    
    return [mejorOpcion, inconformidad]





# Function which return length of string
def findLength(string):
 
    # Initialize count to zero
    count = 0
 
    # Counting character in a string
    for i in string:
        count += 1
    # Returning count
    return count



def Entrada(nombre_archivo_abrir):
    global cupos, cantidadEstudiantesA, materias, asignacion
    materias = {}  # Debes definir el diccionario materias
    asignacion = {}  # Debes definir el diccionario asignacion
    
    with open(nombre_archivo_abrir, 'r') as entrada:
        cupos = int(entrada.readline())

        for lineas in range(0, cupos):
            linea = entrada.readline()
            linea = linea.split(",")
            materias[linea[0]] = int(linea[1])

        cantidadEstudiantesA = int(entrada.readline())

        for estudiantes in range(0, cantidadEstudiantesA):
            estudiante = entrada.readline()
            estudiante = estudiante.split(",")

            nuevoEstudiante = {}
            cantidadAsignaturaEstudiante = int(estudiante[1])

            for linea in range(0, cantidadAsignaturaEstudiante):
                asigSolicitada = entrada.readline()
                asigSolicitada = asigSolicitada.split(",")
                nuevoEstudiante[asigSolicitada[0]] = int(asigSolicitada[1].strip())

            asignacion[estudiante[0]] = nuevoEstudiante

    entrada.close()
    return cupos, cantidadEstudiantesA, materias, asignacion



# entradita = Entrada(nombre_archivo_abrir)
# print("return entrada",entradita)
# BrutalForce = rocFB(cupos,cantidadEstudiantesA,materias,asignacion)
# print(BrutalForce[0])
# print(BrutalForce[1])