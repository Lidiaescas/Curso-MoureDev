
"""Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo."""

def area(poligono, *values):

    if poligono == "triangulo":
        base, altura = values 
        area_triangulo = (base * altura)/2
        print(area_triangulo)
    elif poligono == "cuadrado":
        lado = values[0]
        area_cuadrado = lado **2
        print(area_cuadrado)
    elif poligono == "rectangulo":
        base, altura = values
        area_rectangulo = base * altura
        print(area_rectangulo)
    else:
        print("No hay polígono")


area("rectangulo", 5, 7)

