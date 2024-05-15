"""Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100."""

def numero_primo():

    for indice in range(1, 101):
        i = 1
        j = 0
        while i <= indice:
            
            if indice %i == 0:
                j = j + 1 #Hemos encontrado un divisor
            
            i = i + 1 #Sumo 1 a la i para ir recorriendo el bucle while

        if j == 2: #Mi número es primo
            print(indice) #Entonces lo enseño


numero_primo()    


#Otra forma de hacerlo:

def is_primo():

    for number in range(1, 100):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)

is_primo()