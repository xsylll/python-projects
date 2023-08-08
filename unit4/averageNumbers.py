#
#   Kayla Saniei
#
#   averageNumbers.py
#
#   Calculate the average of a series of numbers entered by a user
#
#   Input: Series of numbers
#
#   Processing: 1. Initalize accumulator (sumNumbers) & counter (countNumbers)
#               2. While there are numbers:
#                       Prompt user for a number
#                       Add number to accumulator
#                       Increment counter
#               3. Calculate average
#                       average = sumNumbers / countNumbers
#               4. Display result
#
#   Output: Average of a series of numbers
#
def main():
    # Intro
    print("\nAverage Calculator App ...")

    # Initalize loop control variable
    moreData = 'y'

    # Initalize accumulator
    sumNumbers = 0

    # Initialize counter
    countNumbers = 0

    # Test control variable
    while moreData.lower() == 'y':
        # Prompt user for a number
        number = eval(input("\nEnter a number: "))

        # Update accumulator
        sumNumbers += number

        # Update counter
        countNumbers += 1

        # Update control variable
        moreData = input("Do you have another number (y/n)?")

    # Calculate average
    average = sumNumbers / countNumbers

    # Display result
    print("\nThe average is: ", format(average, '.3f'))
