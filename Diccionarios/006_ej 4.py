
"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma 
fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes."""

meses = {"Enero": "1", "Febrero": "2", "Marzo": "3", "Abril": "4", "Mayo": "5", "Junio": "6", "Julio": "7", "Agosto": "8", "Septiembre": "9", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"}
pregunta_fecha = input("Inserta fecha: ")
separacion = pregunta_fecha.split("/")

for mes, valor in meses.items():
    if separacion[1] == valor:
        print(separacion[0],"de", mes, "de", separacion[2])
        break

else:
    print("error")
    