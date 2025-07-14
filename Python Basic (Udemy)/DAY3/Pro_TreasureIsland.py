# print("""  """) se multiple line ki string print hoti h

print("Welcome To the Treasure Island. Your mission is to find the Treasure.")

direction = input("You're at a crossroad, where do you wnat to go? Type 'left' or 'right'. ")
direction = direction.lower()   # to make sure that all the charactor is in lower case

if direction == "left" :
    work = input("You've come to a lake. There is an island in th middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    work = work.lower()
    if work == "wait"  :
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which colour door do you choose? ")
        door = door.lower()
        if (door == "yellow") :
            print("You found the treasure! You win!")
        elif (door == "red") :
            print("It's a room full of fire. Game Over.")
        elif (door == "blue") :
            print("You enter a room of beasts. game Over.")
        else :
            print("you chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
        
else :
    print("You fell into a hole. Game over.")