# operations are used to perform operations on vars (variables) and values
print(10 + 5)
x = 5
y = 3
# Arithmetic operations
# - * /
print(x + y)

# Assingnment operators
# used to assign values to vars
# -= *= /=
# x = 5
# x += 3
x = x + 3
print(x)

# Comparison operators are used to compare 2 values
# != not equal
# > < >= <= greater than, less than, greater than or equal to and less than or equal to
x = 5
y = 3
print(x == y)  # is x = y?

# Logical operators are used to combine conditional statements
print(x > 3 and x < 10)
# returns true because 5 is greater than 3 and 5 is less than 10
# or returns true if one of the statements is true
# not returns the result, returns false if the result is true

# identity operators
# used to compare the objects, if they are actually the same object, the same memory allocation
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns true because z is the same object as x

print(x is y)
# returns false, because x might have the same text/content, but it is not the same object as y

print(x == y)
# to demonstrate the difference between is and ==
# returns true because the text/content is actually the same





