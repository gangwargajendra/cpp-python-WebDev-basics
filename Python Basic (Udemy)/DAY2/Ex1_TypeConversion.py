print("Hello"[0])

print(round(8 / 3 , 3))
print(round(8 / 3))
print(round(8 // 3))

numOfChar = len( input("Enter your name : "))

print("numOfChar has type : " , type(numOfChar))

#it will give error bcz str and int will not concatenate only str and str will concatenate
#print("Your name has " + numOfChar + " characters.")

newNumOfChar = str(numOfChar) #typeConversion from integer to string

print("newNumOfChar has type : " ,  type(newNumOfChar))

print("Your name has " + newNumOfChar + " character.")