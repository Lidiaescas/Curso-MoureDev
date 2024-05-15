
"""Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según 
   o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
 las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama."""

def es_anagrama(first_word, second_word):
    if first_word.lower() == second_word.lower(): 
        return False
    return sorted(first_word.lower()) == sorted(second_word.lower()) 

print(es_anagrama("Amor", "Roma"))

"""Pongo lower para que le pase lo que le pase me lo convierta siempre a minusculas. Y este if va 
1º xk esto si que no quiero tomarlo como un anagrama. Si es la misma palabra me pondrá false
Funcion sorted: hace como una lista, y ordena las letras de esa palabra. Lo que estamos haciendo 
aquí es pasar las palabras a minuscula y luego reordenarlas. """