### Diccionarios ### 

#Formas de definir un diccionario:
my_dict= dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

#Formas de trabajar con un diccionario:
#Como nosotros definimos una clave(nombre), y le asocio un valor:(Brais)
my_other_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad":35, 1:"Python"}
#Añado un ID, 1. El valor tambien puede ser un numero, no es fuertemente tipado

my_dict = {
    "Nombre": "Brais", 
    "Apellido": "Moure", 
    "Edad":35, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
    }
print (my_other_dict)
print(my_dict)

print(len(my_other_dict)) #tenemos 4 claves
print(len(my_dict)) #tenemos 5 datos asociados a un valor

print(my_dict["Nombre"]) #Me aparecerá el nombre:Brais. Así puedo acceder al elemento

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"]) #Renombramos el valor 'nombre'

print(my_dict[1])

my_dict["Calle"] = "Calle Mouredev"
print(my_dict) 
#Forma de agregar un nuevo campo al dic

del my_dict["Calle"] #Forma de eliminar un solo elemento en nuestro dic
print(my_dict)

print("Moure" in my_dict) #Comprobar si Moure está en my_dic :False. porque de esta forma estamos buscando por clave y no por valor
print("Apellido" in my_dict)
#Si pusieramos 'Nombre',  apellido, si que saria true


print(my_dict.items()) #Función items: un listado con cada uno de los items
print(my_dict.keys()) #Función keys(claves): listado de las keys: nombre, apellido... 
print(my_dict.values()) #Función values: lista de todos los valores de las claves
print(my_dict.fromkeys())