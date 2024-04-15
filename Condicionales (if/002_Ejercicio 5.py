"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o 
superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos 
mensuales y muestre por pantalla si el usuario tiene que tributar o no"""

edad = int(input("¿Cuál es tu edad?: "))
ingresos = int(input("¿Cuánto cobras tú weon?: "))

if edad > 16 and ingresos >= 1000:
    print("A tributar feo")

else:
    print("A ser weon")


