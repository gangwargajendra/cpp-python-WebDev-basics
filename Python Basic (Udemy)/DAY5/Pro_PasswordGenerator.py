import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_Letters = int(input("How many letters would you like in your password?\n"))
nr_Symbols = int(input("How many symbols would you like?\n"))
nr_Numbers = int(input("How many numbers would you like?\n"))

# Easy level
Easy_Password = ""

for char in range(1 , nr_Letters+1) :
    randomChar = random.choice(letters)
    Easy_Password += randomChar

for symbol in range(1 , nr_Symbols+1) :
    randomSymbol = random.choice(symbols)
    Easy_Password += randomSymbol

for number in range(1 , nr_Numbers+1) :
    randomNumber = random.choice(numbers)
    Easy_Password += randomNumber

print("Easy passwrod : " + Easy_Password)

# hard Level
HardPassword = []

for char in range(1 , nr_Letters+1) :
    randomChar = random.choice(letters)
    HardPassword.append(randomChar)

for symbol in range(1 , nr_Symbols+1) :
    randomSymbol = random.choice(symbols)
    HardPassword.append(randomSymbol)

for number in range(1 , nr_Numbers+1) :
    randomNumber = random.choice(numbers)
    HardPassword.append(randomNumber)

print(f"Before Suffle Password List : {HardPassword}")
random.shuffle(HardPassword)
print(f"After Suffle Password List : {HardPassword}")

password = ""
# for char in HardPassword:
#     password += char
# or for adding list characters
password = password.join(HardPassword)

print("Hard Password : " + password)