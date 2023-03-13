# Roll a Dice, Odd = 0, Even = 1
# Convert roll into binary
# Use letters to make words, and get points

"""
TODO
Make it so they roll a number for how many letters, but I set a hard min and max. Later on,
have difficulties, that decrease the max (Base Value will be 15) 

From the letters give some for vowels and constants, more for vowels than constants

Then add the word check

Some words use the same letters more than once, so account for that
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
    global character_bank
    while True:
        # Since all binary_data letters start with 011, to increase the odds and make the game *actually*
        # playable. We set the first three letters to 011
        binary_data = "011"
        if len(character_bank) < 10:  # 15 for now. Check to do list to see what I have planned for this
            rolls = []  # Creating the rolls list
            rolls.clear()  # Clearing it for the new letter. One iteration of this loop = one letter
            input("Press enter to roll: ")
            for _ in range(5):
                rolls.append(randint(1, 6))  # Adding 5 numbers to list
            print(f"\nYou Rolled: {rolls}")
            for number in range(len(rolls)):  # If the roll is even it becomes a 1 and if it is odd it becomes odd
                if rolls[number] % 2 == 0:
                    rolls[number] = 1
                else:
                    rolls[number] = 0
            print(f"Converted to: {rolls}")
            for number in rolls:  # For the 5 rolls
                binary_data += str(number)  # Add it to the first 3 letters
            letter = chr(int(binary_data, 2))  # Converts binary to letter
            print(f"The letter you rolled is: {letter}")

            alphabet = list(string.ascii_lowercase)  # Get the alphabet as a list in all lowercase
            if letter not in alphabet or letter in character_bank:  # Some of the 011XXXXX binary contain stuff
                # beyond letters. This check if its is a letter and not a pre-existing letter in the character bank
                while True:  # Again your standard user input while True loop
                    reroll = input("\nYour roll is invalid. Would you like to reroll? (Y/N) ").title()
                    if reroll == "Y":
                        break
                    elif reroll == "N":
                        print("Quitting Program")
                        exit()
                    else:
                        continue
            else:  # If it is a letter in the alphabet append to the list, and show user what letters they currently
                # have.
                character_bank.append(letter)
                print(f"Your character Bank: {character_bank}\n")
                # print(len(character_bank))
        else:
            break


def check_word():
    correct_words = 0
    used_words = []
    file = open('Dictionary.json')
    print(f"{file} opened")
    # returns JSON as a dictionary
    data = json.load(file)
    while True:
        while True:
            word = input("Make a word: ")
            for i in word:
                if i not in character_bank:  # Checks if the letters in the word are in the character bank
                    retry = input("That word contains letter not included in the word bank. Would you like try "
                                  "another word? (Y/N) ").title()
                    if retry == "Y":
                        break
                    elif retry == "N":
                        print("Quitting Program")
                        exit()
                    else:
                        continue
            else:
                if word in data and word not in used_words:  # Checks if the word is a real word, and has not already
                    # been used
                    print("Nice")
                    correct_words += 1
                    used_words.append(word)
                    print(f"Words: {correct_words}")
                    print(f"Used Words: {used_words}")
                else:
                    while True:
                        retry = input(
                            "That was an invalid word. Would you like try another word? (Y/N) ").title()  # Again
                        # another standard user input while True loop
                        if retry == "Y":
                            break
                        elif retry == "N":
                            print("Quitting Program")
                            exit()
                        else:
                            continue
            # Closing file
            file.close()


character_bank = []


def main():
    want_to_play()
    roll_to_binary_to_letter_converter()
    check_word()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
