### Exception Handling ###
#Manejo de errores:
#Si hay un try siempre habrá un except, el else y el finally son opcionales.

number_one = 5
number_two = 1
number_two = "1"

#Try except

try:
    print(number_one + number_two)
    print("No se ha producido un error")

except:
    print("Se ha producido un error")


#Try except else

try:
    print(number_one + number_two)
    print("No se ha producido un error")

except:
#El except se ejecuta si se produce una excepción
    print("Se ha producido un error")

else:
    print("La ejecución continua correctamente")
#El else se ejecuta si no se produce una excepción



#Try except else finally
#Cuando nuestro programa no falla: #number_two = "1" :
#Se ejecuta el try, el else y el finally 
#Cuando nuestro programa falla: number_two = "1":
#Se ejecuta el finally, este se ejecutará siempre

try:
    print(number_one + number_two)
    print("No se ha producido un error")

except:
    print("Se ha producido un error")

else:
    print("La ejecución continua correctamente")

finally: #Opcional
    print("La ejecución continua")



#Excepciones por tipo (type)

try:
    print(number_one + number_two)
    print("No se ha producido un error")

except TypeError:
    print("Se ha producido un error")

except ValueError:
    print("Se ha producido un error")

#Si queremos controlar qué tipo de error se produce utilizamos TypeError y valueError(Por siacaso ambos)



#Captura de la información de la ecepcion (as)
#Así sabremos cuál es el error

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as exceptionerror: #Forma de controlar que sea lo que sea el error se controle
    print(exceptionerror)