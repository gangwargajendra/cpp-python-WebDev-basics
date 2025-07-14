import random

rock = """
    ______
___.   ___)
      (____)
      (_____)
      (____) 
---.__(__)
"""

paper = """
    ______
---'   ___)____
         ______)
         _______)
        _______)
---.________)         
"""

scissors = """
    _______
---'   ____)___
        _______)
        ________)
       (____)
---.___(___)  
"""

allItems = [rock , paper , scissors]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

randomNumber = random.randint(0 , 2)
print(f"""you choose => 
{allItems[userChoice]}""")

print(f"""Computer choose =>
{allItems[randomNumber]}""")

if userChoice == randomNumber :
    print("It's a draw.")
elif (userChoice + 1 == randomNumber) or (userChoice == randomNumber + 2) :
    print("You lose.")
else :
    print("You win!")


# second way to write the condition

if userChoice == 0 :
    if randomNumber == 0 :
        print("It's a draw.")
    elif randomNumber == 1 :
        print("you lose.")
    else :
        print("you win!")
elif userChoice == 1 :
    if randomNumber == 0 :
        print("You win!")
    elif randomNumber == 1 :
        print("it's a draw.")
    else :
        print("you lose.")
else :
    if randomNumber == 0 :
        print("You Lose.")
    elif randomNumber == 1 :
        print("You win!")
    else :
        print("It's a draw.")