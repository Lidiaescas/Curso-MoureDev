"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
y muestre por pantalla el grupo que le corresponde."""

nombre = input("Cuál es tu nombre?: ")
sexo = input ("Cuál es tu sexo?: ")

if nombre.upper()<="M" and sexo == "mujer" or nombre.upper() >="N" and sexo == "hombre":
    print("Grupo A")

else:
    print("Grupo B")

#a < b < c < ... < z < A < B < C < ... < Z

