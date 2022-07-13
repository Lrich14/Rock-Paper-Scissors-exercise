# Overall I found help from a guide via the RealPython [website](https://realpython.com/python-rock-paper-scissors/) which further aided in 
# my understanding of the exercise and functions that I need to use for the exercise.

# this is the "game.py" file
import random 

# I'm introducing the game to the player and getting them excited to play.
"Hello. Welcome Player One. Let's play Rock, Paper, Scissors, Shoot!"
print("Hello. Welcome Player One. Let's play Rock, Paper, Scissors, Shoot!")


# processed user inputs, validated user inputs, and set up the randomized computer selections for the game to run properly.
# I need to make a list of all the options so that the user action returns the accurate result
# Found the "while True" via the Real Python link above which helped me to understand and format the below code
while True:
    user_action = input("Enter a choice (Rock, Paper, Scissors): ")
    user_action = user_action.lower()
 
    computer_choices = ["rock", "paper", "scissors"]
    if user_action not in computer_choices:
        print("Sorry I don't understand that entry.  Please try again")
        exit() # quit()
    computer_action = random.choice(computer_choices)
    print(f"You chose {user_action}, \ncomputer chose {computer_action}")
   
# Setting up all the various outcomes of the game between player and computer using if, elif, and else statements
# Then determining the winner based on the player's and computer's actions
    if user_action == computer_action:
        print(f"Whoa, you both selected {user_action}. Tie game!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("paper beats rock! You lost to the computer, uh oh!")
        else:
            print("rock beats scissors! You win!! WOOHOO!")
    elif user_action == "paper":
        if computer_action == "scissors":
            print("scissors beats paper! You lost to the computer, uh oh!")
        else:
            print("paper beats rock! You win!! WOOHOO!")
    elif user_action == "scissors":
        if computer_action == "rock":
            print("rock beats scissors! You lost to the computer, uh oh!")
        else:
            print("scissors beats paper! You win! WOOHOO!")

# Asking the player if they want to play again or end the game.
    play_again = input("Would you like to try again? (y/n): ")
    if play_again != "y":
        print("Goodbye. Thanks for playing!")
        break
