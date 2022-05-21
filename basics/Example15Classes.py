# Create a class named person and us the __init__ () function to assign values for name and age
# Object methods
# Objects can also contain methods
# Methods in objects are functions that belong to the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Diana", 22)
p1.myFunc()

# the self parameter is a reference to the current instance of the class and is used to access
# variables that belong to the classExample14Classes.py





