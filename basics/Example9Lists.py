# Python does not have built in support for Array, but python lists can be used instead
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

cars = ["Ford", "Volvo", "BMW","VW"]
# Get the value of the first array item
x = cars[0]
print(x)

# Modify the value of the first array item
cars[0] = "Toyota"
x = cars[0]
print(x)

x = len(cars)
print(x)

# Other methods we can use

"""
apped()
clear()
insert()
sort()
"""

#Create a class called MyClass, with a property name of x
class MyClass:
    x = 7

#Create an object named p1, and print the value of x
p1 = MyClass()
print(p1.x)

