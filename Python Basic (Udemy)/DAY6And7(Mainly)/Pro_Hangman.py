# do it on Reeborg's World Maze and also hurdle 1,2,3,4
import random
import hangmanWords
import hangmanArt 

print(hangmanArt.logo)

chosenWord = random.choice(hangmanWords.word_list)
print(f"choosen word : {chosenWord}")

display = []
for n in range(len(chosenWord)) :
    display.append("_")

print(display)

noOfLives = 7
# while display.count("_") :
while "_" in display :
    guessChar = input("Guess a letter : ").lower()
    print(guessChar)

    if  guessChar in display :
        print(f"you already guessed {guessChar}.")
    elif guessChar not in chosenWord :
        print(f"You guessed {guessChar}, that's not in the word. you lose a life.")
        noOfLives -= 1
        if noOfLives == 0 :
            print(hangmanArt.stages[noOfLives])
            print("You lose!")
            break
    else :
        for n in range(len(chosenWord)) :
            if chosenWord[n] == guessChar :
                display[n] = chosenWord[n]

    print(display)
    print(hangmanArt.stages[noOfLives])

if "_" not in display :
    print(f'congrats, actual word is : {"".join(display)}.')
    print("You win!")