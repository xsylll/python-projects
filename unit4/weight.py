#
#   Kayla Saniei
#
#   weight.py
#
#   Menu-driven interface program that allows the user to
#       1. Display "10 ways to cut 500 calories" guideline
#       2. Generate next semester expected weight table
#       3. Quit
#
#   Input: User's choice
#          Guideline/weight table
#
#   Processing 1. Display menu
#              2. Prompt user for choice
#              3. Drive menu options
#                  Case 1 - Guideline
#                       Display guideline
#                  Case 2 - Weight Table
#                       Prompt user for starting weight (>100)
#                       Display table showing expected weight at end of each month for six months
#                  Case 3 - Quit
#
#   Output: Based on the user's choice, guideline or weight table
#
def main():
    # Intro
    print("\n500 Less a Day Makes the Weight Go Away")

    # Initalize Quit constant
    QUIT = 3

    # Menu

    # Initalize control variable
    choice = 0

    while choice != QUIT:
        # Display menu & prompt user for choice
        print("\nChoose one of the following options")
        print('\t1. Display "10 ways to cut 500 calories" guideline.')
        print("\t2. Generate next semester expected weight table.")
        print("\t3. Quit.")
        choice = int(input("Option: "))

        # Drive menu options
        if choice == 1: # Guideline
            print("\nTry these 10 ways to cut 500 calories every day.")
            print("""
         *Swap you snack.
         *Cut one high-calorie treat.
         *DO NOT drink your calories.
         *Skip seconds.
         *Make low calorie substitutions.
         *Ask for a doggie bag.
         *Just say “no” to fried food.
         *Build a thinner pizza.
         *Use a smaller plate.
         *Avoid alcohol.
                """)
            print("Source: US National Library of Medicine")
            print()
        elif choice == 2: # Weight Table

            # Prompt user for starting weight (>=100)
            weight = int(input("Please enter a starting weight in pounds (>=100): "))

            # Validate
            while weight <= 100:
                print()
                print("Error ... Invalid length. Try again.")
                print()
                
                # Prompt user for starting weight (>=100)
                weight = int(input("Please enter a starting weight in pounds (>=100): "))

            # Display next semester weight table
            print("----------------")
            print("Month   Weight ")
            print("----------------")
            for month in range(1,7):
                weight -= 4
                print(" ", month, "   ", weight, "lb.",)

        elif choice == QUIT: # Quit
            print("\nGood Bye")
            print()
        else: # Invalid choice
            print("Error ... Invalid option. Try again.")
