## Lets create a predefined list inside a function
import random

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
            if turns == 9:
                print("9 turns left")
                print("----------")
            if turns == 8:
                print("8 turns left")
                print("---------")
                print("    O   ")
            if turns == 7:
                print("7 turns left")
                print("---------")
                print("    O   ")
                print("    |   ")
            if turns == 6:
                print("6 turns left")
                print("---------")
                print("    O   ")
                print("    |   ")
                print("   /   ")
            if turns == 5:
                print("5 turns left")
                print("---------")
                print("    O   ")
                print("    |   ")
                print("   / \  ")
            if turns == 4:
                print("4 turns left")
                print("---------")
                print("  \ O   ")
                print("    |   ")
                print("   / \  ")
            if turns == 3:
                print("3 turns left")
                print("---------")
                print("  \ O /  ")
                print("    |   ")
                print("   / \  ")
            if turns == 2:
                print("2 turns left")
                print("---------")
                print("  \ O /|  ")
                print("    |   ")
                print("   / \  ")
            if turns == 1:
                print("1 turns left")
                print("---------")
                print("  \ O _|/  ")
                print("    |   ")
                print("   / \  ")
            if turns == 0:
                print("You Loose")
                print("---------")
                print("    O _|  ")
                print("   /|\   ")
                print("   / \  ")
                break




name = input("Enter Your Name: \n")
print("Welcome",name, ",Let's Start The Game")
print("-------------------------------")
print("So the game is to guess the word within 10 tries")
hangman()