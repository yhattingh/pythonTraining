# A lambda function is a small anonymous function
# A lambda function can take any number of args, but can only have one expression
# syntax
# lambda arguments: expression
# the expression is executed and the result is returned
# for example, add 10 to arg a, and return the result
x = lambda a : a + 10
print(x(5))

y = lambda a,b: a*b
print(y(5,2))

z = lambda a,b,c,: a + b + c
print(z(5,6,1))

# the power of lambda is better shown when we use them as an anonymous function inside another function
def my_func(n):
    return lambda a : a * n

mydoubler = my_func(2)
mytripler = my_func(3)

print(mydoubler(11))
print(mytripler(11))