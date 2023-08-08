#
#   Kayla Saniei
#
#   roulette.py
#
#   Prompts user for a pocket number & determines whether
#   that pocket is green, red, or black
#
#   Input: A number (0-36)
#
#   Processing 1. Prompts user for pocket number
#              2. Checks if number is between 0-36
#              3. If applicable, check which range of numbers that number is in
#              4. If applicable, check if number is even or odd
#              5. Display result
#
#   Output: Corresponding color of what number they chose
#

def main():
    # Intro
    print("Roulette Wheel Colors App")
    print()

    # Declare and initalize variables
    number = 0
    color = "blank"

    # Prompts user for pocket number (0-36) / Input
    number = int(input("Please enter pocket number (0-36): "))

    # Checks if number is in range or not / Validation
    if number >= 0 and number <= 36:
        # Checks which range of numbers the pocket number is in
        if number == 0:
            color = "Green"
        elif number >= 1 and number <= 10:
            # Checks if even or odd
            if number % 2 == 0:
                color = "Black"
            else:
                color = "Red"
        elif number >= 11 and number <= 18:
            # Checks if even or odd
            if number % 2 == 0:
                color = "Red"
            else:
                color = "Black"
        elif number >= 19 and number <= 28:
            # Checks if even or odd
            if number % 2 == 0:
                color = "Black"
            else:
                color = "Red"
        elif number >= 29 and number <= 36:
            # Checks if even or odd
            if number % 2 == 0:
                color = "Red"
            else:
                color = "Black"
        # Displays result / Output
        print("The color of the Wheel Pocket is", color)
    else:
        # number is out of range / Validation / Output
        print("Error. Invalid pocket number. Try again please.")

main()
