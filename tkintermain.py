from tkinter import *
from random import *
from sys import exit
import string
import json


root = Tk()
root.geometry("1080x720")
root.title("Word Game")
root.configure(background="#32A868")

character_bank = []


rolling_button = Button(root, text="Roll", width=10, height=2, font=("Arial", 16), background="#32A868", activebackground="#32A868", highlightthickness=0, command=lambda x="test" : tkinterbutton())
rolling_button.place(x=1080, y=0, anchor="ne")

def tkinterbutton():
    y= 250
    binary_number_canvas = Canvas(root, width=450, height=200, background="#32A868", bd=0, highlightthickness=0)
    binary_number_canvas.place(x=540, y=y, anchor="center")

    converted_number_canvas = Canvas(root, width=450, height=200, background="#32A868", bd=0, highlightthickness=0)
    converted_number_canvas.place(x=540, y=y+200, anchor="center")

    your_character_canvas = Canvas(root, width=300, height=200, background="#32A868", bd=0, highlightthickness=0)
    your_character_canvas.place(x=540, y=y+325, anchor="center")

    character_bank_canvas = Canvas(root, width=1080, height=100, background="#32A868", bd=0, highlightthickness=0)
    character_bank_canvas.place(x=0, y=720, anchor="sw")

    vowels = ["a", "e", "i", "o", "u", "y"]


    alphabet = list(string.ascii_lowercase)  # Get the alphabet as a list in all lowercase

    global character_bank
    reroll = True
    while True:
        # Since all binary_data letters start with 011, to increase the odds and make the game *actually*
        # playable. We set the first three letters to 011
        if len(character_bank) > 1:
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
                reroll = False
                continue
            else:  # If it is a letter in the alphabet append to the list, and show user what letters they currently
                # have.
                reroll = True
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
                    binary_number_canvas.create_text(i*100+11, 10, text=og_rolls[i], font=("Arial", 28), fill="white", anchor="nw")
                for i in range(len(rolls)):
                    converted_number_canvas.create_text(i*100+11, 10, text=rolls[i], font=("Arial", 28), fill="white", anchor="nw")
                your_character_canvas_text = your_character_canvas.create_text(0, 0, text=f'Your Letter is: {letter}', font=("Arial", 28), fill="white", anchor="nw")
                character_bank_canvas_text = character_bank_canvas.create_text(25, 50, text=f'Your Character Bank: {character_bank}', font=("Arial", 16), fill="white", anchor="nw")

                # if character_bank_canvas.bbox(character_bank_canvas_text)[2] - character_bank_canvas.bbox(character_bank_canvas_text)[0] > 450:
                #     pass # Might do something with this later

                if len(character_bank) == 10:
                    print("You have reached the maximum amount of letters you can have")
                    character_bank_canvas.delete("all")
                    your_character_canvas.delete("all")
                    binary_number_canvas.delete("all")
                    converted_number_canvas.delete("all")
                    rolling_button.destroy()

                    letters_on_screen = []
                    rectangles_for_letters_on_screen = []

                    letter_canvas = Canvas(root, width=1080, height=300, background="#32A868", bd=0,
                                           highlightthickness=0)
                    letter_canvas.place(x=0, y=360, anchor="w")

                    temporary = letter_canvas.create_rectangle(515, 60, 565, 145, width=2)

                    typed_letters = []
                    def on_key_press(event):

                        user_inputted_letter = ""
                        user_inputted_letter += event.char
                        if user_inputted_letter in list(string.ascii_lowercase) and user_inputted_letter in character_bank:
                            typed_letters.append(user_inputted_letter)
                            text_box = letter_canvas.create_text(540, 100, text=user_inputted_letter, font=("Arial", 28), fill="white", anchor="center")
                            will_this_work = letter_canvas.create_rectangle(515, 60, 565, 145, width=2) #50x85 length x wdith
                            letters_on_screen.append(text_box)
                            rectangles_for_letters_on_screen.append(will_this_work)
                            if len(typed_letters) >= 1:
                                letter_canvas.delete(temporary)
                            if len(letters_on_screen) != 1:
                                multiplying_factor = len(letters_on_screen) - 1
                                for i in range(len(letters_on_screen)):
                                    if multiplying_factor > 0:
                                        letter_canvas.coords(letters_on_screen[i],540-25*multiplying_factor, 100)
                                        letter_canvas.coords(rectangles_for_letters_on_screen[i], 515 - 25 * multiplying_factor, 60, 565 - 25 * multiplying_factor, 145)
                                    else:
                                        letter_canvas.coords(letters_on_screen[i],540+25*abs(multiplying_factor), 100)
                                        letter_canvas.coords(rectangles_for_letters_on_screen[i], 515 + 25 * abs(multiplying_factor), 60, 565 + 25 * abs(multiplying_factor), 145)
                                    multiplying_factor -= 2

                    root.bind("<Key>", on_key_press)

                    character_bank_canvas = Canvas(root, width=1080, height=100, background="#32A868", bd=0,
                                                   highlightthickness=0)

                    make_word_button = Button(root, text="Make Word", width=12, height=3, font=("Arial", 18),
                                              background="#32A868", activebackground="#32A868", highlightthickness=0)

                    character_bank_canvas.place(x=0, y=0, anchor="nw")
                    character_bank_canvas.create_text(540, 50, text=f'Your Character Bank: {character_bank}',
                                                       font=("Arial", 26), fill="white", anchor="n")

                    make_word_button.place(x=540, y=550, anchor="center")


            break

def makewordbutton():
    '''
    when button.pressed = true:
        display box (letter)
    while
        if input() = enter:
            checkword()
    '''
    pass
def main():
    pass


root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
