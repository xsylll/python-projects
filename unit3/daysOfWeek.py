#
#   Kayla Saniei
#
#   daysOfWeek.py
#
#   Prompt user for a number (1-7), determine & display
#   the corresponding day of the week.
#
#   Input: A number (1-                 7)
#
#   Processing 1. Prompt user for a number (1-7)
#              2. Determine corresponding day of week
#                 1 - Monday
#                 2 - Tuesday
#                 ...
#                 7 - Sunday
#              3. Display result
#
#   Output: The corresponding day of the week (Monday-Sunday)
#
def main():
    # Intro
    print("\nDays of the Week App ...")
    print()

    # Prompt user for a number (1-7)
    number = int(input("Please enter a number (1-7): "))

    # Determine corresponding day of week
    if number == 1:
        day = "Monday"
    elif number == 2:
        day = "Tuesday"
    elif number == 3:
        day = "Wednesday"
    elif number == 4:
        day = "Thursday"
    elif number == 5:
        day = "Friday"
    elif number == 6:
        day = "Saturday"
    elif number == 7:
        day = "Sunday"
    else:
        # Invalid number
        day = None
        print("Error ... Invalid number. Try Again.")

    # Display result
    if day != None:
        print("The day ", number, " is ", day, sep="")
        
main()
