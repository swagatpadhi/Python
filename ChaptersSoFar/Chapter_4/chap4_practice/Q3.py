y = (3, 66, "Strings", False, 67.5, 39)

print(y[0])
#The following thing is wrong, as Tuples are immutable in Python.
y[0] = "Hard"
print(y)