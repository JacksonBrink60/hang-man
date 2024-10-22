import random


hang = ["   _____", "  |/    |", "  |    ",
        "  |", "  |", "  |", "  |", "  |", "__|__"]


keywords = ["apple", "xylophone", "marchingband", "afjrotc", "xboxseriesx",
            "snaredrum", "bassdrum", "tenordrums", "walkitoff", "power"]


valid = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def begin():
    """Introduction - ask the user if they want to play the game"""
    yn = ""
    while yn not in ["yes", "no", "y", "n"]:
        yn = input("Would you like to play a game? (yes/no): ").lower().strip()
        if yn not in ["yes", "no", "y", "n"]:
            print("ERROR: Please enter 'yes' or 'no'.")
    return yn


def sticks(strikes):
    """Function to handle stickman drawing based on the number of strikes"""
    if strikes >= 1:
        hang[2] = "  |    (_)"
    if strikes >= 2:
        hang[3] = "  |     |"
        hang[4] = "  |     |"
    if strikes >= 3:
        hang[3] = "  |    \\|"
    if strikes >= 4:
        hang[3] = "  |    \\|/"
    if strikes >= 5:
        hang[5] = "  |    /"
    if strikes >= 6:
        hang[5] = "  |    / \\"
    return hang


def guess(keyword, space):
    """Function to get a player's guess and check if it's valid"""
    gues = ""
    while gues not in valid:
        gues = input("Guess a letter: ").strip().lower()
    if gues in keyword:
        for i, letter in enumerate(keyword):
            if letter == gues:
                space[i] = f"{gues} "
    return gues


def board(hang, space, incgues):
    """Function to print the current game board"""
    for line in hang:
        print(line)
    print("Word: ", end=" ")
    for char in space:
        print(char, end=" ")
    print("\nIncorrect guesses: ", ", ".join(incgues))


def play_game():
    """Main function to play the game"""
    strikes = 0
    keyword = keywords[random.randint(0, 9)]
    space = ["_ "] * len(keyword)
    incgues = []

    yn = begin()
    if yn in ["yes", "y"]:
        while strikes < 6 and "_ " in space:
            board(hang, space, incgues)
            gues = guess(keyword, space)
            if gues not in keyword:
                strikes += 1
                incgues.append(gues)
            sticks(strikes)

        board(hang, space, incgues)

        if "_ " not in space:
            print("Congratulations, you won!")
        else:
            print(f"You lost! The word was '{keyword}'.")
    else:
        print("Goodbye!")


def playagain():
    """Ask the player if they want to play again"""
    plaag = ""
    while plaag not in ["yes", "no"]:
        plaag = input(
            "Would you like to play again? (yes/no): ").strip().lower()
        if plaag not in ["yes", "no"]:
            print("ERROR: Please enter 'yes' or 'no'.")
    return plaag


def play():
    """Game loop to keep playing or exit"""
    plaag = ""
    while plaag != "no":
        play_game()
        plaag = playagain()
        if plaag == "no":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    play()
