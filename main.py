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
    for _ in range(5):
        rolls.append(randint(1, 6))
    print(rolls)
    for number in range(len(rolls)):
        if rolls[number] % 2 == 0:
            rolls[number] = 1
        else:
            rolls[number] = 0
        roll_and_binary_converter.rolls.append(rolls[number])
    print(roll_and_binary_converter.rolls)


def binary_to_letter():
    global letters
    binary_data = "011"
    alphabet = list(string.ascii_lowercase)
    print(roll_and_binary_converter.rolls)
    for number in roll_and_binary_converter.rolls:
        binary_data = binary_data + str(number)
    # binary_data = int(binary_data)
    print(binary_data)

    while True:
        try:
            letter = chr(int(binary_data, 2))
            print(letter)
        except ValueError:
            roll_and_binary_converter()
        if letter not in alphabet:
            reroll = input("Your roll is invalid. Would you like to reroll? (Y/N) ").title()
            if reroll == "Y":
                roll_and_binary_converter()
            elif reroll == "N":
                print("Quitting Program")
                exit()
            else:
                continue
        else:
            roll_and_binary_converter()



def main():
    want_to_play()
    roll_and_binary_converter()
    binary_to_letter()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
