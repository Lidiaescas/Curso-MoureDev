"""Escribe un programa que pida al usuario dos números y muestre por pantalla el resultado de su división. 
Además, si el divisor es cero el programa debe mostrar un error"""

numero1 = int(input("Inserta un número: "))
numero2 = int(input("Inserta otro número: "))


if numero2 == 0:
    print("Error")

else:
    print(numero1/numero2)

