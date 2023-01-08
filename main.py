# Roll a Dice, Odd = 0, Even = 1
# Convert roll into binary
# Use letters to make words, and get points
from random import *
from sys import exit
import string


def want_to_play():
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
    rolls = []
    roll_and_binary_converter.rolls = []
    input("Press enter to roll: ")
    for _ in range(8):
        rolls.append(randint(1, 6))
    print(rolls)
    for number in range(len(rolls)):
        print(number)
        if rolls[number] % 2 == 0:
            rolls[number] = 1
        else:
            rolls[number] = 0
        roll_and_binary_converter.rolls.append(rolls[number])
    print(rolls)

def binary_to_letter():
    binary_data = ""
    alphabet = list(string.ascii_lowercase)
    for _ in roll_and_binary_converter.rolls:
        binary_data = binary_data + str(_)
    # binary_data = int(binary_data)
    binary_data = int(binary_data)
    letter = chr(binary_data)
    if letter not in alphabet:
        while True:
            reroll = input("Your roll is invalid. Would you like to reroll? (Y/N) ").title()
            if reroll == "Y":
                roll_and_binary_converter()
            elif reroll == "N":
                print("Quitting Program")
                exit()
            else:
                continue
    else:
        print(letter)

    print(letter)
def main():
    want_to_play()
    roll_and_binary_converter()
    binary_to_letter()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
