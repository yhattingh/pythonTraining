# A for loop is exclusively used for iteration over a sequence like a list, tuple or dictionary,
# set or even string (a string is a list of characters)
# with the for loop we can execute a set of statements, once for each item in a list tuple set ect
# works like an iterator method

# will print all items in the list called x which = fruits
fruits = ["apple", "cherry", "banana"]
for x in fruits:
    print(x)


# loop through the letters in the word banana
for x in "Banana":
    print(x)


# the break statement can be used to stop the loop before it is looped through all the items
# will stop at cherry and not continue
fruits = ["apple", "banana", "cherry", "grape"]
for x in fruits:
    if x == "cherry":
        break
    print(x)

# with the continue statement we can stop the current iteration of the loop and continue to the next
# will stop at cherry, not print it and then continue with grape
fruits = ["apple", "banana", "cherry", "grape"]
for x in fruits:
    if x == "cherry":
        continue
    print(x)

# The range function returns a sequence of numbers,
# starting from 0 by default and increments by 1 by default,
# and ends at a specified number

# this will print 0 1 2 3 4 5
for x in range(6):
    print(x)

# it is possible to specify the starting value by adding a parameter
# this will print 2 3 4 5
for x in range(2,6):
    print(x)

# the range function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third param

# this will start at 2, increment with 3 each time e.g. 2 5 8 11 14 17
for x in range(2,20,3):
    print(x)
