#
#   Kayla Saniei
#
#   rpgv4.py
#
#   Version 4 of an RPG. This version uses functions.
#
#   Input: Name, main menu choice (1-3), and three different submenu choices (1-3)
#
#   Processing: 1. Displays an introduction
#               2. Declares and initalizes variables used throughout the code
#               3. Displays main menu choices (1-3), including see rules, play game, and exit choices. 
#               4. Prompts user for main menu choice. Validate and loops.
#               5. If user chose 1, displays story line and rules
#               6. If user chose 2, prompts user for their name and three submenues appear.
#               7. Prompts user for their choice for each submenu, calculates and displays total points based on what the choice was.
#               8. If user chose 3 from the main menu, game will display goodbye message.
#
#   Output: Corresponding choice from what the user chose from menus. If user decided to play the game, output would be total points. 
from random import randrange

def main():
    # Introduction to game
    print("Welcome to SpaceTrail! ")
    print()

    # Declare and initalize variables
    name = "blank"
    mainMenu = 0
    planet = 0
    item = 0
    power = 0
    points = 0

    # Initalize randomPlanet
    randomPlanet = 0

    # Initalize randomItem
    randomItem = 0

    # Initalize points from power menu
    powerPoints = 0
    
    # Initalize Quit constant
    QUIT = 3
    
    while mainMenu != QUIT: # Main menu while loop
        
    
        # Displays main menu
        print("Choose one of the following to get started: ")
        print(" 1) See Rules")
        print(" 2) Play Game")
        print(" 3) Exit")
        
        print()
        
        # prompts user for their main menu choice
        mainMenu = int(input("Which option do you want to choose: "))

        print()
        
        # Displays rules + story line
        if mainMenu == 1:
            rulesAndStoryline()
        elif mainMenu == 2:

            points = 0
            
            # Prompts user for their name
            name = input("Please enter your name voyager: ")
            
            # Play the game
            print()
            print("It seems you want to explore the uncharted.")

            # First menu
            points += planetMenu()
            
            # Displays total points
            displayPoints(name, points)
            
            # Second menu
            points += itemMenu()

            # Displays total points
            displayPoints(name, points)

            # Third menu
            points += powerMenu()
            
            # Displays total points
            displayPoints(name, points)

        elif mainMenu == 3:
            # Exit
            print("Hope to see you again space explorer!")
        elif mainMenu <= 0 or mainMenu >= 4: # Validation
            print("Error.. Invalid number choice")

#
#   rulesAndStoryline()
#
#   Displays the rules and the storyline. Does not return a value.
#

def rulesAndStoryline():

    # Displays rules
    print("The rules are that you will be given multiple menu options. The choices you take will change")
    print("the path of the game. You will also be given points based on the options you choose.")
    print()
    
    # Display the story line
    print("Trying to get more supplies for your dying planet, you found yourself on a small little village after")
    print("your spaceship went haywire. The residents fixed your ship as best they could but informed you")
    print("the only way to make it back is through the SpaceTrail. Now, you have to make it back to your home")
    print("planet quickly while picking up the supplies your planet needs. Are you ready to embark on your journey?")
    print()

#
#   planetMenu()
#
#   Displays first menu option. Prompts user for their choice.
#
#   Return Value: Points based randomly on user choice
#

def planetMenu():
    # First menu
    print()
    print("Your first endeavor is to choose which planet you call your home.")
    print("Choose from one of the options below: ")
    print(" 1) An ice covered planet in the middle of a heatwave.")
    print(" 2) A jungle planet infested with an invasive planet species.")
    print(" 3) A hot planet that lost its strongest sun.")
    print()

    # Prompts user for their planet choice
    planet = int(input("Which planet do you want to call your home: (1-3) "))
    print()

    # Validate 
    while planet > 3 or planet < 1:
        print("Invalid choice.")
        planet = int(input("Which planet do you want to call your home: (1-3) "))

                
    # Assigns points to what the user chose
    if planet == 1:
        randomPlanet = randrange(1,21) # generates random number
    elif planet == 2:
        randomPlanet = randrange(1,21) # generates random number 
    elif planet == 3:
        randomPlanet = randrange(1,21) # generates random number

    return randomPlanet

#
#   itemMenu()
#
#   Displays second menu option. Prompts user for their choice.
#
#   Return Value: Points based randomly on user choice
#

def itemMenu():

    # Second Menu
    print("Your second endeavor is to choose what item remains intact from your ship.")
    print("Choose from one of the options below: ")
    print(" 1) The radio you use to communicate")
    print(" 2) A document outlining the plan to save your planet")
    print(" 3) The map of the trail")
    print()
            
    # Prompts user for their item choice
    item = int(input("Which item is most valuable to you: (1-3) "))
    print()

    # Validate
    while item > 3 or item < 1:
        print("Invalid choice.")
        item = int(input("Which item is most valuable to you: (1-3) "))

    # Assigns points to what the user chose
    if item == 1:
        randomItem = randrange(1,21) # generates random number 
    elif item == 2:
        randomItem = randrange(1,21) # generates random number
    elif item == 3:
        randomItem = randrange(1,21) # generates random number

    return randomItem
#
#   powerMenu()
#
#   Displays third menu option. Prompts user for their choice.
#
#   Return Value: Points based on user choice
#

def powerMenu():

    # Third menu
    print("Your third endeavor is to choose what alien superpower you have.")
    print("Choose from one of the options below: ")
    print(" 1) Accelerated Healing")
    print(" 2) Shapeshifting")
    print(" 3) Telepathy")
    print()
            
    # Prompts user for their planet choice
    power = int(input("Which superpower do you choose: "))
    print()

    # Validate / New
    while power > 3 or power < 1:
        print("Invalid choice.")
        power = int(input("Which superpower do you choose: "))

    powerPoints = 0
    
    # Assigns points to what the user chose
    if power == 1:
        powerPoints += 2
    elif power == 2:
        powerPoints += 6
    elif power == 3:
        powerPoints += 10

    return powerPoints

#
#   displayPoints(name, points)
#
#   Takes parameters of user's name and current points
#
#   Return Value: Points based on user choice
#

def displayPoints(name, points):
    print("Good choice", name, ". You now have", points, "total points.")
    print()
