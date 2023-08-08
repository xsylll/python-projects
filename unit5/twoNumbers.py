#
#   Kayla Saniei
#
#   twoNumbers.py
#
#   Prompt user for two values i & j (i<=j), calculate
#   and display:
#       - List of numbers from i to j (inclusive)
#       - Sum of numbers from i to j
#       - Product of numbers from i to j
#       - Average of numbers from i to j
#
#   Input: Two values - i & j (i<=j)
#
#   Processing: 1. Prompt user for two values (i & j where i<=j)
#               2. Determine & Display
#                   - List of numbers from i to j (inclusive)
#                   - Sum of numbers from i to j
#                   - Product of numbers from i to j
#                   - Average of numbers from i to j
#
#   Output: List of numbers from i to j (inclusive)
#           Sum, product, & average of numbers from i to j (inclusive)
#

def main():
    # Intro
    print("\nPlaying with Numbers App")

    tryAgain = "y"

    while tryAgain == "y":
        # Prompt user for two values
        i, j = getValues()

        # Determine & Display list of numbers
        print("From", i, "to", j, ":", listValues(i,j))

        # Calculate and display sum, product, & average of number
        print("\n\tSum of Values:", format(sumValues(i,j), '10d'))
        print("\tProduct of Values:", format(productValues(i,j), '10d'))
        print("\tAverage of Values:", format(averageValues(i,j), '10.3f'))

        # Prompt user whether to try again
        tryAgain = input("\nWould you like to try again (y/n)? ").lower()

#
#   getValues()
#
#   Prompt user for two values n1, n2, & return them back
#   to the caller so n1 <= n2
#
#   Return Values: n1, n2
#

def getValues():
    # Prompt user
    n1, n2 = eval(input("\nPlease enter two numbers (seperated by ,): "))

    # Swap values if needed
    if n1 > n2:
        temp = n1
        n1 = n2
        n2 = temp

    # Return numbers to the caller
    return n1, n2

#
#   listValues(n1, n2)
#
#   Create & return, as a string, the list of numbers
#   from n1 to n2 (inclusive)
#
#   Return Value: String containing the list of number from n1 to n2 (inclusive)
#

def listValues(n1, n2):
    # Initalize string of values
    lstString = ""

    # Build the string one number at a time
    for value in range(n1, n2+1):
        lstString = lstString + str(value) + " "

    # Return string to the caller
    return lstString

#
#   sumValues(n1, n2)
#
#   Calculate the sum of the values from n1 to n2 (inclusive)
#   and return it back to the caller
#
#   Return Value: Sum of numbers from n1 to n2 (inclusive)
#

def sumValues(n1, n2):
    # Initalize accumulator
    total = 0

    # Add values one step at a time
    for value in range(n1, n2+1):
        total += value

    # Return sum to the caller
    return total

#
#   productValues(n1, n2)
#
#   Calculate the product of the values from n1 to n2 (inclusive)
#   and return it back to the caller
#
#   Return Value: Product of numbers from n1 to n2 (inclusive)
#

def productValues(n1, n2):
    # Initalize accumulator
    product = 1

    # Multiply values one step at a time
    for value in range(n1, n2+1):
        product *= value

    # Return product to the caller
    return product

#
#   averageValues(n1, n2)
#
#   Calculate the average of the values from n1 to n2 (inclusive)
#   and return it back to the caller
#
#   Return Value: Average of numbers from n1 to n2 (inclusive)
#

def averageValues(n1, n2):
    # Calculate average
    total = sumValues(n1, n2)
    count = n2 - n1 + 1

    average = total / count

    # Return average to the caller
    return average
