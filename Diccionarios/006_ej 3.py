
"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese 
número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando 
de ello."""

fruteta = input("¿Qué fruta quieres? ")
kilos = int and float(input("¿Cuántos kilos quieres? "))

catalogo = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

for fruta, valor in catalogo.items():
    if fruteta == fruta:
        precio = kilos * valor
        print(precio)
        break
else:
        print("no hay de esa fruteta")





