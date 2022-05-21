# Create a class named person and us the __init__ () function to assign values for name and age:
# the __init__() function is called automatically everytime the class is being used to create a new object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Diana", 22)

print(p1.name)
print(p1.age)

# Object methods
# Objects can also contain methods
# Methods in objects are functions that belong to the object

# the self parameter is a reference to the current instance of the class and is used to access
# variables that belong to the class


