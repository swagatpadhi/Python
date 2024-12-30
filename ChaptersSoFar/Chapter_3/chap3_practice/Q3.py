#double-space detection as well as removal problem.
str = "Swagat's a  good gu  y."
print(str.find("  "))
print("After removind double spaces...")
print(str.replace("  ", " "))