# TODO
# S for shuffle
# I think there is some glitch I need to fix where if I press backspace and enter when no character are present on the sctrreen the temporary box is on screen

from tkinter import *
from random import *
import string
import json

root = Tk()
root.geometry("1080x720")
root.title("Word Game")
root.configure(background="#32A868")

character_bank = []
typed_letters = []

letters_on_screen = []
rectangles_for_letters_on_screen = []

number_of_correct_words = 0
used_words = []
file = open('Dictionary.json')
# returns JSON as a dictionary
word_bank = json.load(file)
# Closing file
file.close()

switch_case = BooleanVar(root)

letter_canvas = None
character_bank_canvas = None
your_character_canvas = None
binary_number_canvas = None
converted_number_canvas = None
make_word_button = None
temporary = None


number_of_correct_words_label = Label(root, text=f"Number of Correct Words: {number_of_correct_words}",
                                      font=("Arial", 15), background="#32A868")

#Start off with button placed
rolling_button = Button(root, text="Roll", width=15, height=5, font=("Arial", 16), background="#32A868",
                        activebackground="#32A868", highlightthickness=0, command=lambda x="test": tkinterbutton())
rolling_button.place(x=540, y=360, anchor="center")

def tkinterbutton():
    global switch_case, character_bank_canvas, your_character_canvas, binary_number_canvas, \
        converted_number_canvas, character_bank, letter_canvas, temporary, rolling_button

    rolling_button.configure(width=10, height=2)
    rolling_button.place(x=1080, y=0, anchor="ne")

    if character_bank_canvas is None:
        binary_number_canvas = Canvas(root, width=450, height=200, background="#32A868", bd=0, highlightthickness=0)
        binary_number_canvas.place(x=540, y=250, anchor="center")

        converted_number_canvas = Canvas(root, width=450, height=200, background="#32A868", bd=0, highlightthickness=0)
        converted_number_canvas.place(x=540, y=250 + 200, anchor="center")

        your_character_canvas = Canvas(root, width=300, height=200, background="#32A868", bd=0, highlightthickness=0)
        your_character_canvas.place(x=540, y=250 + 325, anchor="center")

        character_bank_canvas = Canvas(root, width=1080, height=100, background="#32A868", bd=0, highlightthickness=0)
        character_bank_canvas.place(x=0, y=720, anchor="sw")


    vowels = ["a", "e", "i", "o", "u", "y"]

    alphabet = list(string.ascii_lowercase)  # Get the alphabet as a list in all lowercase


    while True:
        your_character_canvas.place(x=540, y=250 + 325, anchor="center")
        # Since all binary_data letters start with 011, to increase the odds and make the game *actually*
        # playable. We set the first three letters to 011
        if len(character_bank) > 0:
            character_bank_canvas.delete("all")
            your_character_canvas.delete("all")
            binary_number_canvas.delete("all")
            converted_number_canvas.delete("all")
        if len(character_bank) < 10:  # 10 for now. Check to do list to see what I have planned for this
            binary_data = "011"
            rolls = []  # Creating the rolls list
            og_rolls = []
            number_of_vowels = 0
            rolls.clear()  # Clearing it for the new letter. One iteration of this loop = one letter
            og_rolls.clear()
            letter = ""
            for i in character_bank:
                if i in vowels:
                    number_of_vowels += 1
            if randint(1, 10) <= 5 and number_of_vowels <= 2:
                # 70% chance of getting a vowel
                # 30% chance of getting a constant
                letter = choice(vowels)
                your_character_canvas.place(x=540, y=400, anchor="center")

            else:
                for _ in range(5):
                    rolls.append(randint(1, 6))  # Adding 5 numbers to list
                og_rolls = rolls[:]
                for number in range(len(rolls)):  # If the roll is even it becomes a 1 and if it is odd it becomes odd
                    if rolls[number] % 2 == 0:
                        rolls[number] = 1
                    else:
                        rolls[number] = 0
                for number in rolls:  # For the 5 rolls
                    binary_data += str(number)  # Add it to the first 3 letters
                letter = chr(int(binary_data, 2))  # Converts binary to letter

            if letter not in alphabet or letter in character_bank:  # Some of the 011XXXXX binary contain stuff
                # beyond letters. This check if its is a letter and not a pre-existing letter in the character bank
                continue
            else:  # If it is a letter in the alphabet append to the list, and show user what letters they currently
                # have.
                character_bank.append(letter)

                if len(rolls) == 0:
                    print("\nYou have been granted a vowel")
                    print(f"The letter you rolled is: {letter}")
                    print(f"Your character Bank: {character_bank}\n")
                else:
                    print(f"\nYou Rolled: {og_rolls}")
                    print(f"Converted to: {rolls}")
                    print(f"The letter you rolled is: {letter}")
                    print(f"Your character Bank: {character_bank}\n")

                for i in range(len(og_rolls)):
                    binary_number_canvas.create_text(i * 100 + 11, 10, text=og_rolls[i], font=("Arial", 28),
                                                     fill="white", anchor="nw")
                for i in range(len(rolls)):
                    converted_number_canvas.create_text(i * 100 + 11, 10, text=rolls[i], font=("Arial", 28),
                                                        fill="white", anchor="nw")

                your_character_canvas.create_text(0, 0, text=f'Your Letter is: {letter}',
                                                  font=("Arial", 28), fill="white",
                                                  anchor="nw")
                character_bank_canvas.create_text(25, 50,
                                                  text=f'Your Character Bank: {character_bank}',
                                                  font=("Arial", 16), fill="white",
                                                  anchor="nw")

                if len(character_bank) == 10:
                    print("You have reached the maximum amount of letters you can have")
                    character_bank_canvas.delete("all")
                    your_character_canvas.delete("all")
                    binary_number_canvas.delete("all")
                    converted_number_canvas.delete("all")
                    rolling_button.destroy()

                    letter_canvas = Canvas(root, width=1080, height=300, background="#32A868", bd=0,
                                           highlightthickness=0)
                    letter_canvas.place(x=0, y=360, anchor="w")

                    character_bank_canvas.place(x=0, y=0, anchor="nw")
                    character_bank_canvas.create_text(540, 50, text=f'Your Character Bank: {character_bank}',
                                                      font=("Arial", 26), fill="white", anchor="n")

                    switch_case.set(not switch_case.get())
                    print(switch_case)
                    temporary = letter_canvas.create_rectangle(515, 60, 565, 145, width=2)
            break

