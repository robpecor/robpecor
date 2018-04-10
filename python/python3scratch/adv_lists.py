l = [1, 2, 3]

l.append(4)

print(l)

# Append an item to the list.  Can only add 1 item at a time
l.append(2)

# Count occurrences of an item in a list
print(l.count(2))
# 2 - There are two '2's in the list.

# Extend - Used to add one or more items.  Probably use this instead of append.
l.extend([5, 6, 7])
print(l)
# [1, 2, 3, 4, 2, 5, 6, 7]

x = [1, 2]
x.extend([3])
print(x)
# [1, 2, 3]

# Index - Shows the index of the first item selected
print(l.index(2))
# 1 - Note, only shows 1st occurrence of the index for 2.  Not 1, 4 in this case.

# Insert - Place an item at an index l.index(<index>, <item>)
l.insert(0, 'inserted')
print(l)
# ['inserted', 1, 2, 3, 4, 2, 5, 6, 7]

# Pop - last item by default, or use index
# Default, last
print(l.pop(), l)
# 7 ##(7 is popped Number), resultant list is ['inserted', 1, 2, 3, 4, 2, 5, 6]

# By Index
print(l.pop(0), l)
# Show popped value at index 0 - inserted, resulted list is [1, 2, 3, 4, 2, 5, 6]

# Remove value - Only the first instance
l.remove(2)
print(l)
# [1, 3, 4, 2, 5, 6]

# Reverse the list
l.reverse()
print(l)
# [6, 5, 2, 4, 3, 1]

# Sort the list - Only if all values are of same type
l.extend([100, 0, 7])
print(l)
# [6, 5, 2, 4, 3, 1, 100, 0, 7]
l.sort()
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 100]

alph = ['a', 'z', 'e', 'm', 'b', 'y']
alph.sort()
print(alph)
# ['a', 'b', 'e', 'm', 'y', 'z']

