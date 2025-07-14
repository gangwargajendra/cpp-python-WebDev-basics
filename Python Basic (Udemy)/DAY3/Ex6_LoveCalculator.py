print("Welcome to the Love calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

# Lower function is used to change string in lower case
# count function is used to frequency of a character in string

# we can also concatenate these two string then find

T = name1.lower().count("t") + name2.lower().count("t")
R = name1.lower().count("r") + name2.lower().count("r")
U = name1.lower().count("u") + name2.lower().count("u")
E = name1.lower().count("e") + name2.lower().count("e")
L = name1.lower().count("l") + name2.lower().count("l")
O = name1.lower().count("o") + name2.lower().count("o")
V = name1.lower().count("v") + name2.lower().count("v")
E = name1.lower().count("e") + name2.lower().count("e")

firstDigit = T + R + U + E
secondDigit = L + O + V + E

LovePercentage = firstDigit * 10 + secondDigit; 

if (LovePercentage < 10) or (LovePercentage > 90) :
    print(f"Your score is {LovePercentage}, you go together like coke and mentos.")
elif LovePercentage > 40 and LovePercentage < 50 :
    print(f"Your score is {LovePercentage}, you are alright together.")
else :
    print(f"Your score is {LovePercentage}.")