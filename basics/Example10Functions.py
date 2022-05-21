# A function (methods in Java) is a block of code which only runs when it is called
# You can pass data knows as parameters into a function
# A function can also return a result
# In Python a function is defined by using the def keyword
def my_function():
    print("Hello from a function")
# To call a function, use the function name followed by parenthesis
my_function()

# Information can be passed into functions as arguments
# Arguments are specified after the function name, inside the parenthesis.

def my_function1(fname):
    print(fname + " Reference")
#call function
my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

# You can add as many arg as you like - Just separate them with a comma
def myfunction2(fname,lname):
    print("A function with 2 arguments")
    print(fname + " " + lname)
myfunction2("Emil", "Andrews")


def my_function3(lname):
    print(lname)

my_function3("Smith")
my_function3("Doe")
my_function3("White")

#if you do not know how many arguments will be passed in your function
#add a * before the params in the function def
def my_functionkids(*kids):
    print("The youngest child is " + kids[1])
my_functionkids("Emil","Tobi","Linus")

# you can also send arguments with the key = value syntax
# this way the order of the args does not matter
def my_functionkidsOrderDoesntmatter(child3, child2, child1):
    print("The youngest kid is " + child3)
my_functionkidsOrderDoesntmatter(child1 = "Emil", child2 = "Tobi", child3 = "Linus")

# **kwags (arbitary key words)
# If you do not know how many keyword arguments that will be passed
# into your function add two asterix before the parameter name in the function definition
# This way the argument will receive a dictionary of arguments and can access the arg accordingly

def my_functionKwags(**kid):
    print("His last name is " + kid["lname"])
my_functionKwags(fname = "Tobias", lname = "Reed", age = "ten")

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



