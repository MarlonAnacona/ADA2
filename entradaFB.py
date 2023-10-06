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
    return cupos, materias, asignacion