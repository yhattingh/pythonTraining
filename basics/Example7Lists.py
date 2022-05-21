# Lists are used to store multiple items in a single variable
# Lists are created using square brackets []
# Lists are one of the 4 built-in data types in Python to store collections.
# The other 3 types are tuples, sets, dictionaries all with different qualities and usage
# Lists are ordered, and the list order will not change
# Lists are changeable - can change, add remove items from list after it has been created
# Tuples, sets, dictionaries are not changeable
# Lists allow duplicates because it is indexed
# Tuple is a collection which is ordered and unchangeable
# Set is a collection and is unordered
# A dictionary is a collection which is ordered, changeable, but no duplicates allowed

myList = ["apple", "cherry", "banana"]
print(myList)
myduplist = ["apple", "cherry", "banana", "apple", "cherry", "banana"]
myintlist = [1, 5, 5, 7, 8]
mydiverselist = [1, 5, 5, 7, 8, "apple", "cherry", "banana", "apple", "cherry", "banana", True, False]
print(myduplist)
print(len(myduplist))  # get length of list (number of items)
print(myintlist)
print(mydiverselist)
print(type(mydiverselist))  ## will return <class type 'list'>
# access a list item
print(mydiverselist[1])