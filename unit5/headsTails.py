#
#   Kayla Saniei
#
#   headsTails.py
#
#   Implements a coin toss game as many times as indicated by the user
#
#   Input: Heads/Tails user's choice
#
#   Processing: 1. Prompt user for Heads/Tails
#               2. Simulate coin toss
#                   Generate random number (1,2)
#                   -> 1 : Heads
#                   -> 2 : Tails
#                   Display coin toss result
#               3. Display judgement (win/lose)
#
#   Output: Coin toss (Heads/Tails)
#

# Import libraries
import random
import time

def main():
    print("Flipping Coins ...")

    # Initalize control variable
    tryAgain = 'y'

    while tryAgain == 'y':
        # Prompt user for Heads/Tails
        player = getPlayerChoice()

        # Simulate coin toss
        toss = coinToss()

        # Display judgement
        if player == toss:
            print("\nPLayer Wins!!!")
        else:
            print("\nPlayer Loses.")

        # Prompt user whether to try again
        tryAgain = input("\nWould you like to try again (y/n)? ").lower()

#
#   getPlayerChoice()
#
#   Prompt user for Heads (1) or Tails (2), and return choice
#   to the caller
#
#   Return Value: Integer value 1-Heads / 2-Tails
#

def getPlayerChoice():
    choice = 0

    # Prompt user for Heads/Tails
    while choice != 1 and choice != 2:
        # Prompt
        print("\nHeads or Tails?")
        print("\t1. Heads")
        print("\t2. Tails")
        choice = int(input("Choice: "))

        # Validate
        if choice != 1 and choice != 2:
            print("Error ... Invalid choice. Try again")

    return choice

#
#   coinToss()
#
#   Simulate & display the tossing of a coin. Return the
#   result back to the caller
#
#   Return Value: Integer Value 1-Heads / 2-Tails
#

def coinToss():

    # Display heading
    print("\nFlipping the coin ... ", end='')
    time.sleep(3)

    # Generate a random integer value from 1 to 2 (inclusive)
    toss = random.randint(1,2)

    # Display Heads/Tails
    if toss == 1:
        print('Heads')
    else:
        print('Tails')

    return toss

    
