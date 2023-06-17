#
#   Kayla Saniei
#
#   calories.py
#
#   This program prompts the user for the number of cookies consumed and,
#   based on the calories per serving, calculates and displays the number of
#   calories consumed.
#
#   Input:  Number of cookies per bag
#           Number of serving per bag
#           Number of calories per serving
#           Number of calories consumed
#
#   Processing: 1. Prompt user for number of cookies consumed
#               2. Calculate number of cookies per serving
#               3. Calculate number of calories per cookie
#               4. Calculate number of calories consumed
#               5. Display result
#
#   Output: Number of calories consumed
#

def main():
    # Initialize constants
    COOKIES_PER_BAG = 40
    NUM_SERVINGS = 10
    CALORIES_PER_SERVING = 300

    # Intro
    print("Calorie Counter App ...")
    print()

    # Prompt user for number of cookies consumed
    cookiesConsumed = eval(input("Please enter number of cookies consumed: "))

    # Calculate number of cookies per serving
    cookiesPerServing = COOKIES_PER_BAG / NUM_SERVINGS

    # Calculate number of calories per cookie
    caloriesPerCookie = CALORIES_PER_SERVING / cookiesPerServing

    # Calculate total calories consumed
    caloriesConsumed = cookiesConsumed * caloriesPerCookie

    # Display calories consumed
    print("\nYou consumed", caloriesConsumed, "calories.")

main()
