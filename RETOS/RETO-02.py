
"""Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo."""

def area(base, altura, lado):
    area_triangulo = (base * altura)/2
    area_cuadrado = (lado * 4)**2
    area_rectangulo = base * altura

    if area_triangulo is True:
        print(area_triangulo)
    elif area_triangulo is True:
        print (area_cuadrado)
    elif area_rectangulo is True:
        print(area_cuadrado)
    else:
        print("FALSE")
