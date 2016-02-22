# IPND Stage 2 Final Project

### This is paragraph_1. It is for level easy.
paragraph_easy = "In Python a value can be stored with a ___1___. A ___1___ can also be used to store a ___2___. A ___2___ is structured data and is denoted with square brackets. Much like cute little Russian dolls, one ___2___ can be inside another ___2___ this is called ___3___ ___2___s. Denoted with a plus sign, ___4___ joins to two strings together."

### This is paragraph_1. It is for level medium.
paragraph_medium = "Lists support ___5___, while strings do not, this means the programmer can change the value of a list after its created. You can an element to the end of a list with ___6___. It is good to start all functions and all classes with a ___7___ which can be recognized by the ___8___ symbol."

### This is paragraph_1. It is for level hard.
paragraph_hard = "A ___9___ is created with the def keyword. You specify the inputs a ___9___ takes by adding ___10___ separated by commas between the parentheses. ___9___s by default return ___11___ if you don't specify the value to return. ___10___ can be standard data types such as string, number, dictionary, tuple, and ___12___ or can be more complicated such as objects and lambda functions."

### The blanks and the correct answers to fill them are below.
correct_responses = ["filler_because_index_starts_at_zero","variable","list","nested","concatenation","mutation","append","comment","hashtag","function","parameters","none","list"]
blanks = ["filler_because_index_starts_at_zero", "___1___", "___2___", "___3___","___4___", "___5___","___6___", "___7___","___8___", "___9___","___10___", "___11___","___12___" ]


### cd nanodegree/intro_programming/project_2



def take_quiz_easy(n):                 ### the coing for level 1 easy begins
    new_paragraph = paragraph_easy     ### identifies what paragraph to use for quiz easy
    while n < 5:                       ### creates loop, so user has to go through questions 1 through 4
        response_to_question = raw_input("What should go in blank number " + str(n) + "?")
        if response_to_question == correct_responses[n]:      ### checks to make sure user response is same as correct answer
            print "Correct Answer!"
            new_paragraph = new_paragraph.replace(blanks[n], correct_responses[n]) ### replaces blanks with the correct response and replaces old paragraph with new paragraph
            print new_paragraph
            n = n + 1                  ### advances to next blank, next correct answer
        else:
            print "Incorrect answer"

    print "Congratulations! You have completed level easy! Go get a sugary snack as a reward, you genius you!"


def take_quiz_medium(n):              ### the coing for level 2 medium begins
    new_paragraph = paragraph_medium  ### identifies what paragraph to use for quiz medium
    while n < 9:                      ### creates loop, so user has to go through questions 5 through 8
        response_to_question = raw_input("What should go in blank number " + str(n) + "?")
        if response_to_question == correct_responses[n]:        ### checks to make sure user response is same as correct answer
            print "Correct Answer!"
            new_paragraph = new_paragraph.replace(blanks[n], correct_responses[n])    ### replaces blanks with the correct response and replaces old paragraph with new paragraph
            print new_paragraph
            n = n + 1                 ### advances to next blank, next correct answer
        else:
            print "Incorrect answer."

    print "Congratulations! You have completed level medium! Go get a beer as a reward!"


def take_quiz_hard(n):               ### the coing for level 3 hard begins
    new_paragraph = paragraph_hard   ### identifies what paragraph to use for quiz hard
    while n < 13:                    ### creates loop, so user has to go through questions 9 to 12
        response_to_question = raw_input("What should go in blank number " + str(n) + "?")
        if response_to_question == correct_responses[n]:         ### checks to make sure user response is same as correct answer
            print "Correct Answer!"
            new_paragraph = new_paragraph.replace(blanks[n], correct_responses[n])     ### replaces blanks with the correct response and replaces old paragraph with new paragraph
            print new_paragraph
            n = n + 1                 ### advances to next blank, next correct answer
        else:
            print "Incorrect answer."

    print "Congratulations! You have completed the most difficult level!"


level = raw_input('Would you like difficulty level easy, medium, or hard?')
def select_difficulty(level):
    if level == "easy" or level == "Easy":       ### directs to easy level
        print paragraph_easy
        n = 1
        take_quiz_easy(n)
    if level == "medium" or level == "Medium":   ### directs to medium level
        print paragraph_medium
        n = 5
        print "So you think you're smart enough to skip a level? Straight to question " + str(n) + " for you."
        take_quiz_medium(n)
    if level == "hard" or level == "Hard":       ### directs to hard level
        print paragraph_hard
        n = 9
        print "Oh you wanna start with the hard level? Bring it on with question " + str(n) + ". Remember, you asked for it."
        take_quiz_hard(n)

print select_difficulty(level)
