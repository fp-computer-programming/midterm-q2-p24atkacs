"""
Create a Python file named Midterm-Q2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

"""

#author: Andrew Tkacs

from random import seed, randint

# Function to choose a random word from a predefined list
def choose_word():
    wordlist = ["Python", "Lighthouse", "Jazz", "Quasar", "Mysterious", "Zephyr", "Giraffe", "Champion", "Galaxy", "Whisper", "Exquisite"]
    return wordlist[randint(0, 10)]

# Main Hangman game function
def hangman(word):
    word = word.lower()
    word_length = len(word)
    wrong_attempts = 0
    guessed_word = "-" * word_length
    guessed_letters = set()

    print("Welcome to Hangman!")

    # Game loop
    while guessed_word != word and wrong_attempts < 7:
        print(f"\nIncorrect attempts left: {7 - wrong_attempts}")
        print("Guessed word:", " ".join(guessed_word))

        # Get user input for a letter guess
        guess = input("What's your guess? ").lower()

        # Validate the input
        if guess.isalpha() and len(guess) == 1:
            # Check if the letter has already been guessed
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
                continue

            guessed_letters.add(guess)

            # Update the guessed word based on the correct letter guesses
            if guess in word:
                for i in range(word_length):
                    if word[i] == guess:
                        guessed_word = guessed_word[:i] + word[i] + guessed_word[i + 1:]
            else:
                wrong_attempts += 1

    # Display the game result
    if guessed_word == word:
        print(f"\nCongratulations! You guessed the word: {word.capitalize()}!")
    else:
        print("\nSorry, you ran out of attempts. The word was:", word.capitalize())

# Entry point of the program
if __name__ == "__main__":
    # Start the game
    start = input("Would you like to play Hangman? (y/n) ")
    if start.lower() == "y":
        seed_input = input("Pick a number 1-10 for randomization: ")
        seed_num = int(seed_input)
        while not 1 <= seed_num <= 10:
            seed_input = input("Pick a number 1-10: ")
            seed_num = int(seed_input)
        seed(seed_num)

        # Choose a word and start the game
        chosen_word = choose_word()
        hangman(chosen_word)

        # Ask if the player wants to play again
        play_again = input("Would you like to play again? (y/n) ")
        while play_again.lower() == "y":
            chosen_word = choose_word()
            hangman(chosen_word)
            play_again = input("Would you like to play again? (y/n) ")
    else:
        print("Goodbye!")


