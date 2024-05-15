
"""Escribe un programa que imprima los 50 primeros números de la sucesión
    de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en
 * la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13..."""

#Iterar = recorrer
def fibonacci():

    prev = 0
    current = 1

    for indice in range(0, 50 ):
        print(prev)

        fibo = prev + current
        prev = current
        current = fibo

       
fibonacci()


#Chapucilla

"""def fibonacci():

    prev = 0
    current = 1
    i = 0
    print(prev)
    print(current)

    while i < 48:
        i = i + 1
        next = current + prev
        print(next)
        prev = current
        current = next


        
fibonacci()"""


        

 
 