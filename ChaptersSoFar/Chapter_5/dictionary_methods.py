marks = {
    34: "Kevin",
    "Swagat": 100,
    "Ramesh": 50,
    "Andrew": 53
}

# store = marks.items()
# print(store)

# print(marks.keys())
# print(marks.values())
marks.update({"Swagat": 98, "Arora":100})
print(marks)

print(marks.get("Swagat"))
print(marks.get("shivam")) #this will print None
print(marks["Swagat"])
print(marks["Shivam"]) #this will give us error