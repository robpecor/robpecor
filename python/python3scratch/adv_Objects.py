# Convert 1024 to binary and hex values.
n = 1024
print('Binary', n, 'is', bin(n), 'Hex is', hex(n))

# Round 5.23222 to two decimal places
r = 5.23222
print(round(r, 2))

# Check if every letter in the string s is lower case
s = 'hello how are you Mary, are you feeling OK?'
print(s.islower())

# How many times does the letter 'w' show up in the string
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

# Find the elements in set1 that are not in set2
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
print(set1.difference(set2))

# Find all elements that are in either set.
print(set1.union(set2))


# Create the dictionary {0:0, 1:1, 2:8, 3:27, 4: 64} using Dictionary Comprehension
# Value = Key ^ 3
d = {x: x**3 for x in range(5)}
print(d)


# Reverse a list
l = [1, 2, 3, 4]
l.reverse()
print(l)

# Sort the list
l = [3, 4, 2, 5, 1]
l.sort()
print(l)