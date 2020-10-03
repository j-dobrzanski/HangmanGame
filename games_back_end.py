from getting_random_word import random_word


def hangman_main():
    secret_word = random_word().strip()

    number_of_letters = len(secret_word)
    i = 0
    secret_word_to_guess = []
    while i < number_of_letters:
        secret_word_to_guess.append("_")
        i += 1
    guessing_word_label = Label(root, )

    number_of_guesses = 0
    remaining_chances = 10
    while True:
        number_of_guesses += 1
        guess = str(input("Guess a letter or a whole word: "))
        if len(guess) != 1 and len(guess) != number_of_letters:
            guess = str(input("You should write only one letter or a whole word! Do this now: "))
        if guess == secret_word:
            print("Congratulations! You won the game in " + str(number_of_guesses) + " guesses!")
            break
        elif guess in secret_word:
            print("You guessed the letter correctly!")
            number_of_guessed_letters = secret_word.count(guess)
            i = 0
            index_of_next_guessed_letter = -1
            while i < number_of_guessed_letters:
                index_of_next_guessed_letter += 1
                index_of_guessed_letter = secret_word.find(guess, index_of_next_guessed_letter)
                secret_word_to_guess[index_of_guessed_letter] = guess
                index_of_next_guessed_letter = index_of_guessed_letter
                i += 1
            print(secret_word_to_guess)
        elif guess not in secret_word:
            remaining_chances -= 1
            if remaining_chances == 0:
                print("You lost the game! The right answer is: " + secret_word)
                break
            else:
                print("You guessed wrong! you have only " + str(remaining_chances) + " chances to guess left!\n" +
                      str(secret_word_to_guess))
        if "_" not in secret_word_to_guess:
            print("Congratulations! You won the game in " + str(number_of_guesses) + " guesses!")
            break


hangman_main()
