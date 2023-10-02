# def calculate_insatisfaction(assignment, M, E):
#     total_insatisfaction = 0
#     total_students = len(E)
    
#     for estudiante, (materias_solicitadas, materias_prioridades) in E.items():
#         insatisfaction_per_student = 0
        
#         for materia, prioridad in materias_prioridades:
#             # Calcula la insatisfacción por materia
#             if materia in [m[0] for m in assignment.get(estudiante, [])]:
#                 cupo_asignado = next(item[1] for item in assignment[estudiante] if item[0] == materia)
#                 insatisfaction_per_student += (1 - cupo_asignado / materias_solicitadas) * (prioridad / (3 * materias_solicitadas - 1))
        
#         total_insatisfaction += insatisfaction_per_student
    
#     return total_insatisfaction 

    
# def assign_materias(k, r, M, E, assignment, memo):
#     if len(assignment) == r:
#         return calculate_insatisfaction(assignment, M, E)
    
#     estudiante = list(E.keys())[len(assignment)]
#     min_insatisfaction = float('inf')
    
#     # Asegúrate de que el estudiante esté registrado en el diccionario de asignaciones
#     if estudiante not in assignment:
#         assignment[estudiante] = []
    
#     for materia, cupo in M.items():
#         if cupo > 0:
#             assignment[estudiante].append((materia, cupo))
#             M[materia] -= 1
            
#             insatisfaction = assign_materias(k, r, M, E, assignment, memo)
            
#             if insatisfaction < min_insatisfaction:
#                 min_insatisfaction = insatisfaction
            
#             assignment[estudiante].pop()
#             M[materia] += 1
    
#     memo[len(assignment)] = min_insatisfaction
#     return min_insatisfaction

# def rocPD(k, r, M, E):
#     assignment = {}
#     memo = {}
#     min_insatisfaction = assign_materias(k, r, M, E, assignment, memo)
    
#     print("Asignaciones realizadas:")
#     for estudiante, materias_asignadas in assignment.items():
#         print(f"Estudiante {estudiante}: {materias_asignadas}")
    
#     return min_insatisfaction

# # Ejemplo de uso
# k = 3
# r = 5
# M = {100: 1, 101: 3, 102: 2}
# E = {
#     1000: (2, [(100, 3), (101, 2)]),
#     1001: (3, [(102, 5), (100, 1), (101, 2)]),
#     1002: (2, [(100, 3), (102, 2)]),
#     1003: (1, [(102, 2)]),
#     1004: (2, [(100, 1), (101, 4)])
# }

# min_insatisfaction = rocPD(k, r, M, E)
# print("Mínima insatisfacción general:", min_insatisfaction)







# def rocPD(k, r, M, E):
#     dp = [[0] * (k + 1) for _ in range(r + 1)]

#     for i in range(1, r + 1):
#         for j in range(1, k + 1):
#             min_cost = float('inf')
#             for materia, priority in E[1000][1]:
#                 if j >= M[materia]:  # Verifica si hay cupos disponibles
#                     costo_asignacion = (1 - j / E[1000][0]) * (priority / (3 * E[1000][0] - 1))
#                     min_cost = min(min_cost, dp[i - 1][j - M[materia]] + costo_asignacion)
#             dp[i][j] = min(min_cost, dp[i - 1][j])

#     costo_minimo = dp[r][k]
#     asignaciones = []

#     i, j = r, k
#     while i > 0 and j > 0:
#         min_cost = dp[i][j]
#         for materia, priority in E[1000][1]:
#             if j >= M[materia] and min_cost == dp[i - 1][j - M[materia]] + ((1 - j / E[1000][0]) * (priority / (3 * E[1000][0] - 1))):
#                 asignaciones.append((i, materia))
#                 i -= 1
#                 j -= M[materia]
#                 break
#         else:
#             i -= 1

#     asignaciones.reverse()
#     return costo_minimo, asignaciones



# def calculate_insatisfaction(student_preferences, assigned_courses):
#     # Calcula la insatisfacción de un estudiante dada sus preferencias y las asignaciones.
#     total_assigned_courses = len(assigned_courses)
#     total_requested_courses = len(student_preferences)
#     insatisfaction = 0

#     for i in range(total_assigned_courses):
#         course, priority = assigned_courses[i]
#         insatisfaction += (1 - (i + 1) / total_requested_courses) * (priority / (3 * total_requested_courses - 1))

#     return insatisfaction

# def rocPD(k, r, M, E):
#     # Inicializa una matriz para almacenar los resultados intermedios.
#     dp = [[float('inf')] * (k + 1) for _ in range(r + 1)]
#     print(dp)
#     dp[0][0] = 0  # Caso base: ningún estudiante, ninguna materia.

#     for i in range(1000, r + 1000):
#         for j in range(k + 1):
#             # Prueba todas las combinaciones posibles de asignaciones para el estudiante i.
#             for assignment in range(1 << len(E[i][1])):
#                 assigned_courses = []
#                 total_assigned_courses = 0

#                 for l, (course, priority) in enumerate(E[i][1]):
#                     if assignment & (1 << l):
#                         assigned_courses.append((course, priority))
#                         total_assigned_courses += 1

#                 if total_assigned_courses <= j:
#                     # Actualiza el costo mínimo para este subproblema.
#                     insatisfaction = calculate_insatisfaction(E[i][1], assigned_courses)
#                     dp[i][j] = min(dp[i][j], dp[i - 1000][j - total_assigned_courses] + insatisfaction)

