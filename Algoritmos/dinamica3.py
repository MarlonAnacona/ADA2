def calculate_insatisfaction(student_preferences, assignments):
    total_insatisfaction = 0

    for student_id, (requested_count, requested_courses) in student_preferences.items():
        assigned_count = sum(assignments.get(course, 0) for course, _ in requested_courses)
        remaining_courses = requested_count - assigned_count

        if remaining_courses > 0:
            total_priority = sum(priority for _, priority in requested_courses)
            insatisfaction = (1 - assigned_count / requested_count) * (total_priority / (3 * requested_count - 1))
            total_insatisfaction += insatisfaction

    return total_insatisfaction


def rocPD(k, r, M, E):
    # Crear un diccionario para realizar un seguimiento de las asignaciones
    assignments = {}
    
    # Función auxiliar para realizar la búsqueda recursiva
    def search(student_index):
        student_index = 1
        if student_index == r:
            # Se han asignado todas las materias a los estudiantes, calcula la insatisfacción
            return calculate_insatisfaction(E, assignments)
        
        student_id, (requested_count, requested_courses) = E[student_index]
        min_insatisfaction = float('inf')
        
        for course, priority in requested_courses:
            if M[course] > 0:
                # Intenta asignar el curso al estudiante si hay cupos disponibles
                assignments[course] = assignments.get(course, 0) + 1
                M[course] -= 1
                insatisfaction = search(student_index + 1)
                min_insatisfaction = min(min_insatisfaction, insatisfaction)
                # Deshacer la asignación para explorar otras opciones
                assignments[course] -= 1
                M[course] += 1
        
        # Explora la opción de no asignar ninguna materia al estudiante actual
        insatisfaction = search(student_index + 1)
        min_insatisfaction = min(min_insatisfaction, insatisfaction)
        
        return min_insatisfaction
    
    # Llama a la función de búsqueda recursiva para encontrar la asignación que minimiza la insatisfacción
    min_insatisfaction = search(0)
    
    return min_insatisfaction

# Ejemplo de uso:
k = 3  # Cantidad de materias
r = 5  # Cantidad de estudiantes
M = {100: 1, 101: 3, 102: 2}  # Materias y sus cupos disponibles
E = {1000: (2, [(100, 3), (101, 2)]), 1001: (3, [(102, 5), (100, 1), (101, 2)]),
     1002: (2, [(100, 3), (102, 2)]), 1003: (1, [(102, 2)]), 1004: (2, [(100, 1), (101, 4)])}  # Estudiantes y sus preferencias

resultado = rocPD(k, r, M, E)
print("Insatisfacción mínima:", resultado)







