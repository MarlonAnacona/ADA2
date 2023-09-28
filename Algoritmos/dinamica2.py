def minimize_student_discontent(k, r, M, E):
    # Inicializa la matriz de memoización con valores infinitos.
    memo = [[float('inf')] * (k + 1) for _ in range(r + 1)]
    
    # Inicializa la insatisfacción general.
    total_discontent = 0.0

    # Inicializa la asignación de materias para cada estudiante.
    assignments = [[] for _ in range(r)]

    # Función recursiva para calcular la insatisfacción mínima.
    def dp(student, assigned):
        # Si ya se han asignado todas las materias a todos los estudiantes, retorna 0.
        if student == r:
            return 0.0

        # Si ya calculamos este estado, simplemente retorna el valor almacenado.
        if memo[student][assigned] != float('inf'):
            return memo[student][assigned]

        # Itera sobre las asignaciones posibles para este estudiante.
        for i in range(len(E[student][1]) + 1):
            # Intenta asignar las primeras i materias.
            new_assign = assignments[student] + [j[0] for j in E[student][1][:i]]

            # Calcula la insatisfacción local para esta asignación.
            dissatisfaction = 0.0
            for subject in M:
                assigned_count = new_assign.count(subject)
                requested_count = E[student][0]
                priority = 0 if subject not in [j[0] for j in E[student][1]] else E[student][1][[j[0] for j in E[student][1]].index(subject)][1]

                dissatisfaction += (1 - assigned_count / requested_count) * (priority / (3 * requested_count - 1))

            # Llama recursivamente a dp para el siguiente estudiante.
            new_discontent = dp(student + 1, assigned + i)

            # Actualiza la insatisfacción mínima si es menor que la actual.
            if dissatisfaction + new_discontent < memo[student][assigned]:
                memo[student][assigned] = dissatisfaction + new_discontent
                assignments[student] = new_assign

        return memo[student][assigned]

    # Llama a dp para el primer estudiante (0) y ninguna asignación (0).
    total_discontent = dp(0, 0)

    # Retorna la insatisfacción general y las asignaciones de materias.
    return total_discontent, assignments

# Ejemplo de uso
k = 3
r = 5
M = {100: 1, 101: 3, 102: 2}
E = {0: (2, [(100, 3), (101, 2)]), 1: (3, [(102, 5), (100, 1), (101, 2)]), 2: (2, [(100, 3), (102, 2)]), 
     3: (1, [(102, 2)]), 4: (2, [(100, 1), (101, 4)])}

insatisfaction, assignments = minimize_student_discontent(k, r, M, E)
print("Insatisfacción General:", insatisfaction)
print("Asignación de Materias:")
for i, assignment in enumerate(assignments):
    print(f"Estudiante {i}: {assignment}")




