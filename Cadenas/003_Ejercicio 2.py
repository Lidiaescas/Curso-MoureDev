"""Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por 
pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con 
todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera."""

nombre = input("Inserte nombre aquí: ")
apellidos = input("Insertar apellido: ")

#Dos formas diferentes de hacer el ejercicio:
#Forma de pecu
print(nombre.lower() + apellidos.lower())
print(nombre.upper() + apellidos.upper())
print(nombre.capitalize() + apellidos.capitalize())

#Mi forma:
minuscula = nombre.lower() + " " + apellidos.lower()
print(minuscula)


mayuscula = nombre.upper() + " " + apellidos.upper()
print(mayuscula)


primeramayuscula = nombre.capitalize() + " " + apellidos.capitalize()
print(primeramayuscula)