#     # El resultado óptimo estará en dp[r][k].
#     return dp[r][k]





# def calcular_insatisfaccion(estudiantes, asignaciones, r):
#     insatisfaccion = 0.0
#     for estudiante in estudiantes:
#         cant_materias_solicitadas, solicitudes = estudiantes[estudiante]
#         insatisfaccion_estudiante = 0.0
#         materias_asignadas = set(asignaciones.get(estudiante, []))
#         for materia, prioridad in solicitudes:
#             if materia not in materias_asignadas:
#                 insatisfaccion_estudiante += (1 - len(materias_asignadas) / cant_materias_solicitadas) * (prioridad / (3 * cant_materias_solicitadas - 1))
#         insatisfaccion += insatisfaccion_estudiante
#     return insatisfaccion / r

# def rocPD(k, r, M, E):
#     asignaciones = {}
#     return asignar_materias(k, r, M, E, asignaciones, 0)

# def asignar_materias(k, r, M, E, asignaciones, estudiante_idx):
#     # print(E.keys())
#     if estudiante_idx == r:
#         return calcular_insatisfaccion(E, asignaciones, k, r)
    
#     mejor_insatisfaccion = float('inf')
    
#     for materia, cupos in M.items():
#         print(materia, cupos)
#         if cupos > 0:
#             estudiante, solicitudes = E[0]
#             print(estudiante, solicitudes)
#             if materia in [m[0] for m in solicitudes]:
#                 asignaciones[estudiante] = asignaciones.get(estudiante, []) + [materia]
#                 M[materia] -= 1
#                 insatisfaccion = asignar_materias(k, r, M, E, asignaciones, estudiante_idx + 1)
#                 M[materia] += 1
#                 asignaciones[estudiante].remove(materia)
#                 mejor_insatisfaccion = min(mejor_insatisfaccion, insatisfaccion)
#                 print("soy asig",asignaciones)
    
#     return mejor_insatisfaccion

# # Ejemplo de uso
# k = 3
# r = 5
# M = {100: 1, 101: 3, 102: 2}
# E = {
#     1000: (2, [(100, 3), (101, 2)]),
#     1001: (3, [(102, 5), (100, 1), (101, 2)]),
#     1002: (2, [(100, 3), (102, 2)]),
#     1003: (1, [(102, 2)]),
#     1004: (2, [(100, 1), (101, 4)])
# }

# resultado = rocPD(k, r, M, E)
# print("Insatisfacción mínima:", resultado)

import numpy as np

import numpy as np

def calcular_insatisfaccion(cant_materias_asignadas, cant_materias_solicitadas, suma_prioridades):
    insatisfaccion = (1 - cant_materias_asignadas / cant_materias_solicitadas) * (suma_prioridades / (3 * cant_materias_solicitadas - 1))
    print("materia_asignada",cant_materias_asignadas)
    print("materia_solicitada",cant_materias_solicitadas)
    print("suma_prioridades",suma_prioridades)
    print(insatisfaccion)
    return insatisfaccion

def asignar_materias(estudiantes, materias):
    num_estudiantes = len(estudiantes)
    num_materias = len(materias)
    
    # Inicializar la tabla de programación dinámica con valores altos
    dp = np.full((num_estudiantes + 1, num_materias + 1), float('inf'))
    dp[0][0] = 0
    
    # Iterar a través de los estudiantes y materias
    for i in range(1, num_estudiantes + 1):
        for j in range(1, num_materias + 1):
            estudiante = estudiantes[i - 1]
            materia = materias[j - 1]
            
            # Calcular la insatisfacción si se asigna la materia al estudiante
            cant_materias_solicitadas = estudiante[1][0]
            prioridades = [p[1] for p in estudiante[1][1]]
            insatisfaccion = calcular_insatisfaccion(materia[1], cant_materias_solicitadas, sum(prioridades))
            
            # Verificar si hay suficientes cupos para la materia
            if materia[1] <= 0:
                continue
            
            # Actualizar la tabla de programación dinámica
            dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + insatisfaccion)
            
            # Actualizar los cupos disponibles para la materia
            materias[j - 1] = (materia[0], materia[1] - 1)
    
    # Reconstruir la asignación de materias
    asignacion = []
    i, j = num_estudiantes, num_materias
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j - 1] + calcular_insatisfaccion(materias[j - 1][0], estudiantes[i - 1][1][0], sum([p[1] for p in estudiantes[i - 1][1][1]])):
            asignacion.append((estudiantes[i - 1][0], materias[j - 1][0]))
            i -= 1
            j -= 1
        else:
            i -= 1
    
    # Devolver la asignación y la insatisfacción general
    asignacion.reverse()
    insatisfaccion_general = dp[num_estudiantes][num_materias] / num_estudiantes
    return asignacion, insatisfaccion_general


# Ejemplo de datos
estudiantes = [(1000, (2, [(100, 3), (101, 2)])), (1001, (3, [(102, 5), (100, 1), (101, 2)])), (1002, (2, [(100, 3), (102, 2)])), (1003, (1, [(102, 2)])), (1004, (2, [(100, 1), (101, 4)]))]
materias = [(100, 1), (101, 3), (102, 2)]

asignacion, insatisfaccion_general = asignar_materias(estudiantes, materias)
print("Asignación de materias:", asignacion)
print("Insatisfacción general:", insatisfaccion_general)



