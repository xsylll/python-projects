#
#   Kayla Saniei
#
#   bigGame.py
#
#   Program will play a MadLib game with the user
#

def main():
    print("MadLib Game ...")
    
    print("Enter the following words: ")
    
    # Prompts user for a plural noun
    PNOUN1 = input("Plural Noun: ")
    
    # Prompts user for their first name
    FNAME = input("Person's First Name: ")

    # Prompts user for a noun
    NOUN1 = input("Noun: ")

    # Prompts user for their last name
    LNAME = input("Person's Last Name: ")

    # Prompts user for another plural noun
    PNOUN2 = input("Plural noun: ")

    # Prompts user for a place
    PLACE1 = input("Place: ")

    # Prompts user for a third plural noun
    PNOUN3 = input("Plural Noun: ")

    # Prompts user for another place
    PLACE2 = input("Place: ")

    # Prompts user for a fourth plural noun
    PNOUN4 = input("Plural Noun: ")

    # Prompts user for a second noun
    NOUN2 = input("Noun: ")

    # Prompts user for an adjective
    ADJECTIVE1 = input("Adjective: ")

    # Prompts user for a second adjective
    ADJECTIVE2 = input("Adjective: ")

    # Prompts user for a verb
    VERB = input("Verb: ")

    # Prompts user for a third adjective
    ADJECTIVE3 = input("Adjective: ")

    # Displays the MadLib
    print("The Big Game !!!")
    print("Hello there, sports", PNOUN1,"!")
    print("This is",FNAME ,",talking to you from the press", NOUN1)
    print("in", LNAME ,"Stadium, where 57,000 cheering", PNOUN2)
    print("Have gathered to watch (the)" , PLACE1 , PNOUN3)
    print("take on (the)", PLACE2 , PNOUN4, ".")
    print("Even though the", NOUN2 , "is shining, it’s a/an" , ADJECTIVE1)
    print("cold day with the temperature in the", ADJECTIVE2 , "20s.")
    print("We’ll be back for the opening", VERB , "-off after a few words")
    print("from our" , ADJECTIVE3 , "sponsor.")

main()
