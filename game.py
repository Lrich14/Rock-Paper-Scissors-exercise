# Overall I found help from a guide via the RealPython [website](https://realpython.com/python-rock-paper-scissors/) which further aided in 
# my understanding of the exercise and functions that I need to use for the exercise.

# this is the "game.py" file
import random 

"Hello. Welcome Player One. Let's play Rock, Paper, Scissors, Shoot!"
print("Hello. Welcome Player One. Let's play Rock, Paper, Scissors, Shoot!")

 

# printuser_action

# processed user inputs, validated user inputs, and set up the randomized computer selections
while True:
    user_action = input("Enter a choice (Rock, Paper, Scissors): ")
    user_action = ("Rock", "Paper", "Scissors", "ROCK", "PAPER", "SCISSORS", "rock", "paper", "scissors")
    computer_choices = ("Rock", "Paper", "Scissors", "ROCK", "PAPER", "SCISSORS", "rock", "paper", "scissors")
    computer_action = random.choice(computer_choices)
    print(f"You chose {user_action}, computer chose {computer_action}")
   
   # Setting up all the various outcomes of the game between player and computer using if, elif, and else statements
    if user_action == computer_action:
        print(f"Whoa, you both selected {user_action}. Tie game!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("paper beats rock! You lose, uh oh!")
        else:
            print("rock beats scissors! You win!! WOOHOO!")
    elif user_action == "paper":
        if computer_action == "scissors":
            print("scissors beats paper! You lose, uh oh!")
        else:
            print("paper beats rock! You win!! WOOHOO!")
    elif user_action == "scissors":
        if computer_action == "rock":
            print("rock beats scissors! You lose, uh oh!")
        else:
            print("scissors beats paper! You win! WOOHOO!")
    else:
        print("Sorry I don't understand that entry.  Please try again")


    play_again = input("Would you like to play again? (y/n): ")
    if play_again != "y":
        print("Goodbye. Thanks for playing!")
        break
