# Python does not have built in support for Array, but Python lists can be used instead
# An array is a special variable which can hold more than one value

#List of items which stores the item in a single variable looks like this:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# If you want to loop through the items to find a specific one
cars = ["Ford", "Volvo", "BMW","VW","Nissan"]
# Get the value of the first array item
x = cars[0]
print(x)

# Modify the value of the first array item
cars[0] = "Toyota"
x = cars[0]
print(x)

x = len(cars)  #the number of items in the list
print(x)

# Other methods we can use

"""
append()
clear()
insert()
sort()
"""
