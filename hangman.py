## Lets create a predefined list inside a function
from random import random
from wsgiref.util import guess_scheme

def hangman():
    ## random.choice will select random word from
    word = random.choice(["Hello", "Avengers", "Superman", "Bedsheet", "Laptop", "Mouse", "Jeans", "Jennifer", "Keyboard", "Editor"])
    validLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    turns = 10
    guessMade = ""

    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessMade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break
        print("Guess the word", main)
        guess = input()

    
    # Checking that the user entered a valid letter
    if guess in validLetters:
        guessMade = guessMade + guess
    else:
        print("Please enter a valid letter.")
        guess = input()
    if guess not in word:
        turns = turns - 1

name = input("Enter Your Name: \n")
print("Welcome",name, ",Let's Start The Game")
print("-------------------------------")
print("So the game is to guess the word within 10 tries")
hangman()