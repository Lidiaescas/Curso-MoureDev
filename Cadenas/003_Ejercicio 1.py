"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""

nombre = input("¿Cuál es tu nombre?: ")
numero = int(input("Inserte un número: "))

print((nombre +"\n") * numero) #Para concatenar un salto de linea (\n) lo tengo que poner entre comillas, es texto