from random import randint #comand randint
player_name = input('Write your name: ')
player_surname = input('Write your surname: ')
points = 0 # points which you will get
false_ans = 0 # Your false answers
skip_ans = 0 # Your skip questions
def random_question(player_name, player_surname,
                    points, false_ans, skip_ans): # Main function

    def true_false(points, questions, quest_list, 
                   true_ans, random_index, false_ans, skip_ans):
            if answer == true_ans:
                print('True!!! Next question, please!') #If answer is True
                points += 25
                questions.pop(f'{quest_list[random_index]}')
                quest_list.pop(random_index)
                ans_list.pop(random_index)
            
            elif answer == '???':                       # If you write '???', you skip question
                skip_ans += 1
              
            else:
                print('Not right! Next question, please!') #If answer is False
                points -= 25
                questions.pop(f'{quest_list[random_index]}')
                quest_list.pop(random_index)
                ans_list.pop(random_index)
                false_ans += 1

            return points, false_ans, questions, quest_list, skip_ans # Saving data
        
    def result_file(player_name, player_surname, points): # Making file with your result
            with open('Your result', 'a') as file:
                file.write(f'Name: {player_name}. Surname: {player_surname}. Points: {points}\n')
                file.close()

    questions = {'How many stars on USA flag?' : '50', 
                    'What year was born Sakharov?' : '1921',
                    'Near which mountain-volcano was the gem tanzanite found for the first time?' : 'Kilimanjaro',
                    'What headdress was worn during the ball by Tatyana Larina, the heroine of the novel "Eugene Onegin"?' : 'Crimson beret',
                    "What product in different countries is called daddy's beard and grandmother's hair?" : 'Cotton candy',
                    'What is the name of the red rag in the hands of a matador?' : 'Muleta',
                    'What astronomical phenomenon can the inhabitants of the Earth observe every 75-76 years?' : "Appearance of Halley's Comet",
                    'How many carats is pure gold?' : '24'} # questions and answers
    
    quest_list = list(questions.keys()) #questions list
    ans_list = list(questions.values()) #answer list
    random_index = randint(0, len(questions) - 1) #random index

    while false_ans != 3 or len(questions) != 0:
        if random_index == 0:
            break
        answer = input(f"You can skip question with '???'. {quest_list[random_index]}: ").strip().lower() #your answer
        true_ans = ans_list[random_index].lower() # find true answer            
        result = true_false(points, questions, quest_list, 
                            true_ans, random_index, false_ans, skip_ans)
        random_index -= 1

        points = result[0] 
        false_ans = result[1]
        questions = result[2]
        quest_list = result[3]

    print('Game over.')
    print("Your result in the file 'Your result.txt'.")
    result_file(player_name, player_surname, points) # Game stop
    return skip_ans

while True:
    result_delet = input("Do you want to delet your result from file 'Your result.txt'? Y/N: ")
    ask = input("Start? Y/N: ") # Question: "Do you want to continue game?"
    if result_delet == 'Y':     # Cleaning file with result if result_delet == 'Y'
        with open('Your result', 'w') as file:
            file.write('New Result: \n')
        random_question(player_name, player_surname,
                        points, false_ans, skip_ans)
    if ask == 'Y':                                    # You continue game
        skip = random_question(player_name, player_surname,
                            points, false_ans, skip_ans)
        if skip == 3:
            break
    else:  # You don't continue game
        break