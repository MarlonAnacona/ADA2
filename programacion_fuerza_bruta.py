# Auxiliary function which return length of string
def findLength(string):
 
    # Initialize count to zero
    count = 0
 
    # Counting character in a string
    for i in string:
        count += 1
    # Returning count
    return count


# Función que calcula la inconformidad individual de un estudiante con respecto a su asignación de asignaturas.
def insatisfaccionIndividual(estudiante, reparticion, solicitudes):

    solicitud = list(solicitudes[estudiante])
    asignacion = list(reparticion[estudiante])
    no_asignadas = [materia for materia in solicitud if materia not in asignacion]
    puntos_prioridad = 3 * findLength(solicitud) - 1
    puntos_no_asignados = 0



    if findLength(no_asignadas) <= findLength(solicitud) / 2:
        puntos_no_asignados = sum(solicitudes[estudiante][materia] for materia in no_asignadas)
    else:
        puntos_no_asignados = puntos_prioridad
        puntos_no_asignados -= sum(solicitudes[estudiante][materia] for materia in asignacion)

    inconformidad = (1 - findLength(asignacion) / findLength(solicitud)) * (puntos_no_asignados / puntos_prioridad)

    return inconformidad


# Función que calcula la inconformidad total promedio entre todos los estudiantes en una posible asignación de asignaturas.
def insatisfaccionGeneral(posibleAsignacion, solicitudes):
    inconformidadGeneral = 0
    totalEstudiantes = 0

    for estudiante in solicitudes:
        inconformidadGeneralEstudiante = insatisfaccionIndividual(estudiante, posibleAsignacion, solicitudes)
        inconformidadGeneral += inconformidadGeneralEstudiante
        totalEstudiantes += 1

    return inconformidadGeneral / totalEstudiantes

# Función que genera todas las permutaciones posibles de un conjunto de elementos.
def permutacion(*elementos):
    
    if not elementos:
        return [()]
    
    result = [[]]
    for iterable in elementos:
        new_result = []
        for combination in result:
            for item in iterable:
                new_result.append(combination + [item])
        result = new_result
    
    return [tuple(combination) for combination in result]


def generarCombinacionesAsignatura(codigo, materia, peticion):
    elementos = [e for e, asignacion in peticion.items() if codigo in asignacion]
    combinaciones = []

    if materia[codigo] > findLength(elementos):
        combinaciones.append(tuple(elementos)) 
    else:
        items = list(elementos)
        n = len(items)
        r = materia[codigo]

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

    return combinations_list

def candidatosPermutacion(materias, peticiones):
    cursoKey = list(materias.keys())
    opcionesCombinar = [generarCombinacionesAsignatura(curso, materias, peticiones) for curso in cursoKey]
    opciones = list(permutacion(*opcionesCombinar))
    return opciones



def rocFB(materias, asignacion, peticion):
    asignacionKeys = list(asignacion.keys())
    escogencias = candidatosPermutacion(asignacion, peticion)

    escogenciaFinal = {}
    insatisfaccion = 1

    eleccion = 0
    while eleccion < len(escogencias):
        candidatoEscogencia = {estudiante: [] for estudiante in peticion}

        curso = 0
        while curso < materias:
            for estudiante in list(escogencias[eleccion][curso]):
                candidatoEscogencia[estudiante].append(asignacionKeys[curso])
            curso += 1

        insatisfaccionPosible = insatisfaccionGeneral(candidatoEscogencia, peticion)

        if insatisfaccionPosible < insatisfaccion:
            escogenciaFinal = candidatoEscogencia
            insatisfaccion = insatisfaccionPosible

        eleccion += 1

    return [escogenciaFinal, insatisfaccion]




materias ={}
asignacion = {}
cantidadEstudiantesA = 0
cupos = 0
nombre_archivo_abrir = 'entradas1.txt'

def Entrada(nombreArchivo):

  global cupos, cantidadEstudiantesA
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
    
    for linea in range (0, cantidadAsignaturaEstudiante):
      asigSolicitada = entrada.readline()
      asigSolicitada = asigSolicitada.split(",")
      nuevoEstudiante[asigSolicitada[0]] = int(asigSolicitada[1].strip())

    asignacion[estudiante[0]] = nuevoEstudiante

  entrada.close()



Entrada(nombre_archivo_abrir)

BrutalForce = rocFB(cupos, materias,asignacion)
print(BrutalForce[0])
print(BrutalForce[1])
