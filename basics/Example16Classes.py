# Create a class named person and us the __init__ () function to assign values for fname and age
# Object methods
# Objects can also contain methods
# Methods in objects are functions that belong to the object

# the self parameter is a reference to the current instance of the class and is used to access
# variables that belong to the class

# Self parameter
# does not have to be named self, you can call it whatever you like,
# but it has to be the first parameter of any function in the class
# the very first parameter will always refer to SELF or iow the class
# google a bit >> is it only when we use __init__()

class Person:
    def __init__(mysillyObject, name, age):
        mysillyObject.name = name
        mysillyObject.age = age

    def myFunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("Diana", 22)
p1.myFunc()

# you can modify properties on objects like this
# set the age of p1 to 40
p1.age = 40
print(p1.age)







