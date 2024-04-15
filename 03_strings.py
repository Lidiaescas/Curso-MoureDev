#Strings

my_string = "My String"
my_other_string = "My other string"

print(len(my_string)) #Me indica el nº de dígitos de la variable
print (my_string + " " + my_other_string) #He añadido un espacio

my_new_line_string = "Este es un string\ncon un salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación" 
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado" 
print(my_scape_string)

y_scape_string = "\\tEste es un string \\n escapado" #Si pongo la doble barra la \n y \t no se ejecutan
print(my_scape_string)

#Formateo

name, surname, age = "Lidia", "Espinosa", 26

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname,age)) #Es mejor este, imprime tal cual el objeto
#%d sirve para números. 

print("Mi nombre es" ,name ,surname, "y mi edad es" ,age) #Esto es lo mismo

print(f"Mi nombre es {name} {surname} y mi edad es {age}") #Esta manera es la mejor


#Desempaquetado de caracteres
language = "Python"
z, b, c, d, e, f = language
print(z)
print(b)
print(c)
print(d)
print(e)
print(f)


#División

language_slice = language [1:3] #Ha cogido las letras de la 1 a la 3 sin contar esta
print(language_slice)

language_slice = language [1:] #Coge todas menos la primera letra: ython
print(language_slice)

language_slice = language [-2] #Coge la segunda letra empezando por el final
print(language_slice)

language_slice = language [0:6:2] #coge pto, va de la letra 0 a la 6 contando de 2 en 2
print(language_slice)

#Reverse (dar la vuelta)

reversed_languaje = language [::-1] #Me pone la palabra python al revés (el final empieza por -1)
print(reversed_languaje)


#Funciones
print(language.capitalize()) #al poner el punto nos dice las opeaciones disponibles para cadenas de texto
#La función capitalice te pone la primera letra en mayuscula

print(language.count("t")) #Contar cuantas letras 't' tiene la palabra Python
print(language.isnumeric()) #FALSE
print("1".isnumeric()) #TRUE
print(language.upper().isupper()) 
"""1º convierte la palabra python en mayuscula, despúes la función isupper
me confirma si es cierto que es mayuscula, y efectivamente es TRUE"""
print(language.lower().isupper()) #FALSE
print(language.startswith("Py")) 


