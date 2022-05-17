print(10 > 9)
print(10 == 9)
print(10 < 0)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Bool tests for a string or int
# If the string is empty or int is 0, then it returns false
# Using variables with bool
x = "hello"
y = 15
a = ""
b = 0

print(bool(x))
print(bool(y))
print(bool(a))
print(bool(b))

print(bool(["apple","cherry","banana"]))
print(bool([]))

print(bool("Hello"))
print(bool(15))# bool evaluate if it is a string or int
print(bool()) # only empty strings are false
print(bool("")) # only empty strings are false
print(bool(0)) # only 0 is false

# You can also create functions that return a bool value
def myFunction1():
    return False
print(myFunction1())

def myFunction2():
    return True
print(myFunction2())

# execute code based on the boolean answer of a function
# Print yes if the function returns true and otherwise print no
if myFunction1():
    print("YES")
else:
    print("NO!!")

if not myFunction2():
    print("NO! - Func2")
else:
    print("YES - Func2")

#isinstance() function for example can be used to determine if an object is of a certain data
x = 200
#should return false because x is an int
print(isinstance(x,str))
#should return true because x is an int
print(isinstance(x,int))



