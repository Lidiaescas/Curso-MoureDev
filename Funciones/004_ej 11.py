
"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada 
palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado 
con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia."""

#diccionario {"clave" : "valor"}
#diccionario {"palabra del texto o la lista" : "cuenta o número de veces"}

def contar(texto):
    diccionario = {"test" : 1}
    lista = texto.split()
    
    for palabra in lista:
        for clave, valor in diccionario.items():
            if palabra == clave: #Si la palabra está en el diccionario
                valor = valor + 1
                diccionario.update({clave: valor})

            else: #Si la palabra no está en el diccionario
                diccionario.update({palabra : 1})
    
texto = input("Qué texto proceso?: ")
contar(texto)




