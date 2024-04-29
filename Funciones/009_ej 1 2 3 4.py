#1Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def my_function():
    print("Hola amiga!")

my_function()


"""2Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo 
¡hola <nombre>!."""

def my_name(name): 
    print("Hola " + name + "!")
    

my_name("LIDIA")


#3Escribir una función que reciba un número entero positivo y devuelva su factorial.
#No está hecho con funciones, pero vale

import math
print(math.factorial (9))




"""4Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe 
recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""

def value(number, IVA = 0.21):

    aplicacion_IVA = IVA * number
    suma = aplicacion_IVA + number
    return(suma)

suma = value(800)
print(suma)

#Otra forma de hacerlo
print(value(800, 0.30))
