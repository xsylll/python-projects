#
#   Kayla Saniei
#
#   sphereMenu.py
#
#   Menu-driven interface program that allows the user to :
#       1. Calculate surface area of a sphere
#       2. Calculate the volume of a sphere
#       3. Quit
#
#   Input: Radius of a sphere
#
#   Processing: Display menu & prompt user for choice
#                   1. Calculate surface area of a sphere
#                   2. Calculate the volume of a sphere
#                   3. Quit
#               Drive user's choice:
#                   1 -> Prompt user for radius
#                        Calculate surface area
#                           area = 4 * math.pi * radius ** 2
#                        Display result
#                   2 -> Prompt user for radius
#                        Calculate volume
#                           volume = 4/3 * math.pi * radius ** 3
#                        Display result
#                   3 -> Quit
#
#   Output: Surface Area/Volume of a sphere
#

# Import library
import math

def main():
    # Intro
    print("\Sphere Geometry Calculator")

    # Display menu & prompt user for choice
    choice = 0

    while choice != 3:
        # Display menu & prompt user for choice
        choice = displayMenu()

        # Drive menu options
        if choice == 1:
            print("\Surface Area of Sphere")
            # Prompt user for radius
            radius = getRadius()

            # Calculate surface area
            area = calcArea(radius)

            # Display result
            dispResult("Surface Area", area)
        elif choice == 2:
            print("\Volume of Sphere")
            # Prompt user for radius
            radius = getRadius()

            # Calculate volume
            volume = calcVolume(radius)

            # Display result
            dispResult("Volume", volume)
        else: # Quit
            print("Good Bye")
            print()

#
#   displayMenu()
#
#   Displays menu & prompt user for choice
#   Returns choice (1-3) back to the caller
#

def displayMenu():
    
    # Initalize control variable
    choice = 0

    while choice < 1 or choice > 3:
        # Display menu & prompt user for choice
        print("\nChoose one of the following options:")
        print("\t1. Calculate surface area of a sphere")
        print("\t2. Calculate the volume of a sphere")
        print("\t3. Quit")
        choice = int(input("Option: "))
        
        # Validate
        if choice < 1 or choice > 3:
            print("Error .. Invalid option. Try again.")

    # Return choice
    return choice

#
#   getRadius
#
#   Prompts user for radius (>0) and returns it back
#   to the caller
#

def getRadius():
    # Initalize control variable
    r = -1
    
    while r < 0:
        # Prompt user for radius
        r = eval(input("\nEnter radius: "))

        # Validate
        if r < 0:
            print("Error .. Invalid option. Try again.")

    # Return radius
    return r

#
#   calcArea(r)
#
#   Calculates the surface area of a sphere whose radius is r,
#   and returns it back to the caller
#

def calcArea(r):
    # Calc area
    a = 4 * math.pi * r ** 2
    
    # Return a
    return a

#
#   calcVolume(r)
#
#   Calculates the volume of a sphere whose radius is r,
#   and returns it back to the caller
#

def calcVolume(r):
    # Calc volume
    v = 4/3 * math.pi * r ** 3
    
    # Return volume
    return v

#
#   dispResult(gFormula, value)
#
#   Displays the value of the geometric formula (gFormula)
#   with a precision of two decimal places
#

def dispResult(gFormula, value):
    print("The", gFormula, "of the sphere is", format(value, '.2f'))

