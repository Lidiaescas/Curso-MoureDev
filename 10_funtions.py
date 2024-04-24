### Funciones ###

#Funciones normales

def my_function (): #función def: Como definir una función
    print("Esto es una funcion")

#Si yo llamo 3 veces a my_funcion aparecerá 3 veces por pantalla
my_function()
my_function()
my_function()

#Funciones para pasar datos

def sum_two_values(first_number, second_number):
    print(first_number + second_number)


sum_two_values(5, 7)
#Si ponemos valores que se puedan concatenar la operación se hará sin problema



#La función return me da posibilidad de almacenar el resultado de la función en una variable, y podré
#llamarla o no según quiera (mostrarla por pantalla)

def sum_two_values_with_return(first_number, second_number):
    return(first_number + second_number)

my_result = sum_two_values_with_return(10, 5)
print(my_result) 

#Para que quede bonito:
def sum_lilo_with_return(first_number, second_number):
    suma = 1 + 1
    multiplicacion = first_number * second_number
    division = first_number / second_number
    resultado = suma - multiplicacion + division
    return(resultado)

resultado = sum_lilo_with_return(8, 1)
print(resultado)


#Otro ejemplo:

def imprime_nombre (name, surname):
    print(f"{name} {surname}") #con la f el nombre y el apellido se pasan a name y surname

imprime_nombre(surname = "Moure", name = "Brais") #Con el = he reordenado el orden del print.

#Parámetros por defecto:

def imprime_nombre_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
#Si quiero definir un valor por defecto en mi función no pongo el alias abajo y le doy un valor a alias arriba
imprime_nombre_with_default ("Brais", "Moure")

def imprime_textos(*text): #Con este asterisco puedo añadir más parametros
    print(text)

imprime_textos("Hola", "Python", "Mouredev")#Puedo quitarle o ponerle cuantos parámetros quiera


#Operar con el for:
#Parámetros en diferentes lineas. también puedo añadir funciones a los parámetros (upper)
def imprime_textos(*texts):
    for text in texts:
        print(text.upper())

imprime_textos("Hola", "Python", "Mouredev")#Puedo quitarle o ponerle cuantos parámetros quiera
imprime_textos("Hola")