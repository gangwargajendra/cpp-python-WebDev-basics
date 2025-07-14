import art
from gameData import data
import random


def getRandomAccount():
    """Get data from random account."""
    return random.choice(data)

def display(playerData, str) :
    """Display the data: name, description and country"""
    print(f"{str}: {playerData['name']}, a {playerData['description']}, from {playerData['country']}.")

def isCorrectGuess(firstPlayer, secondPlayer, choosePlayer) :
    if choosePlayer == "A" and firstPlayer['follower_count'] >= secondPlayer['follower_count']:
        return True
    elif choosePlayer == "B" and firstPlayer['follower_count'] <= secondPlayer['follower_count']:
        return True
    else: 
        return False

def game() :
    no_of_wins = 0
    isContinue = True
    str1 = "Compare A"
    str2 = "Against B"
    firstPlayer = getRandomAccount()
    secondPlayer = getRandomAccount()
    while firstPlayer == secondPlayer :
        secondPlayer = getRandomAccount()

    while isContinue :
        print(art.logo)
        display(firstPlayer , str1)
        print(art.vs)
        display(secondPlayer, str2)
        choosePlayer = input("Who has more follower? Type 'A' or 'B': ")

        if isCorrectGuess(firstPlayer=firstPlayer, secondPlayer=secondPlayer, choosePlayer=choosePlayer) :
            no_of_wins += 1
            print(f"You're right! Current score: {no_of_wins}.")
            if choosePlayer == 'B' :
                firstPlayer = secondPlayer
            secondPlayer = getRandomAccount()
            while firstPlayer == secondPlayer :
                secondPlayer = getRandomAccount()
        else :
            print(f"Sorry, that's wrong. Final score: {no_of_wins}")
            isContinue = False

game()