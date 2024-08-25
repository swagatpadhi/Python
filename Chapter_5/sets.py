s = {1, 34, 3, 6, 7, 3, 3, 3, 3}
 
empty_set = set() #this is an empty set
print(type(empty_set))

print(s)

# Set Elements Must Be Immutable: While sets 
# themselves are mutable, the elements within a
# set must be immutable (e.g., numbers, strings, tuples). This 
# is because sets rely on the hashability 
# of their elements,
# and mutable objects (like lists) cannot
# be hashed and thus cannot be included in a set.