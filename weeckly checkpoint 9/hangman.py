
# This is a pseudocode
# A pseudocode is a file with lines (of code or text) that will help us have an idea of what our main code will do.

# We need to make a Hangman game.

# Create a TXT file with all of the words.
# Define the main function.
# Define a new function to start the game, call it "start_game", with one parameter.
# Use with to open the TXT file.
# Use a randomizer to get a random word.
# Make the word into a list of letters. The word is already a list.
# Welcome the user into the game
# Use list variables and methoods for the selected word.
# use a variable for the lifes of the user.
# Use a while loop to keep asking the user fot the letters.
# Use a for loop to give the user how many letters the word has.
# Use inputs for the user to guess the letter.
# Use ifs and elifs to give the user the correct letters.
# Use ifs, elifs, and update the variable of the user's life.
# Make another variable for the misses that will update as the user misses.
# Make the while loop break when the user's lifes = 0.
# If the user guesses the word, ask them if they want to play again.
# Call the "start_game" function and add the TXT file in it.
# Call the main function (thank you).



import random
def main():
    start_game("words.txt")


def start_game(file):
    attempts = 10
    with open(file) as f:
        word_bank = f.read().splitlines()
    word = random.choice(word_bank)
    hint = ["_"] * len(word)
    incorrect_letters = []
    while attempts > 0:
       print("Current word:", " ".join(hint))

       while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
                break
            else:
                print("Invalid guess, Try again.")


       if guess in word and guess not in hint:
           for i in range(len(word)):
               if word[i] == guess:
                   hint[i] = guess
           print("Great guess!")
       elif guess in hint:
        attempts -= 1
        print("You already guessed that letter! Attempts left:", str(attempts))

       else:
        attempts -= 1
        print("Wrong guess! Attempts left:", str(attempts))
        if guess not in incorrect_letters:
            incorrect_letters.append(guess)
        print(f"Incorrect letters: {" ".join(incorrect_letters)}")

       if "_" not in hint:
        print("Congratulations! 🥳 You guessed the word:", word)
        break

    if attempts == 0 and "_" in hint:
        print("No attempts left 💀 The word was:", word)







if __name__ == "__main__":
    main()
