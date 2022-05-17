#This is a single line comment
"""
This is a comment
written in more than one line
"""
#Variables do not need to be declared with any particular type and can even change type after they have been set
x = 5 # x is of type int
x = "Sally" # x is now a string
y = "hello world"

print(x)
print(y)

# If you want to specify the data type of a variable, it can be done with casting
x = str(3) # x will be '3'
y = int(4) # y will be 3
z = float(3) # z will be 3.0
print(type(x))
print(type(y))
print(type(z))

# string variables (vars) can be declared by using either a single or double quote
# variables are also case-sensitive
x ="Sally-x"
X = 'Sally-X'
print(x)
print(X)
print("hi " + X + " " + "and" + " " + x + " the value of y is " + str(y))

#inputs
my_user_input = input("your user input goes here:  ")
print("The user input was" + my_user_input)

# strings in python are arrays of bytes representing the unicode characters
# char example == there are no chars
