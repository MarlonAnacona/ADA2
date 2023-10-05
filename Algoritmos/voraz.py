from pathlib import Path
import copy

def studentDissatisfaction(student, distribution, requests):

    request = set(requests[student])
    assignment = set(distribution[student])
    unassigned = request - assignment
    puntos_prioridad = 3 * len(request) - 1
    unassigned_points = 0

    if len(unassigned) <= len(request) // 2:
        unassigned_points = sum(requests[student][subject] for subject in unassigned)
    else:
        unassigned_points = puntos_prioridad
        unassigned_points -= sum(requests[student][subject] for subject in assignment)

    dissatisfaction = (1 - len(assignment) / len(request)) * (unassigned_points / puntos_prioridad)

    return dissatisfaction


def generalDissatisfaction(total_student, distribution, requests):
    general_dissatisfaction = 0

    for student in requests:
        general_dissatisfaction += studentDissatisfaction(student, distribution, requests)

    return general_dissatisfaction / total_student

# devuelve una pareja (A, FhM,Ei(A)) tal que A es la respuesta al problema
# rocV(k,r,M,E)
def rocV(total_subjects, total_student, asignaturas, requests):
  answer = {student: [] for student in requests}
  cuposRestantes = copy.deepcopy(asignaturas)
  
  students_sorted = sorted(requests.keys(), key=lambda student: sum(requests[student].values()), reverse=True)
  
  for student in students_sorted:
    courses_sorted = sorted(requests[student], key=lambda curso: -requests[student][curso])
    
    for curso in courses_sorted:
      if cuposRestantes[curso] > 0:
        answer[student].append(curso)
        cuposRestantes[curso] -= 1
  
  dissatisfaction = generalDissatisfaction(total_student, answer, requests)
  
  return [answer, dissatisfaction]

def readFile(nombreArchivo):
  with open(nombre_archivo_abrir, 'r') as entry:
    total_student
    total_subjects = int(entry.readline())
    subjects = {}
    requests = {}

    for i in range(0, total_subjects):
      subject = entry.readline()
      subject = subject.split(",")
      subjects[subject[0]] = int(subject[1])

    total_student = int(entry.readline())

    for estudiantes in range(0, total_student):
      
      student = entry.readline()
      student = student.split(",")

      new_student = {}
      cantidadAsignaturaEstudiante = int(student[1])
      
      for i in range (0, cantidadAsignaturaEstudiante):
        asigSolicitada = entry.readline()
        asigSolicitada = asigSolicitada.split(",")
        new_student[asigSolicitada[0]] = int(asigSolicitada[1].strip())

      requests[student[0]] = new_student

    entry.close()
    return total_subjects, total_student, subjects, requests

# readFile(nombre_archivo_abrir)
nombre_archivo_abrir = './Pruebas/e_3_10_5.roc'

k, r, M, E = readFile(nombre_archivo_abrir)
voraz = rocV(k, r, M, E)

print(voraz)