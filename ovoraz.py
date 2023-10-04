from pathlib import Path
import copy

asignaturasA = {}
solicitudesA = {}
cantidadEstudiantesA = 0
cantidadAsignaturasA = 0
nombre_archivo_abrir = './Pruebas/e_4_30_15.roc'

def inconformidadEstudiante(estudiante, distribucion, solicitudes):
    solicitud = set(solicitudes[estudiante])
    asignacion = set(distribucion[estudiante])
    no_asignadas = solicitud - asignacion
    puntos_prioridad = 3 * len(solicitud) - 1
    puntos_no_asignados = 0

    if len(no_asignadas) <= len(solicitud) // 2:
        puntos_no_asignados = sum(solicitudes[estudiante][materia] for materia in no_asignadas)
    else:
        puntos_no_asignados = puntos_prioridad
        puntos_no_asignados -= sum(solicitudes[estudiante][materia] for materia in asignacion)

    inconformidad = (1 - len(asignacion) / len(solicitud)) * (puntos_no_asignados / puntos_prioridad)

    return inconformidad


def inconformidadTotal(cantidadEstudiantes, distribucion, solicitudes):
    inconformidadGeneral = 0

    for estudiante in solicitudes:
        inconformidadGeneral += inconformidadEstudiante(estudiante, distribucion, solicitudes)

    return inconformidadGeneral / cantidadEstudiantes

def rocV(cantidadAsignaturas, cantidadEstudiantes, asignaturas, solicitudes):
  solucion = {estudiante: [] for estudiante in solicitudes}
  cuposRestantes = copy.deepcopy(asignaturas)
  
  students_sorted = sorted(solicitudes.keys(), key=lambda estudiante: sum(solicitudes[estudiante].values()), reverse=True)
  
  for estudiante in students_sorted:
    courses_sorted = sorted(solicitudes[estudiante], key=lambda curso: -solicitudes[estudiante][curso])
    
    for curso in courses_sorted:
      if cuposRestantes[curso] > 0:
        solucion[estudiante].append(curso)
        cuposRestantes[curso] -= 1
  
  inconformidad = inconformidadTotal(cantidadEstudiantes, solucion, solicitudes)
  
  return [solucion, inconformidad]

def lecturaArchivo(nombreArchivo):
  global cantidadAsignaturasA, cantidadEstudiantesA
with open(nombre_archivo_abrir, 'r') as entrada:

  cantidadAsignaturasA = int(entrada.readline())

  for lineas in range(0, cantidadAsignaturasA):
    linea = entrada.readline()
    linea = linea.split(",")
    asignaturasA[linea[0]] = int(linea[1])

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

    solicitudesA[estudiante[0]] = nuevoEstudiante

  entrada.close()

lecturaArchivo(nombre_archivo_abrir)

voraz = rocV(cantidadAsignaturasA, cantidadEstudiantesA, asignaturasA, solicitudesA)
print(voraz)
