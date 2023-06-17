#
#   Kayla Saniei
#
#   rpgv1.py
#
#   Version 1 of an RPG. This version will have an introduction, a
#   main menu, a story line, and will prompt the user for their name.
#

def main():
    # Introduction to game
    print("Welcome to SpaceTrail! ")
    print()
    
    # Prompts user for their name
    name = input("Please enter your name voyager: ")
    print()
    
    # Displays main menu
    print("Choose one of the following to get started: ")
    print(" 1) See Rules")
    print(" 2) Play Game")
    print(" 3) Exit")
    
    print()

    # prompts user for their main menu choice
    mainMenu = input("Which option do you want to choose: ")

    print()
    
    # Displays rules + story line regardless of input
    print("Wait", name, "! Before you start, you should know the rules and story line.")

    print()
    
    print("The rules are that you will be given multiple menu options. The choices you take will change")
    print("the path of the game. You will also be given points based on the options you choose.")
    print()
    
    # Display the story line
    print("Trying to get more supplies for your dying planet, you found yourself on a small little village after")
    print("your spaceship went haywire. The residents fixed your ship as best they could but informed you")
    print("the only way to make it back is through the SpaceTrail. Now, you have to make it back to your home")
    print("planet quickly while picking up the supplies your planet needs. Are you ready to embark on your journey?")
    print()

    # Play the game
    print()
    print("It seems you want to explore the uncharted.")
    print()
    
    # First menu
    print("Your first endeavor is to choose which planet you call your home.")
    print("Choose from one of the options below: ")
    print(" 1) An ice covered planet in the middle of a heatwave.")
    print(" 2) A jungle planet infested with an invasive planet species.")
    print(" 3) A hot planet that lost its strongest sun.")

    print()

    # Prompts user for their planet choice
    planet = input("Which planet do you want to call your home: ")

    print()
    
    # Second menu
    print("Your second endeavor is to choose what item remains intact from your ship.")
    print("Choose from one of the options below: ")
    print(" 1) The radio you use to communicate")
    print(" 2) A document outlining the plan to save your planet")
    print(" 3) The map of the trail")

    print()

    # Prompts user for their item choice
    item = input("Which item is most valuable to you: ")

    print()
    
    # Third menu
    print("Your third endeavor is to choose what alien superpower you have.")
    print("Choose from one of the options below: ")
    print(" 1) Accelerated Healing")
    print(" 2) Shapeshifting")
    print(" 3) Telepathy")

    print()

    # Prompts user for their planet choice
    power = input("Which superpower do you choose: ")

    print()
    
    # Exit
    print("Hope to see you again space explorer!")

main()
