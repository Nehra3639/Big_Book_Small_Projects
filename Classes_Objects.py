# A class is an object constructor, or a "Blueprint" for creating objects.
# An object is an instance of a class. A class is a blueprint while instance
# is a copy of class with actual values.
# An object consists of
#    * State:      It is represented by the attributes of an object. it also
#                  reflects the properties of an object.
#    * Behaviour:  It is represented by the methods of an object. it also
#                  reflects the response of an object to other objects.
#    * Identity:   It gives a unique name to an object and enables one
#                  object to interact with other objects.
#
# Let's create any class

# Class for Dog
class Dog:
    pass
# Class Variable
    animal = 'dog'

# The init method or constructor
    def __init__(self, breed, type, color, age):
        self.breed = breed       # Instance Variable
        self.type = type
        self.color = color
        self.age = age


# Objects of Dog class
Rodger = Dog("Pug", "Male", "Brown", "3 years")
Rexy = Dog("Dalmatian", "Bitch", "Black spotted", "2.5 years")
Panther = Dog("Rottweiler", "Male", "Tan_black", "3 years")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Type: ', Rodger.type)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
print('Age: ', Rodger.age)

print('\nRexy details:')
print('Rexy is a', Rexy.animal)
print('Type: ', Rexy.type)
print('Breed: ', Rexy.breed)
print('Color: ', Rexy.color)
print('Age: ', Rexy.age)

print('\nPanther details:')
print('Panther is a', Panther.animal)
print('Type: ', Panther.type)
print('Breed: ', Panther.breed)
print('Color: ', Panther.color)
print('Age: ', Panther.age)
