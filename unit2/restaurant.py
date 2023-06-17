#
#   Kayla Saniei
#
#   restaurant.py
#
#   Prompts user for cost of a meal (food and drinks) consumed at a resturant,
#   and produces a bill detailing tax, tip, and total amounts.
#

def main():
    # Initialize constants
    TAX = 0.075
    TIP = 0.18
    
    # Intro
    print("\nResturant Bill Generator ...")
    print()

    # Prompts user for cost of food & drinks
    food = eval(input("Please enter cost of food: "))
    drink = eval(input("  \"      \"   cost of drinks: "))

    # Calculate cost of meal
    costOfMeal = food + drink

    # Calculate tax of meal
    taxOfMeal = TAX * costOfMeal

    # Calculate subtotal after tax
    subTotal = taxOfMeal + costOfMeal
    
    # Calculate tip of meal
    tipOfMeal = TIP * subTotal

    # Calculate total
    total = subTotal + tipOfMeal

    # Displays the bill detailing tax, tip, and total amounts
    print()
    print("Restaurant Bill")
    print("------------------------------")
    print()
    print("Cost of Meal:", format(costOfMeal, '.2f'), sep='\t$\t')
    print("Tax Amount:", format(taxOfMeal, '.2f'), sep='\t$\t')
    print("Tip Amount:", format(tipOfMeal, '.2f'), sep='\t$\t')
    print("\t\t--------------")
    print("Total:", format(total, '.2f'), sep='\t\t$\t')

main()
    
