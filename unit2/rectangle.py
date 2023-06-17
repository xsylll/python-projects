#
#   Kayla Saniei
#
#   rectangle.py
#
#   Prompt user for the width and height of a rectangle,
#   calculate its area, and display the result
#
#   Processing: 1. Prompt user for rectangle's width & height
#               2. Calculate area
#                  area = width * height
#               3. Display result
#
#   Output: Area of rectangle

def main():
    #   Intro
    print("\nGeometry Calculator ...")
    print()

    #   Prompt user for rectangle's width & length
    width = eval(input("Please enter rectangle's width: "))
    height = eval(input("   \"      \"      \"   height: "))

    #   Calculate area
    area = width * height

    #   Display result
    print()
    print("The area of a", format(width, '.2f'), "by", format(height, '.2f'), "rectangle is", format(area, '.2f'))

main()
