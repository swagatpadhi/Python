# name = "Swagat loves pizza and rasgulla donuts"

# print("rasgulla" in name)
#demonstration of in keyword

word1 = "Make a lot of money"
word2 = "buy now"
word3 = "subscribe this"
word4 = "click this"
word4 = "\"click this\""

comment = input("Enter comment: ")
if((word1 in comment) or (word2 in comment) or (word3 in comment) or (word4 in comment)):
    print("Spam Comment")

else:
    print("Genuine Comment")