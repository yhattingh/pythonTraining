# operations are used to perform operations on vars and values
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

# comparison operators are used to compare 2 values
# != not equal
# > < >= <= greater than, less than, greater than or equal to and less than or equal to
x = 5
y = 3
print(x == y)  # is x = y?

# identity operators
# used to compare the objects, if they are actually the same object, the same memory allocation
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns true because z is the same object as x

print(x is y)
# returns false, because x is not the same object as y

print(x == y)
# to demonstrate the difference between is and ==
# returns true because the content is actualy the same

myList = ["apple", "cherry", "banana"]
print(myList)
myduplist = ["apple", "cherry", "banana", "apple", "cherry", "banana"]
myintlist = [1, 5, 5, 7, 8]
mydiverselist = [1, 5, 5, 7, 8, "apple", "cherry", "banana", "apple", "cherry", "banana", True, False]
print(myduplist)
print(len(myduplist))
print(myintlist)
print(mydiverselist)
print(type(mydiverselist))
# access a list of items
print(mydiverselist[1])

# The while loop can execute a set of statements as long as the condition is true
# print i as long as i is let than 6
i = 1
while i < 6:
    print(i)
    i += 1  # i = 1 + 1
    # remember to increment i, or else the loop will continue forever
    # the while loop requires relevant variables to be ready
    # this is why we define i and set it to 1

    # With the break statement we can stop the loop even if the while condition is true
    # Exit the loop whe i is 3
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1

    # the continue statement can stop the current iteration, and continue with the next
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)

    # the else statement can be used to run a block of code once when the condition is no longer true
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")

    # A for loop is used for iterationg over a sequence like a list tuple or dictionary or even string
    # with the for loop we can execute a set of statements, once for each item in a list tuple set ect
    fruits = ["apple", "cherry", "banana"]
    for x in fruits:
        print(x)

    # loop through the letters in the word banana
    for x in "Banana":
        print(x)

    # the break statement can be used to stop the loop before it is looped through all the items
    fruits = ["apple", "banana", "cherry", "grape"]
    for x in fruits:

        if x == "cherry":
            break
        print(x)

    # with the continue statement we can stop the current iteration of the loop and continue to the next
    fruits = ["apple", "banana", "cherry", "grape"]
    for x in fruits:

        if x == "cherry":
            continue
        print(x)





