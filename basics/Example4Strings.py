# this is like substring in java
# chars 2-4 are inlcuded and 0-1 and 5 onwards are excluded returning ell
b = 'hello,there'
# splitting strings
# the first character has an index of 0
print(b[2:5]) #Java's substrings

# By leaving out the start index, the range will start at the first char
print(b[:7])

# Use negative indexes to start the slice from the end of the string will count from the back
print(b[-5:-2])

# change to case
print(b.upper())
print(b.lower())

# Modifying strings
print(b.replace("h","j"))
print(b.split(","))

# Straight forward concatenation of strings
A = "Hello1"
B = "World1"
C = A + " " + B
print(C)

# concatenate == will return a type error
age = 36
#txt = "My name is Nance" + age
#print(txt)

# formatting strings
# to fix the type error above, use the format method
# The format() method takes the passed args, formats them, and place them in the string
# where the place holders are {}
txt2 = "My name is Nancy, and I am {}"
print(txt2.format(age))

# the format() method takes unlimited number of args, and are placed into the respective place holders
quantity = 3
itme0   = "tomatoes"
price = 45.64
myorder1 = "I want {} {} for {} rands"
# using an index to make sure items are in correct placeholders
myorder2 = "I want to pay {2} rand for {0} pieces of item {1}"
print(myorder1.format(quantity,itme0,price))
print(myorder2.format(quantity,itme0,price))

#escape characters for illegal text
illegalText1 = "We are the so-called \"Vikings\" from the north"
illegalText2 = "We are the so-called \tVikings\" from the north"
illegalText3 = "We are the so-called \nVikings\" from the north"
print(illegalText1)
print(illegalText2)
print(illegalText3)










