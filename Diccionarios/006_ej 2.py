
"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo 
guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>."""

nombre = input("Nombre: ")
edad = input("Edad: ")
direccion = input("Dirección: ")
telefono = input("Teléfono: ")
datos = {"Nombre": nombre, "Edad": edad, "Dirección": direccion, "Teléfono": telefono}

print(datos["Nombre"], "tiene", datos["Edad"], "años, vive en", datos["Dirección"], "y su número de teléfono es", datos["Teléfono"])
