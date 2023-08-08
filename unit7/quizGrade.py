#
#   Kayla Saniei
#
#   quizGrade.py
#
#   Read students' answers from a file and:
#       - Compare the key vs. answers list
#       - Calculate and display correct answers, incorrect answers,
#         and whether student has passed or not
#
#   The student file includes 15 lines each with answer to the
#   corresponding question. Responses are single character strings,
#   from A to D, uppercase
#
#   Input: Student name and answers file
#
#   Processing: 1. Create a list holding quiz answers
#               2. Prompt user for input
#               3. Compare key vs. answer list
#
#   Output: Number of correct answers, number of incorrect answers,
#           questions incorrectly answered, whether the student has
#           passed or failed the quiz
#

def main():

    # Intialize control variable
    again = "y"

    while again == "y":

        # Declare lists
        keyList = ["A", "C", "A", "B", "B", "D", "D", "A", "C", "A", "B", "C", "D", "C", "B"]
        studentList = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        correctList = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

        studentName = ""
        fileName = ""

        # if passsed quiz or not
        passQuiz = False

        numCorrect = 0
        numIncorrect = 0

        incorrectAnswers = ""

        print("Quiz Grading App")

        # Prompt user for student name
        studentName = input("\nEnter name of student: ")

        # Prompt user for file
        filename = input("\nName of file: ")
    
        try:
            # Open file
            inFile = open(filename, 'r')
    
            for i in range(15):
                studentList[i] = inFile.readline().rstrip('\n')
    
            # Close file
            inFile.close()

            for j in range(15):
                if keyList[j] == studentList[j]:
                    correctList[j] == True
                    numCorrect = numCorrect + 1
                else:
                    correctList[j] == False
                    numIncorrect = numIncorrect + 1
                    answer = j + 1
                    incorrectAnswers += str(answer)
                    incorrectAnswers += " "
                    

            if numCorrect >= 11:
                passQuiz = True
            else:
                passQuiz = False

            print()
            print(studentName, "Quiz Results")
            print("--------------------------------")
            print("Correct Answers: ", numCorrect)
            print("Incorrect Answers: ", numIncorrect)
            print("Incorrect Questions: ", incorrectAnswers)

            print()
            if passQuiz == True:
                print("Student passed the quiz.")
            else:
                print("Student failed the quiz.")
                

        except:
            print("Error ... could not process", filename, "file.")
            

        # Prompt user whether to try again
        again = input("\nWould you like to process another file (y/n)? ")
        again = again[0].lower()


    
