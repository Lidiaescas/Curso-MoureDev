#Listas (NO ES LO MISMO UNA LISTA QUE UN ARREGLO (array))

my_list = list() #si le pongo list no va a ser un tuple
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 32, 32, 30, 26, 31]
print(my_list)
print(len(my_list)) #El lenght(longitud) de my list es 7. Es una forma de agrupar datos.

my_other_list = [35, 1.77, "Brais", "Moure"] #No tiene por qué ser sólo un tipo de caracter
print(type(my_other_list)) #El type nos dice que tenemos una lista

#La diferencia entre tuple (35, 24, 62) y list [35, 24, 62] es que la ultima puedo modificarla, la otra no
#Podemos acceder a los elementos por separado. Las listas tienen operaciones propias. El array es + inamobible

#Si quiero acceder a mi edad en 'my_other_list':
print(my_other_list[0]) #Pongo 0 para que me diga el primer elemento de mi lista: 35 (EDAD)
print(my_other_list[-1]) #Me da el ultimo elemento (MOURE)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Brais")) #Cuenta cuántos Brais hay almacenados en mi lista (no en mi variable)

print(my_list.count(32)) #Cuenta cuántos 32 hay almacenados en mi lista

fea = "calcamonia"
print(fea.count("c")) #Cuenta cuántas c hay en la palabra de mi variable

my_other_list = [35, 1.77, "Brais", "Moure"] 
age, height, name, surname = my_other_list
print(age)

#si quito un elemento, al tener my_other_list 4 elementos y quedar 3
#el print da error

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

#concatenar dos listas: 
print(my_list + my_other_list) #Con - da error

#Para que pase a ser una lista hay dos modos: my_list = list("Hola") o my_list = ["Hola"]

my_other_list.append("Mouredev") #Función append: se añade un nuevo objeto a la lista
print(my_other_list)

my_other_list.insert(1, "Azul") #Funcion insert: se añade un nuevo objeto a la lista en la posición indicada (1)
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(32) #función remove: Eliimna directamente lo que le pongas (32), y el primero que encuentra
print(my_list)

my_list.pop() #Función pop: Elimina el último elemento de la lista
print(my_list)

print(my_list.pop(2)) #Si le pongo el 2 eliminará el elemento de la posición 2
print(my_list)

#si quiero almacenar el objeto que he eliminado con el pop:
my_pop_element = my_list.pop(2)
print(my_pop_element)

del my_list[0] #Funcion del: sirve para cargarse el elemento directamente. Lo elimina por indice (en este caso el 0)
print(my_list)

my_new_list = my_list.copy() #Función copy: para hacer una copia del valor de la variable


my_list.clear() #Funcion clear: se borra todo lo de dentro de la lista
print(my_list)
print(my_new_list) #Se borrará my_list, pero no la copia adquirida de my_list

my_new_list.reverse() #Función reverse: le da la vuelta a todo
print(my_new_list)

my_new_list.sort() #Función sort: ordena, en este caso de menor a mayor
print(my_new_list)

#Cómo hacer sublistas:
print(my_new_list[1:2]) #Con esta 'funcion' obtengo el rango de numeros entre posiciones 1 y 2


my_other_list[1] = "Rojo"
print(my_other_list) #El color anteriormente era azul, ahora lo he cambiado a rojo















