import random
import math 

game_running = True
game_restarted = True
guessed_correctly = False
guesses = 0
times_played = 0
correct_guesses = 0
incorrect_guesses = 0 



print("||  ||")

def greeting():
    print("||||||||||||||||||||||||||||||||| \n||| Welcome To Number Guesser ||| \n|||||||||||||||| |||||||||||||||||")

def select_ranges():
    lower_range = int(input("Enter the lowest possible number for this round: "))
    upper_range = int(input("Enter the highest possible number for this round: "))
    return lower_range, upper_range

def generate_random_number(lower, upper):
    number_to_guess = random.randint(lower, upper)
    print(f"|| A random number bwtween {lower} and {upper} has been selected ||")
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
        if keep_playing == "Y" or keep_playing == "YES":
            global game_running
            game_running = True
            break
        elif keep_playing == "Q" or keep_playing == "Quit":
            game_running = False
            break
        else:
            print("select a valid option ")
        
'''
whle game runnig
    select numer
    
    if guess wrong:
       guess again
    if guess correct:
       play again?
'''

def game():
    greeting()
    global guessed_correctly
    global game_restarted
    while game_running:
        print("_while loop restarted_")
        if game_restarted:
             print("If game restarted")
             lower_limit, upper_limit = select_ranges()
             generated_number = generate_random_number(lower_limit, upper_limit)
             game_restarted = False
             guessed_correctly = False

        if guessed_correctly == False:
            print("**guessed_correctly == False**")
            guessed_number = guess_number()
            validate_guess(guessed_number, generated_number)
        elif guessed_correctly:
            print("**if guessed_correctly**")
            play_more()
            game_restarted = True
        


 
if __name__ == "__main__":
    game()


