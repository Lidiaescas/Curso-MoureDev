
"""Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo."""

def area(poligono, *values):
    

    if poligono == area_triangulo:
        base, altura = values 
        area_triangulo = (base * altura)/2
        print(area_triangulo)
    elif area_cuadrado:
         lado = values
         area_cuadrado = lado * lado
         print(area_cuadrado)
    elif area_rectangulo:
        base, altura = values
        area_rectangulo = base * altura
        print(area_cuadrado)
    else:
        print("No hay polígono")

    area(area_triangulo,)
    area(area_cuadrado)
    area(area_rectangulo)

