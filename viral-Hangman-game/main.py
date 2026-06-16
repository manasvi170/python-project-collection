import random
import hangman_words
import hangman_art

lives = 6

# Importing the logo from hangman_art.py
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f'****************************{lives}/6 LIVES LEFT****************************')
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If the letter chosen by user is not in the chosen_word, let the user know that it's not in the word.
    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess} ,that`s not in the word you lose a life !\n {lives}/6 left')

        if lives == 0:
            game_over = True

            #Let the user know the correct word they were trying to guess.
            print(f'The CORRECT WORD was {chosen_word}!\n***********************YOU LOSE**********************')

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Printing the ASCII Art of hangman stages
    print(hangman_art.stages[lives])
