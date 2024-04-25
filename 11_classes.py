# Classes #

#Cómo definir una clase:
#Los nombres de las clases se escriben en camel case (MyPerson)
class MyEmtyPerson:
    pass

print(MyEmtyPerson)
print(MyEmtyPerson())

#Constructor de clase (siempre necesario el self):
class Person:
    def __init__(self, name, surname):
        self.name = name #Self tiene una propiedad name igualada a name
        self.surname = surname

my_person = Person("Brais", "Moure")
print(f"{my_person.name} {my_person.surname}")


class Person:
    def __init__(self, name, surname, alias = "sin alias"): #name solo podria cambiarlo aquí
        self.full_name = f"{name} {surname} ({alias})" #Propiedad publica
        self.__name = name #Propiedad privada: las dos barras sirven para no poder cambiar el nombre
#Para poder modificar la p.privada tendriamos que hacer un set para poder acceder a la variable 

    def get_name (self):
        return self.__name #


    def walk(self):
        print(f" {self.full_name} Está caminando")

my_person = Person("Brais", "Moure")
print(my_person.full_name)

my_person.walk()


my_other_person = Person("Brais", "Moure", "Mouredev")
print(my_other_person.full_name)
print(my_person.get_name()) #
my_other_person.walk()
my_other_person.full_name = "Hector de Leon (El loco de los perros)"
print(my_other_person.full_name)

