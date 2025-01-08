# LIST METHODS

numbers = [1, 2, 3, 4, 5]

# append method to add value to the end of list
numbers.append(6)
print(numbers)          # we'll get updated list [1, 2, 3, 4, 5, 6]

# insert method to add value to the list
numbers.insert(0, -1)
print(numbers)           # we'll get updated list [-1, 1, 2, 3, 4, 5, 6]

# to remove item
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)           # we'll get updated list [1, 2, 4, 5]

# to if 1 is in our list
numbers = [1, 2, 3, 4, 5]
print(1 in numbers)       # this boolean expression will return a boolean value True
# to if 1 is in our list
print(10 in numbers)       # this boolean expression will return a boolean value False

# how many items we get in list?
print(len(numbers))      # 5

