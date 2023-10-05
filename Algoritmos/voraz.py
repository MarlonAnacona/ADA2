import time
import copy

def studentDissatisfaction(student, distribution, requests):

    request = set(requests[student])
    assignment = set(distribution[student])
    unassigned = request - assignment
    priority_points = 3 * len(request) - 1
    unassigned_points = 0

    if len(unassigned) <= len(request) // 2:
        unassigned_points = sum(requests[student][subject] for subject in unassigned)
    else:
        unassigned_points = priority_points
        unassigned_points -= sum(requests[student][subject] for subject in assignment)

    dissatisfaction = (1 - len(assignment) / len(request)) * (unassigned_points / priority_points)

    return dissatisfaction

def generalDissatisfaction(total_student, distribution, requests):
    general_dissatisfaction = 0

    for student in requests:
        general_dissatisfaction += studentDissatisfaction(student, distribution, requests)

    return general_dissatisfaction / total_student

def format_output(data):
    # Separa los datos en las dos partes
    dictionary, number = data

    # Redondea el número a tres decimales
    number_str = f'{number:.3f}'

    # Inicializa una lista para almacenar las líneas del resultado
    result = [number_str]

    # Recorre el diccionario y su valor correspondiente
    for key, values in dictionary.items():
        key_line = f'{key},{len(values)}'
        result.append(key_line)
        result.extend(values)

    # Convierte las líneas en una cadena de texto separada por saltos de línea
    output = '\n'.join(result)

    return output

def rocV(total_subjects, total_student, subjects, requests):
  tiempo_inicio = time.time()
  answer = {student: [] for student in requests}
  cuposRestantes = copy.deepcopy(subjects)
  
  students_sorted = sorted(requests.keys(), key=lambda student: sum(requests[student].values()), reverse=False)
  
  for student in students_sorted:
    courses_sorted = sorted(requests[student], key=lambda course: -requests[student][course])
    
    for course in courses_sorted:
      if cuposRestantes[course] > 0:
        answer[student].append(course)
        cuposRestantes[course] -= 1
  
  dissatisfaction = generalDissatisfaction(total_student, answer, requests)

  result = [answer, dissatisfaction]
  output = format_output(result)
  tiempo_fin = time.time()
  tiempo_ejecucion = tiempo_fin - tiempo_inicio
  print(f"Tiempo de ejecución de rocV: {tiempo_ejecucion:.6f} segundos")
  return output



# file = './Pruebas/e_3_5_5.roc'

# k, r, M, E = readFile(file)
# voraz = rocV(k, r, M, E)

# print(voraz)