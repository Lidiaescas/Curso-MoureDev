#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar

numero = int(input("Inserta un número: "))

if numero % 2 == 0: #Un numero dividido entre 2 cuyo resto es 0, es par.
    print("par")

else:
    print("impar")
