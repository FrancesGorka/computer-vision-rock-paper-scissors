import random
import numpy as np
from RPS_Template import camera_prediction

game_options = ['rock','paper','scissors']

def get_prediction():
    prediction = camera_prediction()
    max_index = np.argmax(prediction)
    user_choice_pred = game_options[max_index]
    print(f"You chose {user_choice_pred}")
    return user_choice_pred

def get_computer_choice():
    comp_choice = random.choice(game_options)
    return comp_choice

def get_winner(computer_choice,user_choice):
    if computer_choice == user_choice:
        #user_choice = get_user_choice()
        #computer_choice = get_computer_choice()
        #get_winner(user_choice,computer_choice)
        print("It's a tie!")
    if computer_choice == 'rock' and user_choice == 'scissors':
        winner = 'computer'
        print("You lost.")
    elif computer_choice == 'paper' and user_choice == 'rock':
        winner = 'computer'
        print("You lost.")
    elif computer_choice == 'scissors' and user_choice == 'paper':
        winner = 'computer'
        print("You lost.")
    else:
        winner = 'user'
        print("You win this round!. ")
    return winner

def play():
    computer_choice = get_computer_choice()
    user_choice = get_prediction()
    winner = get_winner(computer_choice,user_choice)
    return winner

def best_of_three():
    user_wins = 0
    comp_wins = 0
    while user_wins != 3 and comp_wins != 3:
        winner = play()
        if winner == 'user':
            user_wins += 1
        elif winner == 'computer':
            comp_wins += 1
    if user_wins == 3:
        print("Game over. You win! ")
    if comp_wins == 3:
        print("Game over. Computer wins! ")

best_of_three()