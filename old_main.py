# Roll a Dice, Odd = 0, Even = 1
# Convert roll into binary
# Use letters to make words, and get points
from random import *
from sys import exit
import string
import json


def want_to_play():
    # Asks user if they want to play
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


def roll_and_binary_converter():
    global character_bank
    binary_data = "011"
    rolls = []
    roll_and_binary_converter.rolls = []
    rolls.clear()
    roll_and_binary_converter.rolls.clear()
    input("Press enter to roll: ")
    for _ in range(5):
        rolls.append(randint(1, 6))
    print(rolls)
    for number in range(len(rolls)):
        if rolls[number] % 2 == 0:
            rolls[number] = 1
        else:
            rolls[number] = 0
        roll_and_binary_converter.rolls.append(rolls[number])
    alphabet = list(string.ascii_lowercase)
    for number in roll_and_binary_converter.rolls:  # For the 5 rolls
        binary_data += str(number)
    print(binary_data)

    while True:
        try:
            letter = chr(int(binary_data, 2))  # Converts binary to letter
            print(letter)
            if len(character_bank) <= 2:  # 2 is a placeholder atm
                print(len(character_bank))
                character_bank.append(letter)
                print(character_bank)
                roll_and_binary_converter()
                print("test")
                break
            if letter not in alphabet:
                reroll = input("Your roll is invalid. Would you like to reroll? (Y/N) ").title()
                if reroll == "Y":
                    roll_and_binary_converter()
                    break
                elif reroll == "N":
                    print("Quitting Program")
                    exit()
                else:
                    break
            else:
                break

        except ValueError:
            if len(character_bank) <= 2:
                roll_and_binary_converter()
            else:
                break


def check_word():
    file = open('Dictionary.json')
    print("test")

    # returns JSON object as a dictionary
    data = json.load(file)

    for i in data:
        if i in character_bank:
            print("yes")

    # Closing file
    file.close()


character_bank = []


def main():
    want_to_play()
    roll_and_binary_converter()
    # check_word()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

