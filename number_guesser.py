import random
 
# greeting graphic
def greeting():
    print("||||||||||||||||||||||||||||||||| \n||| Welcome To Number Guesser ||| \n|||||||||||||||||||||||||||||||||")

# range of the number to be guessed is selected
def select_ranges():
    return int(input("Enter the lowest possible number for this round: ")), int(input("Enter the highest possible number for this round: "))

# a random number is generated, user must guess this number
def generate_random_number(lower, upper):
    print(f"|| A random number bewtween {lower} and {upper} has been selected ||")
    return random.randint(lower, upper)

# user guesses number
def guess_number():
    return int(input("What is your guess? "))

# checks if user guess matches actual number
def validate_guess(guess, actual):
    if guess == actual:
        print(f"|| You Have Guessed The Correct Answer, Congrats!!! ||")
        return True
    else:
        print("|| Wrong Quess, Try Again!!! ||")
        if guess > actual:
            print("|| Your guess was too large ||")
        else:
            print("|| Your guess was  too small ||")
        return False
        
# players chooses if they want to continue or quit
def play_more():
    while True:       
        keep_playing = input("Do you want to play again? 'Y' or 'Yes' to continue,'Q' to Quit ").upper()
        if keep_playing in ["Y", "YES"]:
            return True
        elif keep_playing in ["Q", "QUIT"]:
            return False
        else:
            print("select a valid option ")
        
def game():
    greeting()
    game_running = True
    while game_running:
        lower_limit, upper_limit = select_ranges()
        generated_number = generate_random_number(lower_limit, upper_limit)
        guessed_correctly = False
        
        while not guessed_correctly:
            guessed_number = guess_number()
            guessed_correctly =  validate_guess(guessed_number, generated_number)
        
        game_running = play_more()
        
        
if __name__ == "__main__":
    game()


