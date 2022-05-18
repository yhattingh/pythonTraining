# The range function returns a sequence of numbers,
# starting from 0 by default and increments by 1 by default,
# and ends at a specified number
for x in range(6):
    print(x)

# it is possible to specify the starting value by adding a param
for x in range(2, 6):
    print(x)

# In Python a function is defined by using the def keyword
def my_function():
    print("Hello from a function")
# To call a function, use the function name followed by parenthesis
my_function()

# Information can be passed into functions as arguments
# Arugments are specified after the function name, inside the parenthesis.  You can add as many arg as you like
# Just separate them with a comma
def my_function1(fname):
    print(fname + " Reference")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

def myfunction2(fname,lname):
    print("A function with 2 arguments")
    print(fname + " " + lname)

def my_function3(lname):
    print(lname)

my_function3("Smith")
my_function3("Doe")
my_function3("White")

# my_function2("Emil")

#if you do not know how many arguments will be passed in your function
#add a * before the params in the function def
def my_functionkids(*kids):
    print("The youngest child is " + kids[0])

my_functionkids("Emil","Tobi","Linus")
# you can also send arguments with the key = value syntax
# this way the order of the args does not matter
def my_functionkidsOrderDoesntmatter(child3, child2, child1):
    print("The youngest child is " + child3)

my_functionkidsOrderDoesntmatter(child1 = "Emil", child2 = "Tobi", child3 = "Linus")

# **kwags
def my_functionKwags(**kid):
    print("His last name is " + kid["lname"])

my_functionKwags(fname = "Tobias", lname = "Reed")

# To let a function return a value, use the return statement
def my_returnFunction(x):
    return 5 * x
print(my_returnFunction(4))
print(my_returnFunction(2))

# you can send any data types of arguments to a function (string, number, dictionary)
# and it will be treated as the same data type inside the function
# for example if you send a list as an argument, it will be a list when it reaches the function
fruits = ["apple", "banana", "cherry", "grape"]
def my_functionList(food):
    for x in food:
        print(x)
my_functionList(fruits)

# Default parameter value
# the following example shows how to use the default value
# if we call the function without an argument, it used the default value
def my_functionDefault(country = "South Africa"):
    print("I am from " + country)

my_functionDefault("India")
my_functionDefault()
my_functionDefault("Brazil")



