### sets ###

#Como definimos un set:
my_set = set()
my_other_set = {} #Generamos un diccionario, pero tambén es un set

print(type(my_set))
print(type(my_other_set)) #Esto es un diccionario (inicialmente)

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set)) #Ahora vuelve a ser un set

print(len(my_other_set)) #Funcion len: nos dice que hay 3 elementos en la variable

#print(my_other_set[0]) #Forma no valida de acceder al elemento de la posicion 0

#Un set no es una estructura ordenada, cuando añadimos un objeto se añade de forma desordenada:
#En los sets no podemos acceder a los elementos ([x]), es diferente que en las listas.
my_other_set.add ("Mouredev")
print(my_other_set)

#Vuelvo a añadir 'Mouredev'
my_other_set.add("Mouredev")
print(my_other_set)
#Un set no admite repetidos

#Cómo es la sintaxis para comprobar si un elemento existe dentro de un set
#Así, tenemos la posibilidad de realizar búsquedas 
print("Moure" in my_other_set) #TRUE
print("Mouri" in my_other_set) #False

my_other_set.remove("Moure") #Elimino Moure
print(my_other_set)

my_other_set.clear() #Funcion clear: ha borrado todos los elementos del set
print(len(my_other_set)) #Con len veoo cuantos elementos hay en el set, ahora 0

#Funcion update: te une un set con otro
my_set.update(my_other_set)
print(my_set)

del my_other_set
#print(my_other_set) #Va a dar error porque con del el set ya no existe

#Voy a transformar mi set en una lista
my_set = {"Brais", "Moure", 35}
my_list = list (my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kutlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "Cs"})) #Aquí no pasa nada xq no se duplican
#Al ser elementos del set que no teníamos antes si que aparecen
#Hemos hecho un union ({"JavaScript", "Cs"}), sin almacenarlo en ninguna variable

print(my_new_set.difference(my_set)) #Función difference: nos muestra los objetos diferentes de ambos sets

print(my_set.issubset(my_new_set)) #Verifica si el 1er conjunto es subconjunto del 2º conjunto

print(my_other_set.discard("Python")) #Funcion discard: eliminar un elemento del conjunto, si está presente.

""" Resumen: con una tupla, podemos tener un conjunto de objetos que no se modifican
con un set, los objetos no se repetirán, y con una lista si que podremos modificarlas"""

