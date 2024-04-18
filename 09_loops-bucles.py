#Loops/bucles

#While:
#Para parar el bucle: ctrl + c

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition = my_condition + 2 #También puedo ponerlo como my_condition += 2

#Llega un momento en el que el while no se cumple.Para enterarnos ponemos lo siguiente:
#A partir del 8 se detiene el buble

else:
    print("Mi condicion es mayor o igual que 10") #Al while también se le puede meter un else, pero no un elif o un if
#El else es opcional

print("La ejecución no continúa")



while my_condition < 20:
    my_condition = my_condition + 1
    if my_condition == 15:
        print("Mi condicion es 15")
        print("se detinene la ejecucion")
        break #Se para el bucle

    print("Mi condicion es menor que 20")
    print(my_condition)


#FOR
# Recorre un listado de elementos
#Un for se va a repetir tantas veces como elementos tengamos en la lista

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)


my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad":35, 1:"Python"}

for element in my_dict:
    print(element) #Solo imprime las claves y no los valores, cuando metemos un for
    if element == "Edad":
        break
else:
    print("El bucle for ha finalizado")


#Puedo hacer esto para que me imprima los valores:

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad":35, 1:"Python"}

for element in my_dict.values():
   print(element)
   if element == "Edad":
       continue #A pesar de tener un stop en la edad porque el for no se cumple, con el continue seguirá
   #Antes de continuar, va a volver de nuevo al for
else:
   print("El bucle for ha finalizado")