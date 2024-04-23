### Funciones ###

#Funciones normales

def my_function (): #función def: Como definir una función
    print("Esto es una funcion")


my_function()


#Funciones para pasar datos

def sum_two_values(first_number, second_number):
    print(first_number + second_number)


sum_two_values(5, 7)
#Si ponemos valores que se puedan concatenar la operación se hará sin problema



#La función al igual que puede recibir parametros los puede retornar
def sum_two_values_with_return(first_number, second_number):
    return(first_number + second_number)

my_result = sum_two_values_with_return(10, 5)

