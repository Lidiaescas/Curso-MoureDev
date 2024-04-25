### Modules ###
#Sirven para no replicar código una y otra vez
#Función import: para acceder a otros ficheros
#Creamos un fichero llamado module.
#Entramos dentro de module (Module.)
#importar unicamente una de las funciones que tiene definida el fichero


import my_module

my_module.sum_value(5, 3, 1)
my_module.print_value("Hola Python")

from my_module import sum_value, print_value

sum_value(5, 6, 1)
print_value("Hola python")

#Funciona porque importamos una operacion concreta de ese modulo
#Tenemos módulos creados por python

import math

print(math.pi) #numero pi
print(math.pow(2, 8)) #nº elevado

from math import pi
print(pi)

#Si quiero nombrar de alguna forma a pi (que no haria falta xk está detro del modulo de math, lo llamo ej:pi_value)
from math import pi as pi_value
print(pi_value)