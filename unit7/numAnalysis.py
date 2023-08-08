#
#   Kayla Saniei
#
#   numAnalysis.py
#
#   Read a series of numbers from a file, and:
#       - Display the values in ascending order
#       - Determine & Display the lowest & highest numbers
#       - Calculate & Display the average of the numbers
#
#   Input: List of numbers stored in a file
#
#   Processing: 1. Read numbers from a file into a numeric list
#               2. Display values in ascending order
#                  Sort list
#                  Display values
#               3. Determine & display lowest & highest numbers
#               4. Calculate & display average of numbers
#
#   Output: Ordered list of numbers in a file
#           Lowest & highest numbers
#           Average of the numbers
#

def main():
    # Initialize variables
    tryAgain = 'y'

    # Intro
    print("\nNumber Analysis App ...")

    while tryAgain == 'y':

        # Read numbers from a file into a list of numeric values
        numberLst = readNumbers()

        if len(numberLst) != 0:
            # Display values in ascending order
            displaySortedList(numberLst)

            # Determine & display lowest & highest values
            print("Lowest  number:", min(numberLst))
            print("Highest number:", max(numberLst))

            # Calculate & display average of numbers
            average = calcAverage(numberLst)
            print("Average of numbers: {0:.1f}".format(average))

        # Prompt user whether to try again
        tryAgain = input("\nWould you like to process another file (y/n)? ")
        tryAgain = tryAgain[0].lower()

#
#   readNumbers()
#
#   Prompts user for the name of a file, and returns its contents
#   as a list of numbers
#
#   Return Value: List of numbers
#
def readNumbers():
    # Intialize list
    numLst = []
    
    # Prompt user for file
    filename = input("\nName of file: ")

    try:
        # Open file
        inFile = open(filename, 'r')

        # Read values into list
        numLst = inFile.readlines()

        # Close file
        inFile.close()

        # Convert list contents to numbers
        for i in range(len(numLst)):
            numLst[i] = eval(numLst[i])
            
    except:
        print("Error ... could not open file.")

    return numLst

#
#   displaySortedList(numLst)
#
#   Displays the list of values stored in the list numLst
#   in ascending order
#
#   Return Value: None
#
def displaySortedList(numLst):
    # Copy list to a temp list
    tempLst = [] + numLst
    
    # Sort temp list in ascending order
    tempLst.sort()

    # Display values
    print("\nList of Values ...")
    for value in tempLst:
        print("\t", value)

    print()

#
#   calcAverage(numLst)
#
#   Calculates the average of the numbers contained in the list
#   numLst, and returns it back to the caller
#
#   Return Value: Average of numbers
#

def calcAverage(numLst):
    # Initialize accumulator
    sumNumbers = 0

    # Calculate sum of numbers
    for value in numLst:
        sumNumbers = sumNumbers + value

    # Calculate average
    average = sumNumbers / len(numLst)

    return average

# Call main()
main()
