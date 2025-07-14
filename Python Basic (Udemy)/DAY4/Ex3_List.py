import random

name_str = input("Give me everybody's names, separated by a space. : ")
# split will split the string in a list with " ".
names = name_str.split(" ")
print(names)

nameSize = len(names)

randomNumber = random.randint(0 , nameSize-1)

print(names[randomNumber] + " is going to buy the meal today!")

# using choice function

PayName = random.choice(names)
print(PayName + " is going to buy the meal today!")


#Nested List
List1 = ["Gajendra" , "Gangwar" , "is"]
List2 = ["an" , "Gentle" , "Man"]

WholeList = [List1 + List2]

print("List1 => " , List1)
print("List2 => " , List2)
print("WholeList => " ,  WholeList)