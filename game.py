# this is the "game.py" file
"Rock, Paper, Scissors, Shoot!"
print("Rock, Paper, Scissors, Shoot!")

# processing user inputs
x = input("Enter a choice (Rock, Paper, Scissors): ")
print(x)
print(type(x))

# validate user inputs
x = ("Rock, Paper, Scissors")
if x == ("Rock", "Paper", "Scissors"):
    print("Yes")
else:
    print("Sorry I don't understand.  Please try again")