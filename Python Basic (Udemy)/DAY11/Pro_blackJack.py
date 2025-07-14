import random
from BlackjackLogo import logo

def randomCardPick() :
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    randomCard = random.choice(cards)
    return randomCard

def returnScore(cards) :
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    if sum(cards) > 21 and 11 in cards :
        cards.remove(11)
        cards.append(1)

    return sum(cards)
    #******OR*******
    # sum = 0
    # for element in cards :
    #     sum += element
    # return sum

def compare(userScore, computerScore) :
    if userScore == computerScore :
        print("It's a draw.")
    elif computerScore == 0 :
        print("Lose, opponent has Blackjack.")
    elif userScore == 0 :
        print("Win with BlackJack..")
    elif userScore > 21 :
        print("You went over. You lose..")
    elif computerScore > 21 :
        print("Opponent went over. You win.")
    elif userScore > computerScore :
        print("You wins.")
    else : 
        print("You lose.")
    

def Blackjack() :
    userCard = []
    computerCard = []
    is_game_over = False

    for i in range(2) :
        userCard.append(randomCardPick())
        computerCard.append(randomCardPick())

    userScore = returnScore(userCard)
    computerScore = returnScore(computerCard)


    # for calculating user cards score
    while not is_game_over  :
        userScore = returnScore(userCard)
        print(f"    Your cards: {userCard}, current score: {userScore}")
        print(f"    Computer's get first card: {computerCard[0]}")
        if userScore == 0 or computerScore == 0 or userScore > 21 :
            is_game_over = True
        else :
            userWnatAddCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if userWnatAddCard == 'y' :
                userCard.append(randomCardPick())
            else :
                is_game_over = True

    # for calculating computer cards score
    while computerScore != 0 and computerScore < 17 :
        computerCard.append(randomCardPick())
        computerScore = returnScore(computerCard)
        
    print(f"    Your final hand: {userCard}, final socre: {userScore}.")
    print(f"    Computer final hand: {computerCard}, final score: {computerScore}.")
    compare(userScore=userScore, computerScore=computerScore)

wantPlay = input("Do you want to play a game of BalckJack? Type 'y' or 'n': ").lower()
if wantPlay == "y"  :
    print(logo)
    Blackjack()
    # can do clear console