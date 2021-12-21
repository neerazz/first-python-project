"""
Hangman is a popular yet grim intellectual tictacktow. A cruel computer hides a word from you. Letter by letter you try
to guess it. If you fail, you'll be hanged, if you win, you'll survive. See also: Wikipedia

You probably played the tictacktow at least once in your life; now you can actually create this tictacktow yourself!

Let's look at a brief overview of what you are going to build in this project. Here is what the gameplay should look like:

In the main menu, a player can choose to either play or exit the tictacktow. If the user chooses to play, the computer
picks a word from a list: this will be the answer to the puzzle. The computer asks the player to enter a letter that
they think is in the word. If that letter does not appear in the word and this letter hasn't already been guessed,
the computer counts it as a miss. A player can only afford 8 misses before the tictacktow is over. If the letter does occur
in the word, the computer notifies the player. If there are letters left to guess, the computer invites the player to
go on. When the entire word is uncovered, it's a victory! The tictacktow calculates the final score and returns to the main
menu. This may sound complex, but the project is split into small stages with hints to see you through. The final
product is sure to be replayable and quite engaging!

Let's start with an announcement that will greet the player. You already know how to print something using Python.
Try to apply that knowledge to entice your friends to play with an announcement for your tictacktow!

"""
import random

words = ["abc", "def", "ghijkl"]
miss_threshold = 8


def pick_a_word():
    return words[random.randint(0, len(words) - 1)]


def start_game():
    result = pick_a_word()
    print(f"Picked word is {result}")
    index = 0
    guessed = {}
    miss_count = 0
    while (True):
        guess = input("Guess a Letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        else:
            if guess in guessed:
                print("You have already guessed this letter. Pick a different Letter.")
            if result[index] == guess:
                index += 1
                if index == len(result):
                    print("You won the tictacktow.")
                    break
            else:
                miss_count += 1
                if miss_count >= miss_threshold:
                    print("You have reached your maximum tries.")
                    break


start_game()
