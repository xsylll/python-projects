#
#   Kayla Saniei
#
#   roster.py
#
#   Read a series of student records from a course file and:
#       - Display the list of students in alphabetical order
#
#   The student records include the following fields - one line per field:
#       - Last name
#       - First name
#       - GPA
#
#   Input: Series of student records stored in a file
#
#   Processing: 1. Read student records into a two-dimensional list
#                  where each row corresponds to a student record, each
#                  column to a field - <last name> <first name> <gpa>
#               2. Display list of students in alphabetical order
#                   Sort list (using last name)
#                   Display student records
#
#   Output: Sorted list of students stored in a file
#

def main():
    # Intialize control variable
    tryAgain = 'y'
    
    # Intro
    print("\nCourse Roster App ...")

    while tryAgain == 'y':
        # Read student records into a two-dimensional list
        stdLst = readStudents()

        if len(stdLst) != 0:
            # Display list of students
            displayStudents(stdLst)

        # Prompt user whether to try again
        tryAgain = input("\nWould you like to process another file (y/n)? ")
        tryAgain = tryAgain[0].lower()

#
#   readStudents()
#
#   Prompts user for the name of a file, and returns its contents
#   as a two-dimensional list of students, where each row corresponds
#   to a student, and each column to a field <last name>, <first name>,
#   and <GPA>
#
#   Return Value: Two-Dimensional list of student records
#
def readStudents():
    # Intialize students'list
    studentsLst = []

    # Prompt user for file
    filename = input("\nName of file: ")

    try:
        # Open file
        inFile = open(filename, 'r')

        # Read each student record into students list

        # Read first student's last name
        stdLName = inFile.readline().rstrip('\n')
        
        while stdLName != "":
            # Read <first name> and GPA
            stdFName = inFile.readline().rstrip('\n')
            stdGPA = float(inFile.readline())
            
            # Append student's record to list
            studentsLst = studentsLst +[[stdLName, stdFName, stdGPA]]

            # Read next student's last name
            stdLName = inFile.readline().rstrip('\n')

        # Close file
        inFile.close()

    except:
        print("Error ... could not process", filename, "file.")

    return studentsLst

#
#   displayStudents(studentsLst)
#
#   Displays the students (<last name>, <first name> and <gpa>)
#   stored in the list studentsLst. The students are shown in
#   alphabetical order according to their <last name>
#
#   Return Value: None
#   
def displayStudents(studentsLst):
    # Heading
    print("\nList of students ...")
    print()
    print("{0:<30s}{1}".format("Name", "GPA"))
    print("-"*35)

    # Copy students list to a temp list & sort it
    tempLst = [] + studentsLst
    tempLst.sort()
    
    # Display student records in alphabetical order
    for stdIdx in range(len(tempLst)):
       print("{0:<15s}".format(tempLst[stdIdx][0]), end="")
       print("{0:<15s}".format(tempLst[stdIdx][1]), end="")
       print("{0}".format(tempLst[stdIdx][2]))

# Call main()
main()
