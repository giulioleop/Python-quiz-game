# Giulio Leopaldi - 5.11 MULTI-PLAYER QUIZ GAME

import random
import string

# Creating a class to handle the questions of the quiz game, with 2 attributes: the quiz and the answer
class Question():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
        
question = [
    "\nWhich country is Parmesan cheese originally from?\n\n", 
    "\nWhat type of creature lives in an apiary?\n\n",
    "\nWhat colour flag is awarded to a beach that meets high standards for cleanliness, safety and water quality?\n\n",
    "\nAt what time of the year do Pantomimes traditionally take place?\n\n",
    "\nGiven a number x: if you add 9 to it and divide it by 4, the result is 5. How much is x?\n\n",
    "\nWhich is the largest island in the world?\n\n",
    "\nCO2 is the chemical formula for what?\n\n",
    "\nWhat's the name of the river that runs through London?\n\n",
    "\nWhat does IPA stand for?\n\n",
    "\nWhat star sign would someone born on November 16th be?\n\n"   
]

questions = [
    Question (question[0], 'Italy'), 
    Question (question[1], 'Bee'),
    Question (question[2], 'Blue'),
    Question (question[3], 'Christmas'),
    Question (question[4], '11'),
    Question (question[5], 'Greenland'),
    Question (question[6], 'Carbon Dioxide'),
    Question (question[7], 'Thames'),
    Question (question[8], 'Indian Pale Ale'),
    Question (question[9], 'Scorpio'),
]


# Extra feature #1: Choosing the number of questions the user wants in the quiz game (1 to 10)
while True:
    try:
        number_of_questions = int(input("How many questions you'd like in your quiz? Enter a number between 1 and 10: "))
        while number_of_questions <1 or number_of_questions >10:
            number_of_questions = int(input("Invalid input. Enter a number between 1 and 10:"))
        break
    except ValueError:
        print ("Invalid input. Enter a number between 1 and 10: ")
        continue

# Function to run the quiz
def run_quiz (questions):
    # creting a dictionary to store player name as key and player's score as value
    players = {}
    
    new_player = 'yes'
    while new_player.lower().strip() == 'yes':
        player_name = input("Enter your name: ")
        while player_name.strip() == "" or player_name in players:
            player_name = input("Invalid input. Enter your name: ")
        score = 0
        # Extra feature#2: Questions asked in random order
        randomsample_of_Questions = random.sample(questions, number_of_questions)
        
        # Creating other 2 dictionaries to keep track of correct/incorrect answers for each user.
        correct_answer ={}
        wrong_answer ={}

        for question in randomsample_of_Questions:
            answer = input(question.question)
            while answer.strip() == "":
                print("Invalid input")
                answer = input(question.question)
            # formatting the text of the answer by eliminating upper/lower case sensitivity and blank spaces and updating score.
            if answer.lower().strip() == question.answer.lower().strip():
                correct_answer [question.question] = answer
                score+=1
            else:
                wrong_answer [question.question] = [answer, question.answer]
        players[player_name] = score
        
        #printing user's score
        user_score_percentage = int((score/number_of_questions)*100)
        print ("\n>>> ", str(player_name)+ ' guessed '+ str(score) + ' out of '+ str(number_of_questions),
               'answers, which equals to', str(user_score_percentage)+"% of correct guesses.\n")        
        # Extra feature #3: The user is shown which questions they got correct and which they got incorrect
        if correct_answer != {}:
            print ("\n", str(player_name) +  "'s correct answers are:")
            for k,v in correct_answer.items():
                print (k, v)
        if wrong_answer !={}:   
            print("\n", str(player_name) +"'s wrong answers are:")
            for k,v in wrong_answer.items():
                print (k, "Your answer:", v[0], "\tThe correct answer is:", v[1])
        
        print ("==============================================================")
        
        # Asking if anybody else wants to take the quiz
        new_player = input('Is there another player? Enter yes or no: ')
        while new_player.lower().strip() != 'yes' and new_player.lower().strip() != 'no':
            new_player = input('Invalid input. Is there another player? Enter yes or no: ')
    else:
        return players
   
player_scores = run_quiz (questions)

# Determining the highest score
highest_score = max(player_scores.values())
percentage_score = int(((highest_score/number_of_questions)*100))

all_users_av_score_percentage = int((sum(player_scores.values())*100)/(len(player_scores.keys())*(number_of_questions)))

#printing the final results
print("\nFINAL RESULTS\nPlayer\t\t\tScore")
for item in player_scores:
    print("{}\t\t\t{}".format(item, player_scores[item]))

print("\nAnd the winner is:\n")
# the winner is stored in the dictionary that has the value matching the highest score
for key,value in player_scores.items():
    if value == highest_score:
        print (key)
print ("\nwho scored", str(highest_score)+ " out of "+ str(number_of_questions),
       "points, which equals to a success rate of "+ str(percentage_score) +"%.")
print("The average score of all players is:", str(all_users_av_score_percentage)+"% of correct guesses.")
