#
#   Kayla Saniei
#
#   guessNumber.py
#
#   Generate a random integer (1-100). Prompt the user to guess. Checks and displays if
#   user's guess is too high, too low, or right. 
#
#   Input: One number (1-100) each round
#
#   Processing: 1. Generate a random number (1-100)
#               2. Display round, validate number, and prompt for guess (Repeats for 7 rounds)
#               3. If guess, is wrong check & display if its too high or low and
#                  go to the next round
#               4. If guess is right, congratulate the user
#               5. Prompt user to play again
#
#   Output: Guessing number game where user either wins or doesnt
#

# Import random
import random

def main():

    # Initalize and declare variables
    rounds = 0
    guess = 0
    mysteryNumber = 0
    totalRounds = 7
    firstRange = 1
    lastRange = 100

    tryAgain = "y"
    
    displayTitle()
    
    tryAgain = "y"

    while tryAgain == "y":
        rounds = 1
        mysteryNumber = random.randint(firstRange,lastRange)
        # game rounds
        while rounds <= totalRounds and guess != mysteryNumber:
            print()
            print("Round ", rounds, "of ", totalRounds)
            print("---------------")
            guess = getGuess(firstRange, lastRange)
            guessWin(mysteryNumber, guess)
            rounds += 1   

        # Prompt user to play again
        tryAgain = input("\nWould you like to try again (y/n)? ").lower()
        
#
#   displayTitle()
#
#   Displays the title of the game
#

def displayTitle():
    # Intro
    print("\nGuess the Mystery Number ...")
    print()
#
#   getGuess(first, last)
#
#   Prompt for guess. Validates number is between range (loops until valid).
#   Returns guess
#

def getGuess(first, last):

    guess = int(input("Enter your guess(1-100)"))
    
    # Validate
    if guess < 1 or guess > 100:
        print("Error .. Invalid option. Try again.")
        guess = int(input("Enter your guess(1-100) "))

    return guess

#
#   guessWin(number, guess)
#
#   Compare mystery number to player's guess.
#   If guess is:
#       - higher than mystery number then display too high
#       - lower than mystery number then display too low
#       - correct congratulate the player
#
#   Return true if player guessed correctly, return false otherwise
#

def guessWin(number, guess):
    if guess == number:
        print()
        print("Congratulations ... You guessed the Mystery Number!")
        return True
    elif guess > number:
        print(guess, "is too high")
        return False
    elif guess < number:
        print(guess, "is too low")
        return False
