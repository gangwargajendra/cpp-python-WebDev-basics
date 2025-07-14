# pahle print function execute hoga to Hello print ho jayega
# uske baad input function execute hoga joki console se input lega
# and vahi input is poore function ko replace kar dega and print ho jayega

print("Hello " + input("Enter your name : "))

#using nested function

print("characters in name : " , len(input("Enter your name : ")))

#using variables

name = input("Enter your name : ")
length = len(name)
print("Characters in name : " , length)


#  new exercise for changing the value of two variables

a = input("Enter first value : ")
b = input("Enter second value : ")

c = a
a = b
b = c

print("Value of a : " , a)
print("VAlue of b : " , b)