#Variables

my_variable = "My String variable" #nomenclatura camello no correcta, mejor snake case (barrabaja)
print(my_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_int_to_str_variable =  str(my_int_variable)

"""Función str: sirve para transformar lo insertado(el 
parametro), en cadena de texto"""

print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_variable, str(my_int_variable), my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Funciones del sistema
print(len(my_int_to_str_variable)) #Función len (cuenta los caracteres incluidos los espacios, en este caso 5)

#Variables en una sola linea. 
name, surname, alias, age = "Lidia", "Espinosa", "lilo", 26 #hay 3 str y 1 int
print("Me llamo:" ,name, surname, "Mi alias es" ,alias,  " y Mi edad es" ,age)

name = input("Cómo te llamas?: ")
age = input("Cuántos años tienes?: ")
#Primero respondo la primera pregunta, le doy a run y después me saldrá la de la edad para responderla.
#Input es una función que me permite contestar con el valor que se almacenará en mi variable
#Podré asignarle el valor que quiera (ya sea numérico o de texo, es decir, cambiando su tipo)
print(name)
print(age)

#Forzamos el tipo
address: str = "Mi dirección"
address = 65
print(address)
print(type(address))