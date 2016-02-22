# IPND Stage 2 Final Project

### This is paragraph_1. It is for level easy. It it used with the correct_respones list and the blanks list. More on this later when it is actively used in a function.
paragraph_easy = "In Python a value can be stored with a ___1___. A ___1___ can also be used to store a ___2___. A ___2___ is structured data and is denoted with square brackets. Much like cute little Russian dolls, one ___2___ can be inside another ___2___ this is called ___3___ ___2___s. Denoted with a plus sign, ___4___ joins to two strings together."

### This is paragraph_1. It is for level medium. It it used with the correct_respones list and the blanks list.
paragraph_medium = "Lists support ___5___, while strings do not, this means the programmer can change the value of a list after its created. You can an element to the end of a list with ___6___. It is good to start all functions and all classes with a ___7___ which can be recognized by the ___8___ symbol."

### This is paragraph_1. It is for level hard. It it used with the correct_respones list and the blanks list.
paragraph_hard = "A ___9___ is created with the def keyword. You specify the inputs a ___9___ takes by adding ___10___ separated by commas between the parentheses. ___9___s by default return ___11___ if you don't specify the value to return. ___10___ can be standard data types such as string, number, dictionary, tuple, and ___12___ or can be more complicated such as objects and lambda functions."

### These are the correct answers they get compared to what the user inputs later. More on that later when they are actively used in a function.
correct_responses = ["filler_because_index_starts_at_zero","variable","list","nested","concatenation","mutation","append","comment","hashtag","function","parameters","none","list"]

### These are the blanks, they get replaced with the correct answers as the user advances through the quiz. More on that later when they are actively used in a function.
blanks = ["filler_because_index_starts_at_zero", "___1___", "___2___", "___3___","___4___", "___5___","___6___", "___7___","___8___", "___9___","___10___", "___11___","___12___" ]


def take_quiz_easy(n):                 ### this function defines the coing for level 1 easy and runs lines 19 to 31
    new_paragraph = paragraph_easy     ### identifies what paragraph to use for quiz easy and renames it as new_paragraph
    while n < 5:                       ### creates loop, so user has to go through questions 1 through 4 before exiting loop
        response_to_question = raw_input("What should go in blank number " + str(n) + "?")   ### asks user what the answer is to n (what question they may be on at the time) and takes answer as raw_input
        if response_to_question == correct_responses[n]:      ### checks to make sure user response is same as correct answer, if it the same then the user advances
            print "Correct Answer!"                           ### prints statement letting the user know their answer is correct
            new_paragraph = new_paragraph.replace(blanks[n], correct_responses[n])   ### replaces blank of n [whatever question the user is on] with the correct response and updates the paragraph hence it's called new paragraph
            print new_paragraph                                                      ### prints the new_paragraph so user sees answer plugged in
            n = n + 1                  ### advances n, so if and when the loop continues user it asked to answer next question number and program knows it is working with next blank and next correct answer
        else:                          ### in the event the user does not enter correct answer, python will instead use the next line
            print "Incorrect answer"   ### print statement so user knows this is wrong, the program will not advance to the question/blank/answer, the loop will continue

    print "Congratulations! You have completed level easy! Go get a sugary snack as a reward, you genius you!"    ### print statement congratulating user on passing this level


def take_quiz_medium(n):              ### the coing for level 2 medium begins
    new_paragraph = paragraph_medium  ### identifies what paragraph to use for quiz medium and renames it as new_paragraph
    while n < 9:                      ### creates loop, so user has to go through questions 5 through 8 before exiting loop
        response_to_question = raw_input("What should go in blank number " + str(n) + "?")    ### asks user what the answer is to n (what question they may be on at the time) and takes answer as raw_input
        if response_to_question == correct_responses[n]:        ### checks to make sure user response is same as correct answer, if it the same then the user advances
            print "Correct Answer!"                             ### prints statement letting the user know their answer is correct
            new_paragraph = new_paragraph.replace(blanks[n], correct_responses[n])    ### replaces blank of n [whatever question the user is on] with the correct response and updates the paragraph hence it's called new paragraph
            print new_paragraph
            n = n + 1                 ### advances n, so if and when the loop continues user it asked to answer next question number and program knows it is working with next blank and next correct answer
        else:                         ### in the event the user does not enter correct answer, python will instead use the next line
            print "Incorrect answer."   ### print statement so user knows this is wrong, the program will not advance to the question/blank/answer, the loop will continue

    print "Congratulations! You have completed level medium! Go get a beer as a reward!"                       ### print statement congratulating user on passing this level


def take_quiz_hard(n):               ### the coing for level 3 hard begins
    new_paragraph = paragraph_hard   ### identifies what paragraph to use for quiz hard and renames it as new_paragraph
    while n < 13:                    ### creates loop, so user has to go through questions 9 through 12 before exiting loop
        response_to_question = raw_input("What should go in blank number " + str(n) + "?")    ### asks user what the answer is to n (what question they may be on at the time) and takes answer as raw_input
        if response_to_question == correct_responses[n]:         ### checks to make sure user response is same as correct answer, if it the same then the user advances
            print "Correct Answer!"                              ### prints statement letting the user know their answer is correct
            new_paragraph = new_paragraph.replace(blanks[n], correct_responses[n])     ### replaces blank of n [whatever question the user is on] with the correct response and updates the paragraph hence it's called new paragraph
            print new_paragraph
            n = n + 1                 ### advances n, so if and when the loop continues user it asked to answer next question number and program knows it is working with next blank and next correct answer
        else:                         ### in the event the user does not enter correct answer, python will instead use the next line
            print "Incorrect answer."  ### print statement so user knows this is wrong, the program will not advance to the question/blank/answer, the loop will continue

    print "Congratulations! You have completed the most difficult level!"        ### print statement congratulating user on passing this level


level = raw_input('Would you like difficulty level easy, medium, or hard?')  ### sets up the question of what level would the user like to start on
def select_difficulty(level):                                                ### sets up select_difficulty function with level parameter, which is applied in the next few lines
    if level == "easy" or level == "Easy":       ### if statement telling python where to do if user chooses easy
        print paragraph_easy                     ### prints paragraph_easy as defined way up on line 4
        n = 1                                    ### tells python we're beginning with n = 1 as in question 1, blank 1, answer 1
        take_quiz_easy(n)                        ### tells python to go to take_quiz_easy with that n from the line before  
    if level == "medium" or level == "Medium":   ### if statement telling python where to do if user chooses medium
        print paragraph_medium                   ### prints paragraph_medium
        n = 5                                    ### tells python we're beginning with n = 5
        print "So you think you're smart enough to skip a level? Straight to question " + str(n) + " for you."
        take_quiz_medium(n)                      ### tells python to go to take_quiz_medium with that n from the line before
    if level == "hard" or level == "Hard":       ### if statement telling python where to do if user chooses hard
        print paragraph_hard                     ### prints paragraph_hard
        n = 9                                    ### tells python we're beginning with n = 9
        print "Oh you wanna start with the hard level? Bring it on with question " + str(n) + ". Remember, you asked for it."
        take_quiz_hard(n)                        ### tells python to go to take_quiz_hard with that n from the line before

print select_difficulty(level)                   ### actually prints out the question for the user to answer
