import random

RANDON_NUMBER = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "hard" :
    attempt_left = 5
else :
    attempt_left = 10

while attempt_left > 0 :
    print(f"You have {attempt_left} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess: "))
    attempt_left -= 1
    if guess_number > RANDON_NUMBER :
        print("Too hign.\nGuess again.")
    elif guess_number < RANDON_NUMBER :
        print("Too low.\nGuess again.")
    elif guess_number == RANDON_NUMBER :
        print("congratulation, you guess the correct number.")
        break
    if attempt_left == 0 :
        print("You've run out of guesses, you lose.")
