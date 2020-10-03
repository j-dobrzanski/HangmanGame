from tkinter import *
from PIL import ImageTk, Image
from getting_random_word import random_word

# Creating main window of the game
root = Tk()
root.title("The Hangman Game!")
root.geometry("500x500")
root.iconbitmap('HangmanImages\hangman_icon_BhA_icon.ico')

# Creating and setting main variables used in game
number_of_guesses = IntVar()
number_of_guesses.set(0)
remaining_chances = IntVar()
remaining_chances.set(10)
made_guesses = []


def hangman_main():
    global number_of_guesses
    global remaining_chances
    global made_guesses
    remaining_chances_value = remaining_chances.get()

    # Setting a word to guess and creating a list to store it's characters
    secret_word = random_word().strip()
    number_of_letters = IntVar
    number_of_letters = len(secret_word)
    i = 0
    secret_word_to_guess = []
    while i < number_of_letters:
        secret_word_to_guess.append("_")
        i += 1

    # Setting a main view of the game interface: buttons, labels, images, etc.
    prompt_label = Label(root, text="Welcome to The Hangman Game!")
    prompt_label.grid(row=1, column=0, columnspan=2)
    chances_counter_label = Label(root, text="You have " + str(remaining_chances_value) + " chances left!")
    chances_counter_label.grid(row=1, column=2, sticky=E)
    guessing_word_label = Label(root, text=secret_word_to_guess)
    guessing_word_label.grid(row=2, column=0)
    guess_label = Label(root, text="Guess a letter or a whole word: ")
    guess_label.grid(row=3, column=0)
    guess_entry = Entry(root)
    guess_entry.grid(row=3, column=1)
    basic_image = ImageTk.PhotoImage(Image.open("HangmanImages\state0.png"))
    image_label = Label(image=basic_image)
    image_label.image = basic_image
    image_label.grid(row=4, column=0, columnspan=2)
    made_guesses_label = Label(root, text='')
    made_guesses_label.grid(row=6, column=0)

    def click():
        global remaining_chances_value
        global made_guesses

        # Counting the number of guesses needed by the user to guess the word
        number_of_guesses.set(number_of_guesses.get() + 1)

        # Taking the guess from the user
        guess = guess_entry.get()

        # Checking if user wrote a letter or a whole world, otherwise the game will bug
        if len(guess) != 1 and len(guess) != number_of_letters:
            prompt_label.configure(text="You should write only one letter or a whole word!")
            guess_label.configure(text=" Do this now: ")
            guess_entry.delete(0, END)
            return

        # If user made that guess already inform them about that
        if guess in made_guesses:
            prompt_label.configure(text="You already made that guess!! Try one more time")
            guess_entry.delete(0, END)
            return

        # Adding to a list of already made guesses
        made_guesses.append(guess)
        made_guesses_label.configure(text=str(made_guesses))

        # Main part of the game, considering all possible cases of user guess
        # If user guesses the whole world
        if guess == secret_word:
            prompt_label.configure(text="Congratulations! You won the game in " + str(number_of_guesses) + " guesses!")
            guess_entry.delete(0, END)
            return
        # If user's guessed letter is in the word
        elif guess in secret_word:
            prompt_label.configure(text="You guessed the letter correctly!")
            number_of_guessed_letters = secret_word.count(guess)

            # Calculating on which positions should the guessed letter be inserted
            i = 0
            index_of_next_guessed_letter = -1
            while i < number_of_guessed_letters:
                index_of_next_guessed_letter += 1
                index_of_guessed_letter = secret_word.find(guess, index_of_next_guessed_letter)
                secret_word_to_guess[index_of_guessed_letter] = guess
                index_of_next_guessed_letter = index_of_guessed_letter
                i += 1

            # Preparing the labeled string of guessed and unguessed letters
            secret_word_to_guess_in_string = ""
            for item in secret_word_to_guess:
                secret_word_to_guess_in_string += item
            guessing_word_label.configure(text=secret_word_to_guess_in_string)

        # If user guessed the letter wrong
        elif guess not in secret_word:

            # Changing the image of the hangman
            remaining_chances.set(remaining_chances.get() - 1)
            remaining_chances_value = remaining_chances.get()
            state_number = 10 - remaining_chances_value
            state_image = ImageTk.PhotoImage(Image.open("HangmanImages\state" + str(state_number) + ".png"))
            image_label.configure(image=state_image)
            image_label.image = state_image

            chances_counter_label.configure(text="You have " + str(remaining_chances_value) + " chances left!")

            # Checking if user can still play the game
            if remaining_chances_value == 0:
                prompt_label.configure(text="You lost the game! The right answer is: " + secret_word)
                guess_entry.delete(0, END)
                return
            else:
                prompt_label.configure(text="You guessed wrong!")

        # If user guessed all the letters in the word one by one and won the game
        if "_" not in secret_word_to_guess:
            number_of_guesses_value = number_of_guesses.get()
            prompt_label.configure(text="Congratulations! You won the game in " + str(number_of_guesses_value)
                                        + " guesses!")

        # Making the entry block clean for the next guess
        guess_entry.delete(0, END)

    submit_button = Button(root, text="Guess!", command=click)
    submit_button.grid(row=4, column=1)


play_button = Button(root, text="Let's play a new Hangman game!", command=hangman_main)
play_button.pack(anchor='n')

root.mainloop()
