import random
import math 

game_running = True
guessed_correctly = False
lives = 10
guesses = 0
times_played = 0
correct_guesses = 0
incorrect_guesses = 0 



print("||  ||")

def greeting():
    print("|||||||||||||||||||||||||||||||| \n||| Welcome To Number Guesser ||| \n|||||||||||||||||||||||||||||||| ")

def select_ranges():
    lower_range = int(input("Enter the lowest possible number for this round: "))
    upper_range = int(input("Enter the highest possible number for this round: "))
    return lower_range, upper_range

def generate_random_number(lower, upper):
    number_to_guess = random(range(lower, upper))
    print(f"|| A random nubber bwtween {lower} and {upper} has been selected ||")
    return number_to_guess

def guess_number():
    user_guess = int(input("What is your guess? "))
    return user_guess

def validate_guess(guess, actual):
    if guess == actual:
        global guessed_correctly
        guessed_correctly = True
        print("|| You Have Guessed The Correct Answer, Congrats!!! ||")
    else:
        guessed_correctly = False
        print("|| Wrong Quess, Try Again!!! ||")

def play_more():
    while True:
        keep_playing = input("Do you want to play again? 'Y' or 'Yes' to continue,'Q' to Quit").upper()
        if keep_playing == "Y" or "YES":
            global game_running
            game_running = True
            break
        elif keep_playing == "Q" or "Quit":
            game_running = False
            break
        else:
            print("select a valid option ")
        


def game():
    greeting()
    global guessed_correctly
    while game_running:
        lower_limit, upper_limit = select_ranges()
        generated_number = generate_random_number(lower_limit, upper_limit)
        guessed_number = guess_number()
        validate_guess(guessed_number, generated_number)
    if guessed_correctly:
        play_more()
    else:
        pass



