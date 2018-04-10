d = {'k1':1, 'k2': 2}

# Create a Dictionary using Comprehension

cd = {k:v**2 for k, v in zip(['a', 'b', 'c', 'd'], range(4))}
print(cd)
# {'a': 0, 'b': 1, 'c': 4, 'd': 9}

# Iteration of existing dictionary
for k in d.items():
    print(k)

# Print out Key and Value, just Keys, just Values
print(d.items(), d.keys(), d.values())
