mark1 = int(input("Enter marks in Python: "))
mark2 = int(input("Enter marks in Maths: "))
mark3 = int(input("Enter marks in Biology: "))

avg = ((mark1 + mark2 + mark3)/3)*100
if(avg >= 0.4 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
    print("Passed Successfully.")
else:
    print("Sorry you've failed.")