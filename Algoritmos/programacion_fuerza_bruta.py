import itertools

def gamma(X):
    return 3 * X - 1

def calcular_evaluacion(materias, estudiantes, asignacion):
    evaluacion_total = 0

    for estudiante, materias_solicitadas in enumerate(estudiantes):
        materias_asignadas = asignacion[estudiante]

        maj = len(materias_asignadas)
        msj = len(materias_solicitadas)

        parte_1 = 1 - maj / msj

        parte_2_sumatoria = 0
        for materia_solicitada, prioridad in materias_solicitadas:
            if materia_solicitada not in materias_asignadas:
                parte_2_sumatoria += prioridad

        parte_2 = parte_2_sumatoria / gamma(msj)

        insatisfaccion_estudiante = parte_1 * parte_2

        evaluacion_total += insatisfaccion_estudiante

    return evaluacion_total

def leer_datos_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        # Leer el número de materias.
        k = int(archivo.readline())

        # Leer las materias y sus cupos.
        materias = [archivo.readline().strip().split(',') for _ in range(k)]

        # Leer el número de estudiantes.
        r = int(archivo.readline())

        estudiantes = []
        for _ in range(r):
            linea_estudiante = archivo.readline().strip().split(',')
            ej = linea_estudiante[0]
            sj = int(linea_estudiante[1])
            materias_solicitadas = []
            for _ in range(sj):
                linea_materia = archivo.readline().strip().split(',')
                sjl = linea_materia[0]
                pjl = int(linea_materia[1])
                materias_solicitadas.append((sjl, pjl))
            estudiantes.append([(ej, sj)] + materias_solicitadas[1:])  # Excluye el código del estudiante de las materias solicitadas

    return materias, estudiantes
def asignacion_fuerza_bruta(materias, estudiantes):
    mejor_asignacion = None
    mejor_evaluacion = float('inf')

    for asignacion_posible in itertools.product(*estudiantes):
        cupos = {materia[0]: int(materia[1]) for materia in materias}
        asignacion_valida = True

        for estudiante, materia in enumerate(asignacion_posible):
            materia_codigo = materia[0]
            if materia_codigo in cupos and cupos[materia_codigo] > 0:
                cupos[materia_codigo] -= 1
            else:
                asignacion_valida = False
                break

        if asignacion_valida:
            evaluacion = calcular_evaluacion(materias, estudiantes, asignacion_posible)

            if evaluacion < mejor_evaluacion:
                mejor_asignacion = asignacion_posible
                mejor_evaluacion = evaluacion

    return mejor_asignacion, mejor_evaluacion

def escribir_resultados_en_archivo(nombre_archivo_salida, mejor_asignacion, mejor_evaluacion):
    with open(nombre_archivo_salida, 'w') as archivo:
        archivo.write(f"Costo\n")
        archivo.write(f"{mejor_evaluacion}\n")

        for estudiante, materias_asignadas in enumerate(mejor_asignacion):
            ej, aj = materias_asignadas[0]
            archivo.write(f"{ej},{aj}\n")

            for materia in materias_asignadas[1:]:
                materia_codigo = materia  # Obtiene directamente el código de la materia
                archivo.write(f"{materia_codigo}\n")



# Nombre del archivo de entrada y de salida
nombre_archivo_entrada = "entrada1.txt"
nombre_archivo_salida = "salidas1.txt"

# Leer los datos desde el archivo
materias, estudiantes = leer_datos_desde_archivo(nombre_archivo_entrada)

# Ejecutar el algoritmo de asignación por fuerza bruta
mejor_asignacion, mejor_evaluacion = asignacion_fuerza_bruta(materias, estudiantes)

# Escribir los resultados en el archivo de salida
escribir_resultados_en_archivo(nombre_archivo_salida, mejor_asignacion, mejor_evaluacion)
