from GuessingGame import Guessing_Game
from HangmanGame import Hangman_Game_While

print("****************************")
print("****Choose your game!******")
print("****************************")

print("(1) Hangman Game (2) Guessing Game")

game = int(input("What's the game? "))

if(game == 1):
    print("Hangman Game")
    Hangman_Game_While.play()
elif (game == 2):
    print("Guessing Game")
    Guessing_Game.play()