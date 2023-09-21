def leer_archivo_txt(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    # Extrayendo k (número de materias) y r (número de estudiantes)
    k = int(lineas[0])
    r = int(lineas[k + 1])

    # Extrayendo M (conjunto de materias)
    M = {}
    for i in range(1, k + 1):
        codigo_materia, cupo = map(int, lineas[i].strip().split(','))
        M[codigo_materia] = cupo

    # Extrayendo E (conjunto de estudiantes)
    E = {}
    linea_actual = k + 2
    for i in range(r):
        codigo_estudiante, numero_materias = map(int, lineas[linea_actual].strip().split(','))
        materias_prioridad = []
        for j in range(numero_materias):
            materia, prioridad = map(int, lineas[linea_actual + j + 1].strip().split(','))
            materias_prioridad.append((materia, prioridad))
        E[codigo_estudiante] = (numero_materias, materias_prioridad)
        linea_actual += numero_materias + 1

    return k, r, M, E

nombre_archivo = "./Pruebas/e_3_5_5.txt"
k, r, M, E = leer_archivo_txt(nombre_archivo)
print(f"k = {k}")
print(f"r = {r}")
print(f"M = {M}")
print(f"E = {E}")