#
#   Kayla Saniei
#
#   starsMenu.py
#
#   Menu-driven interface program that allows the user to
#       1. Draw a line of stars
#       2. Draw a square filled with stars
#       3. Quit
#
#   Input: User's choice
#          Length line/square
#
#   Processing 1. Display menu
#              2. Prompt user for choice
#              3. Drive menu options
#                  Case 1 - Line
#                       Prompt user for length of the line (>O)
#                       Display line filled with stars:
#                           One star at a time
#                  Case 2 - Square
#                       Prompt user for length of the square (>O)
#                       Display square filled with stars:
#                           One line at a time
#                               One star at a time
#                  Case 3 - Quit
#
#   Output: Based on the user's choice, line/square filled with stars
#
def main():
    # Intro
    print("\nLines & Squares App ...")

    # Initalize Quit constant
    QUIT = 3

    # Menu

    # Initalize control variable
    choice = 0

    while choice != QUIT:
        # Display menu & prompt user for choice
        print("\nChoose one of the following options")
        print("\t1. Draw a line of stars.")
        print("\t2. Draw a sqaure filled with stars.")
        print("\t3. Quit.")
        choice = int(input("Option: "))

        # Drive menu options
        if choice == 1: # Line
            print("\nLine ...")
            print()

            # Prompt user for length of the line (>O)
            length = int(input("Enter length of line (<O): "))

            # Validate
            while length <= 0:
                print("Error ... Invalid length. Try again.")

                # Prompt user for length of the line (>O)
                length = int(input("Enter length of line (<O): "))
                
            # Display line filled with stars
            print()
            for star in range(length):
                print("*", end = " ")
            print()
        elif choice == 2: # Square
            print("\nSquare ...")
            print()

            # Prompt user for length of the square (>O)
            length = int(input("Enter length of square (<O): "))

            # Validate
            while length <= 0:
                print("Error ... Invalid length. Try again.")

                # Prompt user for length of the square (>O)
                length = int(input("Enter length of square (<O): "))

            # Display square filled with stars
            print()
            for line in range(length):
                for star in range (length):
                    print("*", end = " ")
                print()
        elif choice == QUIT: # Quit
            print("\nGood Bye ...")
            print()
        else: # Invalid choice
            print("Error ... Invalid option. Try again.")
