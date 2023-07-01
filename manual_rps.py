import random

game_options = ['rock','paper','scissors']

def get_computer_choice():
    comp_choice = random.choice(game_options)
    return comp_choice

def get_user_choice():
    user_choice = input("Select between rock, paper and scissors")
    return user_choice

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
        print("You won!.")
    return winner

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice,user_choice)

play()