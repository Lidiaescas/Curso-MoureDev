### Tuples ###

#dos formas de definir una tupla
my_tuple = tuple()
my_other_tuple = (35, 60, 30)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0]) #Me da el elemento 0 de la lista -> 35
print(my_tuple[-1])


print(my_tuple.count("Brais")) #Cuenta cuantos 'brais' hay
print(my_tuple.index("Moure")) #unción index: nos dice la posicion del objeto (en este caso 3)
print(my_tuple.index("Brais")) 

#my_tuple[1] = 1.80
print(my_tuple) #Las tuplas no pueden cambiarse, son inmutables

print(my_tuple + my_other_tuple) #Sumo las tuplas

#Taambién puedo hacer esto:
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) #Coge los objetos entre posicion 3 y 6 


#Transformo la tupla en lista, la modifico, y la vuelvo a transformar en tupla.
my_tuple = list(my_tuple) #He transformado mi tupla en lista, ahora puedo modificarla
print(type(my_tuple))

my_tuple[4] = "Mouredev" #La posición 4 ha sido modificada
my_tuple.insert(1, "Azul") #Insertar Azul en la posicion 1.
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple[2] #Esto no se puede hacer, las tuplas no se modifican
del my_tuple #Funcion del:borro la variable
print(my_tuple) #Ya no existe


