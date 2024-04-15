#Operadores aritméticos

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2) #Me da el resto de la división, que es 0 porque 2*5=10
print(10 // 3) #La división me da decimal, y la llamada floor division (//) Me da el numero entero aproximado
print(2 ** 3) #Calcular un exponente 2^3

print("Hola"+"Python") #con menos, o por, o cualquier otro, daría error
print("Hola"+ str(5)) #Para que me deje sumar texto con el 5, tengo que transformar el 5 en texto (F. str)
#Es lo mismo poner srt(5) que "5"

print("Hola"* 5) #Multiplico los holas
print("Hola"* (2 ** 5))

my_number_float = 2.5 * 2
print("hola" * int(my_number_float)) #Me convierte el número decimal (5.0) a entero (función int)
#Pero si la operación diera un número decimal como tal, seguiría dando error. (float - decimal)


#Operadores comparativos
print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4) 
print(3 == 4) #igual
print(3 != 4) #distinto 
print(3 > 4 == 2)


print("aaaa" > "abaa") #Ordenación alfabética por ASCII¿? (a no es mayor que b)
print(len("aaaa") > len("aaaabaa")) #Función len: para calcular la longitus de una cadena de texo, va a contar caracteres.
print("Hola" < "Python")
print("Hola" >= "Zola") #Aquí lo que comprueba es una ordenación alfabética (Z despues que H) (False)
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python") 


#Operadores Lógicos (lógica booliana)
print(3 < 4 and "Hola" > "Python") #True y False = False / False y True = False 
print(3 > 4 or "Hola" > "Python") #False o False = False 
print(3 < 4 and "Hola" < "Python") #True y True = True
print(3 < 4 or "Hola" > "Python") #False o True = True 
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
#Si quiero que una operación se haga antes que otra, igual que en mates, le coloco un paréntesis.

print(not(3 > 4 )) #Un no falso es verdadero, por lo tanto es TRUE