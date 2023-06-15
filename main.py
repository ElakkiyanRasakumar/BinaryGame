# Roll a Dice, Odd = 0, Even = 1
# Convert roll into binary
# Use letters to make words, and get points

"""
TODO
Make it so they roll a number for how many letters, but I set a hard min and max. Later on,
have difficulties, that decrease the max (Base Value will be 10) ) - DO WITH GUI

From the letters give some for vowels and constants, more for vowels than constants

Some words use the same letters more than once, so account for that

Check for aliasing for def want_to_play()

Add ability to quit program
"""

from random import *
from sys import exit
import string
import json


def want_to_play():
    # Asks user if they want to play
    # Your day-to-day while True user input loop
    while True:
        input_to_play = input("Would you like to play? (Y/N): ").title()
        if input_to_play == "Y":
            break
        elif input_to_play == "N":
            if input("Are you sure? (Y/N): ").title() == "Y":
                exit()
            else:
                continue
        else:
            continue


def roll_to_binary_to_letter_converter():
    vowels = ["a", "e", "i", "o", "u", "y"]
    # a = 01100001
    # e = 01100101
    # i = 01101001
    # o = 01101111
    # u = 01110101
    # y = 01111001
    alphabet = list(string.ascii_lowercase)  # Get the alphabet as a list in all lowercase

    global character_bank
    reroll = True
    while True:
        # Since all binary_data letters start with 011, to increase the odds and make the game *actually*
        # playable. We set the first three letters to 011
        binary_data = "011"
        if len(character_bank) < 10:  # 10 for now. Check to do list to see what I have planned for this
            rolls = []  # Creating the rolls list
            og_rolls = []
            number_of_vowels = 0
            rolls.clear()  # Clearing it for the new letter. One iteration of this loop = one letter
            og_rolls.clear()
            letter = ""
            for i in character_bank:
                if i in vowels:
                    number_of_vowels += 1

            if reroll:
                input("Press enter to roll: ")


            if randint(1, 10) <= 7 and number_of_vowels <= 2:
                # 70% chance of getting a vowel
                # 30% chance of getting a constant
                letter = choice(vowels)
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
        else:
            break


def check_word():
    correct_words = 0
    used_words = []
    file = open('Dictionary.json')
    # returns JSON as a dictionary
    word_bank = json.load(file)
    # Closing file
    file.close()
    while True:
        print(f"\n{character_bank}")
        word = input("Make a word: ").lower()
        if word == "s":
            shuffle(character_bank)
            continue
        for i in word:
            if i not in character_bank:  # Checks if the letters in the word are in the character bank
                print("That word contains letter not included in the word bank. Try again")
                break
            if word in used_words:
                print("You already used that word. Try again.") # Checks if the word has already been used

            elif word in word_bank and len(word) > 2:  # Checks if the word is a real word
                used_words.append(word)
                correct_words += 1
                print(f"Nice. Words Correct: {used_words}")
            else:
                if len(word) <= 2:
                    print("\nThat word was too SHORT. Try again.")
                else:
                    print("\nThat was an invalid word. Try again.")
                shuffle_input = input("Press S to shuffle the word bank or ENTER to continue: ").lower()
                if shuffle_input == "s":
                    shuffle(character_bank)
            break



character_bank = []


def main():
    try:
        want_to_play()
        roll_to_binary_to_letter_converter()
        check_word()
    except KeyboardInterrupt:
        exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
