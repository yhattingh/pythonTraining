# The while loop can execute a set of statements as long as the condition is true
# print i as long as i is let than 6

i = 1
while i < 6:
   print(i)
   i += 1  # i = i + 1


# remember to increment i, or else the loop will continue forever
# the while loop requires relevant variables to be ready
# this is why we define i and set it to 1

# With the break statement we can stop the loop even if the while condition is true
# Exit the loop when i is 3

i = 1
while i < 6:
   print(i)
   if i == 3:
      break
   i += 1


# the continue statement can stop the current iteration, and continue with the next
# The following will not print 3, but only 12456
# So, while i < 6 then increment i + 1, when you reach 3, skip 3 and continue from 4
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