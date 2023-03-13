# Roll a Dice, Odd = 0, Even = 1
# Convert roll into binary
# Use letters to make words, and get points

"""
TODO
Make it so they roll a number for how many letters, but I set a hard min and max. Later on,
have difficulties, that decrease the max

From the letters give some for vowels and constants, more for vowels than constants

Then add the word check
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
        try:
            binary_data = "011"
            if len(character_bank) < 15:
                rolls = []
                roll_to_binary_to_letter_converter.rolls = []
                rolls.clear()
                roll_to_binary_to_letter_converter.rolls.clear()
                input("Press enter to roll: ")
                for _ in range(5):
                    rolls.append(randint(1, 6))
                print(rolls)
                for number in range(len(rolls)):
                    if rolls[number] % 2 == 0:
                        rolls[number] = 1
                    else:
                        rolls[number] = 0
                    roll_to_binary_to_letter_converter.rolls.append(rolls[number])
                for number in roll_to_binary_to_letter_converter.rolls:  # For the 5 rolls
                    binary_data += str(number)
                print(binary_data)
                letter = chr(int(binary_data, 2))  # Converts binary to letter
                print(letter)

                alphabet = list(string.ascii_lowercase)
                if letter not in alphabet:
                    while True:
                        reroll = input("Your roll is invalid. Would you like to reroll? (Y/N) ").title()
                        if reroll == "Y":
                            break
                        elif reroll == "N":
                            print("Quitting Program")
                            exit()
                        else:
                            continue
                else:
                    character_bank.append(letter)
                    print(character_bank)
                    print(len(character_bank))
            else:
                break

        except ValueError:
            print("valueerror")
            if len(character_bank) < 15:
                continue
            else:
                break


character_bank = []


def main():
    want_to_play()
    roll_to_binary_to_letter_converter()
    # check_word()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
