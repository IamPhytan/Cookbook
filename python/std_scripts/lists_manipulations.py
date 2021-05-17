#
# Print elements of a tuple or a default message
# Used a lot in CodinGame Clash of Code
#

# Tuple of elements
a = tuple(range(5))

# Unpack the elements of a
# >>> print(*a)
# 0 1 2 3 4

# If a is empty, *a = False
# Therefore, unpack the elements inside ["None"], therefore "None"
print(*a or ["None"])


#
# Transpose a list of list
# Used a lot in CodinGame Clash of Code
#

# List of lists
a = [[*range(5)] for _ in range(5)]

# Unpack then zip
# Unpack : Returns every list in a
# >>> print(*a)
# [0, 1, 2, 3, 4] [0, 1, 2, 3, 4] [0, 1, 2, 3, 4] [0, 1, 2, 3, 4] [0, 1, 2, 3, 4]
# Zip : Get an item from each list of a and puts it inside a tuple of elements
# >>> for elem in zip(d.keys(), d.values(), d.items(), d.keys()):
# ...     print(type(elem), elem)
# <class 'tuple'> ('0', 0, ('0', 0), '0')
# <class 'tuple'> ('1', 1, ('1', 1), '1')
# <class 'tuple'> ('2', 4, ('2', 4), '2')
# <class 'tuple'> ('3', 9, ('3', 9), '3')
a_t = list(zip(*a))
print(a_t)


#
# Convert a boolean to another variable
# Used a lot in CodinGame Clash of Code
#

# Boolean
b = True

# Convert
# False : 0, True : 1
res = ("bar", "foo")
print(res[b])
