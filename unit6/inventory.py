#
#   Kayla Saniei
#
#   inventory.py
#
#   Menu-Driven Interface program that allows the user to:
#       1. Create a new Inventory file
#       2. Add an item to the Inventory
#       3. Display items in the Inventory
#       4. Generate Inventory Price Summary
#       5. Quit
#
#   Input: Name of Inventory file
#          Item record field data - Description, Quantiy & Price
#
#   Processing: 1. Display menu & prompt user for choice
#               2. Drive menu options
#                   1 - Create new Inventory file
#                       Open file in writing mode
#                       Close file
#                   2 - Add item Inventory
#                       Prompt user for item record field data
#                       Open file for appending
#                       Write item record to file
#                       Close file
#                   3 - Display items in Inventory
#                       Open file for reading
#                       While there are records in the file:
#                           Read description, quantity, price
#                           Display item record data
#                       Close file
#                   4 - Generate Inventory Price Summary
#                       Open file for reading
#                       Initialize item counter, price accumulator, lowest & highest
#                       While there are records in the file:
#                           Read description, quantity, price
#                           Increment item counter
#                           Update price accumulator
#                           Determine if item price is new lowest / highest
#                       Calculate average price
#                           average price = price accumulator / item counte
#                       Display Inventory price summary
#                   5 - Quit
#
#   Output: List of items in the Inventory
#           Inventory Price Summary
#


def main():
    # Intro
    print("Inventory Control App ...")

    # Initialize constants & variables
    QUIT = 5    # Option associated with Quit - to make menu easier to expand
    choice = 0  # Menu control variable

    while choice != QUIT:
        # Display menu & prompt user for choice
        print("\nChoose one of the following options")
        print("\t1. Create new Inventory file.")
        print("\t2. Add item to Inventory.")
        print("\t3. Display items in Inventory.")
        print("\t4. Generate Inventory Price Summary.")
        print("\t5. Quit")
        choice = int(input("Option: "))

        # Drive menu options
        if choice == 1: # New file
            print("\nCreating new Inventory file ...", end=" ")
            createFile("inventory.txt")
            print("\"inventory.txt\" successfully created")
            
        elif choice == 2: # Add item
            print("\nAdding item to Inventory ...")
            
            # Prompt user for item information
            description, quantity, price = getItem()
            
            # Append item to inventory.txt
            addItem(description, quantity, price, "inventory.txt")
            
        elif choice == 3: # Display file
            print("\nDisplaying items in Inventory ...")
            displayFile("inventory.txt")
            
        elif choice == 4: # Process file data
            print("\nGenerating Inventory Price Summary ...")
            priceSummary("inventory.txt")
            
        elif choice == QUIT: 
            print("\nGood Bye ...")
            print()
            
        else: # Invalid
            print("Error ... Invalid option. Try again")

#
#   createFile(filename)
#
#   Creates an empty file named filename
#
#   Return Value: None
#
def createFile(filename):
    # Open file for writing - create a new one if it already exists
    outFile = open(filename, "w")

    # Close file
    outFile.close()

#
#   getItem()
#
#   Prompts user for Inventory record fields:
#       - Item description    <string>
#       - Item quantity (>=0) <int>
#       - Item price (>=0)    <float>
#   and returns them back to the caller
#
#   Return Values: <Item Descripton> <Item Quatity> <Item Price>
#
def getItem():

    print("\nPlease enter the following data ...")

    # Prompt user for item description, quantity & price
    description = input("\t" + format("Item Description:", "<20s"))

    # Quantity (>=0)
    quantity = -1
    while quantity < 0:
        try:
            quantity = int(input("\t" + format("Item Quantity:", "<20s")))

            if quantity < 0:
                print("\tError ... Invalid quantity. Try again.")
        except ValueError:
            print("\tError ... Quantity must be a whole number. Try again.")

    # Price (>=0)
    price = -1
    while price < 0:
        try:
            price = float(input("\t" + format("Item Price:", "<20s")))

            if price < 0:
                print("\tError ... Invalid price. Try again.")
        except ValueError:
            print("\tError ... Price must be a number. Try again.")

    return description, quantity, price

