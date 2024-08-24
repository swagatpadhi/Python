y = (3, 66, "Strings", False, 67.5, 39)

#The following thing is wrong, as Tuples are immutable in Python.
print(y[0])
y[0] = "Hard"
print(y)