#
def on_key_press(event, letter_or_backspace):
    global temporary
    print(temporary)
    user_inputted_letter = ""
    user_inputted_letter += event.char

    if letter_or_backspace != "backspace" and  user_inputted_letter in character_bank and len(letters_on_screen) < 21:
        letter_canvas.delete(temporary)
        temporary = None
        typed_letters.append(user_inputted_letter)
        text_box = letter_canvas.create_text(540, 100, text=user_inputted_letter,
                                             font=("Arial", 28), fill="white", anchor="center")
        first_box = letter_canvas.create_rectangle(515, 60, 565, 145,
                                                   width=2)  # 50x85 length x wdith
        letters_on_screen.append(text_box)
        rectangles_for_letters_on_screen.append(first_box)
    elif len(letters_on_screen) >= 1 and letter_or_backspace == "backspace":
        letter_to_delete = letters_on_screen[-1]
        letters_on_screen.pop(-1)
        letter_canvas.delete(letter_to_delete)

        rectangle_to_delete = rectangles_for_letters_on_screen[-1]
        rectangles_for_letters_on_screen.pop(-1)
        letter_canvas.delete(rectangle_to_delete)

        typed_letters.pop(-1)

    if len(typed_letters) >= 1:
        multiplying_factor = len(letters_on_screen) - 1
        temporary = None
        for i in range(len(letters_on_screen)):
            if multiplying_factor > 0:
                letter_canvas.coords(letters_on_screen[i], 540 - 25 * multiplying_factor, 100)
                letter_canvas.coords(rectangles_for_letters_on_screen[i],
                                     515 - 25 * multiplying_factor, 60,
                                     565 - 25 * multiplying_factor, 145)
            else:
                letter_canvas.coords(letters_on_screen[i], 540 + 25 * abs(multiplying_factor),
                                     100)
                letter_canvas.coords(rectangles_for_letters_on_screen[i],
                                     515 + 25 * abs(multiplying_factor), 60,
                                     565 + 25 * abs(multiplying_factor), 145)
            multiplying_factor -= 2
    if len(letters_on_screen) == 0 and temporary == None:
        temporary = letter_canvas.create_rectangle(515, 60, 565, 145, width=2)


def makewordbutton():
    global temporary, number_of_correct_words, letters_on_screen, letter_canvas
    x = "".join(typed_letters)
    duration = 0.5
    magnitude = 10
    frequency = 10
    if x in word_bank and len(x) >= 3 and x not in used_words:
        print("Correct")
        used_words.append(x)
        number_of_correct_words += 1

    else:
        # Get the initial position of the root window
        x = root.winfo_x()
        y = root.winfo_y()

        # Calculate the number of frames
        num_frames = int(duration * frequency)


        # Shake the screen by moving the root window randomly
        for _ in range(num_frames):
            dx = randint(-magnitude, magnitude)
            dy = randint(-magnitude, magnitude)
            root.geometry(f"+{x+dx}+{y+dy}")
            root.update()
            root.after(int(1000 / frequency))

        # Reset the position of the root window to the original position
        root.geometry(f"+{x}+{y}")
        root.update()
        # root.configure(background="red")
        # root.after(3000, root.configure(background="#32A868"))

    print(used_words)
    print(number_of_correct_words)
    # To reset the letters and rectangles on screen
    for i in letters_on_screen:
        letter_canvas.delete(i)
    for i in rectangles_for_letters_on_screen:
        letter_canvas.delete(i)
    letters_on_screen.clear()
    rectangles_for_letters_on_screen.clear()
    temporary = letter_canvas.create_rectangle(515, 60, 565, 145, width=2)
    typed_letters.clear()
    number_of_correct_words_label.config(text=f"Number of Correct Words: {number_of_correct_words}")

def switch_case_function(*args):
    root.bind("<Key>", lambda event: on_key_press(event, "letter"))
    root.bind("<BackSpace>", lambda event: on_key_press(event, "backspace"))
    root.bind("<Return>", lambda event: makewordbutton())

    make_word_button = Button(root, text="Make Word", width=12, height=3, font=("Arial", 18),
                              background="#32A868", activebackground="#32A868", highlightthickness=0,
                              command=makewordbutton)  # lambda x="test" : tkinterbutton()

    make_word_button.place(x=540, y=550, anchor="center")

    number_of_correct_words_label.place(x=0, y=720, anchor="sw")

switch_case.trace("w", lambda *args: switch_case_function())


root.mainloop()


def main():
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