#
#   addItem(desc, qty, price, filename)
#
#   Appends and Inventory record with fields:
#       - Item description <desc>
#       - Item quantity    <qty>
#       - Item price       <price>
#   to the file named filename, one field per line
#
#   Return Value: None
#
def addItem(desc, qty, price, filename):
    try:
        # Open file for appending
        outFile = open(filename, 'a')

        # Write item data to file - one field per line
        outFile.write(desc  + '\n')
        outFile.write(str(qty)   + '\n')
        outFile.write(str(price) + '\n')

        # Close file
        outFile.close()
    except:
        print("Fatal Error ... Could not open file", filename)

#
#   displayFile(filename)
#
#   Displays a table containing Inventory records stored in file named filename
#
#   Return Value: None
#
def displayFile(filename):

    try:
        # Open file
        inFile = open(filename, "r")

        # Display Table Header
        print()
        print("{0:<20s} {1:^10s} {2:^15s}".format("Description", "Quantity", "Price"))
        print("-"*47)

        # Read file one record at a time & display it

        # Read first item description
        itemDesc = inFile.readline() 
        
        while itemDesc != "":
            # Read item quatity & price
            itemQty   = inFile.readline()
            itemPrice = inFile.readline()

            # Strip \n from fields
            itemDesc  = itemDesc.rstrip('\n')
            itemQty   = itemQty.rstrip('\n')
            itemPrice = itemPrice.rstrip('\n')

            # Convert numeric values
            itemQty = eval(itemQty)
            itemPrice = eval(itemPrice)

            # Display record
            print("{0:<20s} {1:^10d} {2:>12,.2f}".format(itemDesc, itemQty, itemPrice))

            #Read next item description
            itemDesc = inFile.readline()
            
        # Close file
        inFile.close()
    except FileNotFoundError:
        print("Fatal Error ...", filename, "not found.")
    except IOError:
        print("Fatal Error ... could not read", filename)

#
#   priceSummary(filename)
#
#   Reads item records from Inventory file named file name, determines
#   and displays:
#       - Number of items in Inventory
#       - Lowest  price in Inventory
#       - Highest price in Inventory
#       - Average price of items in Inventory
#
#   Return Value: None
#
def priceSummary(filename):
    # Import library
    import sys
    
    # Intialize Variables
    itemCount = 0                   # Number of items in Inventory
    lowPrice  = sys.float_info.max  # Lowest price in Inventory
    highPrice = sys.float_info.min  # Highest price in Inventory
    priceSum  = 0.0                 # Sum of prices in Inventory
    priceAvg  = 0.0                 # Average price of items in Inventory

    try:
        # Open file
        inFile = open(filename, "r")

        # Read file one record at the time to determine
        #   - Number of items in Inventory
        #   - Lowest  price in Inventory
        #   - Highest price in Inventory
        #   - Sum of prices in Inventory

        # Read first item description
        itemDesc = inFile.readline()

        while (itemDesc != ""):
            # Read item quatity & price
            itemQty   = inFile.readline()
            itemPrice = inFile.readline()

            # Convert price to numeric value
            itemPrice = eval(itemPrice)

            # Update counter & accumulator
            itemCount = itemCount + 1
            priceSum = priceSum + itemPrice

            # Check whether lowest / highest price
            if itemPrice < lowPrice:
                lowPrice = itemPrice

            if itemPrice > highPrice:
                highPrice = itemPrice

            #Read next item description
            itemDesc = inFile.readline()

        # Close file
        inFile.close()

        # Calculate average price
        priceAvg = priceSum / itemCount

        # Display price summary information
        print("\nInventory Price Summary")
        print("-"*30)
        print("{0:<20s} {1:d}".format("Number of Items:", itemCount))
        print("{0:<20s} ${1:,.2f}".format("Lowest   Price:", lowPrice))
        print("{0:<20s} ${1:,.2f}".format("Highest  Price:", highPrice))
        print("{0:<20s} ${1:,.2f}".format("Average  Price:", priceAvg))
    except FileNotFoundError:
        print("Fatal Error ...", filename, "not found.")
    except IOError:
        print("Fatal Error ... could not read", filename)

# Call main()
main()
