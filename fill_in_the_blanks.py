### IPND Stage 2 Final Project

### The blanks that will appear in the paragraph before the user gives the correct answer. Is needed so later on with line 68 the program knows what it is replacing.
blanks=["___1___", "___2___", "___3___", "___4___"]



### This is paragraph_1. It is for level easy. It it used with the correct_respones list and the blanks list. More on this later when it is actively used in a function.
paragraph_easy= "In Python a value can be stored with a ___1___. A ___1___ can also be used to store a ___2___. A ___2___ is structured data and is denoted with square brackets. Much like cute little Russian dolls, one ___2___ can be inside another ___2___ this is called ___3___ ___2___s. Denoted with a plus sign, ___4___ joins to two strings together."

### This is paragraph 2. It is for level medium. It it used with the correct_respones list and the blanks list.
paragraph_medium = "Lists support ___1___, while strings do not, this means the programmer can change the value of a list after its created. You can an element to the end of a list with ___2___. It is good to start all functions and all classes with a ___3___ which can be recognized by the ___4___ symbol."

### This is paragraph 3. It is for level hard. It it used with the correct_respones list and the blanks list.
paragraph_hard = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions."


### These are the correct answers they get compared to what the user inputs later. More on that later when they are actively used in a function.
correct_responses_easy=["variable","list","nested","concatenation"]
correct_responses_medium=["mutation","append","comment","hashtag"]
correct_responses_hard=["function","parameters","none","list"]



level=raw_input('Would you like difficulty level easy, medium, or hard?')     ### sets up the question of what level would the user like to start on and takes the user response as input
def select_difficulty(level):   ### the function that returns the level the user selected

    if level=="easy" or level=="Easy":
        return paragraph_easy

    if level=="medium" or level=="Medium":
        return paragraph_medium

    if level=="hard" or level=="Hard":
        return paragraph_hard


print select_difficulty(level)     ###prints question so the user can see it


def select_answers(level):        ### sets up function that corresponds user selected level to the correct answers for that level
    if select_difficulty(level)==paragraph_easy:
        return correct_responses_easy
    if select_difficulty(level)==paragraph_medium:
        return correct_responses_medium
    if select_difficulty(level)==paragraph_hard:
        return correct_responses_hard


def check_answer(replies, answers, correct_responses):  #### sets up function that sees if user response is same as correct answer
     if replies==answers[correct_responses]:
         return "Correct"
     return "Incorrect"


def fill_in_the_blanks():   ### this function is the actual taking the quiz part and has many parts, so lets break it down
    quiz=select_difficulty(level)    ### makes sure the quiz actually taken is the one corresponding to the difficulty level the user asked for
    answers=select_answers(level)    ### makes sure we're working with the answers for the correct difficulty level of the quiz
    blanks_index=0                   ### defines blanks_index, so python does not return undefined error
    correct_responses=0              ### defines correct_respones, so python does not return undefined error
    while blanks_index<len(blanks):      ### creates while loop so quiz will end when there's no more blanks to answer
        replies=raw_input("Please fill in the correct answer for " + blanks[blanks_index])   ### set up question for asking user to fill in blank and stores as input
        while check_answer(replies, answers, correct_responses)=="Incorrect":  ### if the user reply is not the same as the correct response, with the help of function check_answer will return incorrect
            replies=raw_input("You stupid eejit, try again. Do you think you can get the correct answer for question " + blanks[blanks_index] + " now?")     ### informs user they are wrong and gives second chance to answer by printing the string enclosed
        if check_answer(replies, answers, correct_responses)=="Correct":   ### if the users' reply is the same as the correct answer it will return correct
            print "Good job, your answer is correct!"                      ### prints the user is correct message
            quiz=quiz.replace(blanks[blanks_index], replies)               ### replaces the blank in the paragraph with the correct response and overrides the old paragraph, so new paragraph will print
            print quiz                                                     ### prints new paragraph for user to see
            blanks_index = blanks_index + 1                                ### advances the blank_index to next blank
            correct_responses = correct_responses + 1                      ### advances the correct_responses index to the next correct answer

    print "Congratulations! It's over! Go get a drunk, you genius you!"    ### prints congratulations you survived message

print fill_in_the_blanks()                    ### prints the fill in the blanks function, which user sees first input request from line 63
