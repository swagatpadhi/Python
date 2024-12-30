s = {3, 66, 321, 80}
s.add(50)
s.add(100)
print(s)
print(len(s))
s.remove(66)
print(s)
s.clear()
print(s)

s1 = {1, 33, 67, 8}
s2 = {1, 100}
print(s1.intersection(s2))
print(s1.union(s2))