list = []
inp = int(input("Please enter a number:"))
list.append(inp)
inp = int(input("Please enter a number:"))
list.append(inp)
inp = int(input("Please enter a number:"))
list.append(inp)
inp = int(input("Please enter a number:"))
list.append(inp)

if(list[0] > list[1] and list[0] > list[2] and list[0] > list[3]) :
    print(list[0], "is greatest")
elif(list[1] > list[0] and list[1] > list[2] and list[1] > list[3]) :
    print(list[1], "is greatest")
elif(list[2] > list[0] and list[2] > list[1] and list[2] > list[3]) :
    print(list[2], "is greatest")
else:
    print(list[3], "is greatest")