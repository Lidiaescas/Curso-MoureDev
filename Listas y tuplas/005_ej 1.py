"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista y la muestre por pantalla."""

subjets = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print (subjets)

subjets = list("Matemáticas, Física, Química, Historia, Lengua")
print (subjets)


"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje 
Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista."""

subjets = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print("Yo estudio", subjets[0], "\n", "Yo estudio", subjets[1], "\n", "Yo estudio", subjets[2])