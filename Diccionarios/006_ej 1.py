"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 
'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la 
divisa no está en el diccionario."""

#CHAPUZA PECU

"""diccionario = {"Euro" : "€", 'Dollar':'$', 'Yen':'¥'}

divisa = input("Qué divisa quieres: ")

switch = 0

for clave, valor in diccionario.items():
    if divisa == clave:
        print(valor)
        switch = 1
        break

if switch == 0:
    print("error")"""

#Bien hecho

diccionario = {"Euro": "€", "Dolar": "$", "Yen": "¥"}
divisa = input("¿Qué divisa quieres?: ")


for clave, valor in diccionario.items():
    if divisa == clave:
        print(valor)
        break
else:
    print("error")