# Overall I found help from a guide via the RealPython [website](https://realpython.com/python-rock-paper-scissors/) which further aided in 
# my understanding of the exercise and functions that I need to use for the exercise.

# this is the "game.py" file
import random 

"Rock, Paper, Scissors, Shoot!"
print("Rock, Paper, Scissors, Shoot!")

# processing user inputs
user_action = input("Enter a choice (Rock, Paper, Scissors): ")
print(user_action)

# validated user inputs and set up the randomized computer selections
while True:
    user_action = ("Rock, Paper, Scissors, ROCK, PAPER, SCISSORS, rock, paper, scissors")
if user_action == ("Rock", "Paper", "Scissors", "ROCK", "PAPER", "SCISSORS", "rock", "paper", "scissors"):
    print(user_action)
else:
    print("Sorry I don't understand.  Please try again")

# Setting up the randomized computer selection. 

    computer_choices = ("Rock", "Paper", "Scissors", "ROCK", "PAPER", "SCISSORS", "rock", "paper", "scissors")
    computer_action = random.choice(computer_choices)


    print(f"You chose {user_action}, computer chose {computer_action}")
