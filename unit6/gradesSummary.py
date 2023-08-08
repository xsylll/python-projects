#
#   Kayla Saniei
#
#   gradesSummary.py
#
#   File processing program that generates a course grades summary report
#   based on the course, instructor, and student data stored in a file.
#
#   Input: course file
#
#   Processing: 1. Display Title
#               2. Prompt for file
#                   - input validation 
#               3. Opens file
#               4. Prints Course, Professor, and Term
#               5. Loops through file
#                   - Prints grade and student in a table
#                   - Counts number of students
#                   - Counts number of students passed
#                   - adds up sum of all grades
#               6. Prints students' performance table that shows
#                   - amount of students passed
#                   - amount of students failed
#                   - passing percentage
#                   - average grade
#               7. Closes file
#               8. Asks user if they want to process a new file
#
#   Output: a report showing course number, course description, instructor name,
#   term, list of students registered in the course, student's grades, number of
#   students that passed & failed the course, course passing percentage, and average
#   grade for the course
#

def main():
    # Intro
    print("Course Grades Summary Report")
    tryAgain = "y"
    while tryAgain == "y":
        try:
            passCounter = 0
            studentCounter = 0
            gradeTotal = 0
            
            courseFile = input("\nEnter name of course file: ")

            courseReport = open(courseFile, 'r')
            
            print()
            print("-----------------------------------------")
            print("   Broward College Grade Summary")
            print("-----------------------------------------")

            # Reads and prints course number and name from file
            courseName = courseReport.readline()
            print()
            print(courseName)

            # Reads course professor from file
            prof = courseReport.readline()

            # Reads course term from file
            year = courseReport.readline()

            print("Professor:" , prof, "Term:", year)

            print()

            print("Student Name               Grade")
            print("----------------------------------")

            # Assigns next line to student
            student = courseReport.readline()
            
            #removes the newline character
            student = student[:-1]
            while student!= "":
                #reads the next piece of data + assigns it to grades
                grade = courseReport.readline()
                #convert text to int
                grade = int(grade)
                
                print(student, "      	  ", grade)
                student = courseReport.readline()
                #removes newline character
                student = student[:-1]

                # adds up total amount of students
                studentCounter += 1

                # adds up sum of all grades
                gradeTotal += grade
                
                #count every grade over 60 to see how many students passed
                if grade >= 60:
                    passCounter +=1

            print()
            
            print("Students' Performance")
            print("----------------------------------")

            # prints amount of students passed
            print("Passed:", passCounter)

            # calculates + displays amount of students failed
            failCounter = studentCounter - passCounter
            print("Failed:", failCounter)

            # calculates + displays passing percentage
            passingPercent = (passCounter / studentCounter) * 100
            print("Passing Percent:", int(round(passingPercent, 0)),"%")

            # calculates + displays average grade
            averageGrade = (gradeTotal / studentCounter)
            print("Average Grade:", int(averageGrade))
            
            courseReport.close()
            
        # Exception Handling
        except FileNotFoundError:
            print("File not Found!")

        # lets user process as many files as they wish
        tryAgain = input("\nWould you like to process another file (y/n)? ").lower()
