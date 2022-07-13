# Rock-Paper-Scissors-exercise

## Setup Instructions
First setup a repository in Github named "Rock-Paper-Scissors-exercise" and clone that repository onto your computer Desktop location using Github Desktop

Next, navigate to the clone repository on the command line using the below code:
```
cd ~/Desktop/rock-paper-scissors-exercise
```

Next, use text editor in this case VS Code to create a file in the repository called "game.py", and place the below inside:

'# this is the "game.py" file
"Rock, Paper, Scissors, Shoot!"
print("Rock, Paper, Scissors, Shoot!")'

After completing these steps, make sure to save your files.

### Environment Setup

First, create and activate the **project-specific** Anaconda virtual environment using the below lines of code:
```
conda create -n my-game-env python=3.8
```

When prompted enter: 
```
conda activate my-game-env
```

After these steps are completed, enter the below in the virtual environment on the command-line:
```
python game.py
```
If you see the following message: "Hello. Welcome Player One. Let's play Rock, Paper, Scissors, Shoot!" you are ready to play!

### Helpful Tools/Sites

The following websites/links provide helpful guides and explanations on how to run similar style rock-paper-scissors games in python which can aid in creating this game as well:

*[Real Python](https://realpython.com/python-rock-paper-scissors/)
*[Hello World Program](https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/)


## Usage

### Inputs and Determining Winners

It will be important to have an understanding of the following functions, statements, modules, and datatypes in order to create this game:

1. input function
2. if/elif/else 
3. random module
4. exit keyword
5. choice function
6. list datatype


An example of the expected desire output after one game should look something like this:
>Hello. Welcome Player One. Let's play Rock, Paper, Scissors, Shoot!
>
>Enter a choice (Rock, Paper, Scissors): 
>
>You chose paper, 
>
>computer chose scissors
>
>scissors beats paper! You lost to the computer, uh oh!
>
>Would you like to try again? (y/n):