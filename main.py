marks = {
    "A1": " ",
    "A2": " ",
    "A3": " ",
    "B1": " ",
    "B2": " ",
    "B3": " ",
    "C1": " ",
    "C2": " ",
    "C3": " ",
}


def board():
    print("\n")
    print("\t     1     2     3")
    print("\t        |     |")
    print(f"\t  A  {marks['A1']}  |  {marks['A2']}  |  {marks['A3']}")
    print('\t   _____|_____|_____')

    print("\t        |     |")
    print(f"\t  B  {marks['B1']}  |  {marks['B2']}  |  {marks['B3']}")
    print('\t   _____|_____|_____')

    print("\t        |     |")
    print(f"\t  C  {marks['C1']}  |  {marks['C2']}  |  {marks['C3']}")
    print("\t        |     |")
    print("\n")


def check():
    if move.upper() in marks:
        if marks[move.upper()] != " ":
            print("Already taken")
            return False
        else:
            return True
    else:
        print("Wrong move")
        return False


def check_win():
    if marks["A1"] == marks["A2"] and marks["A1"] == marks["A3"] and marks["A1"] != " ":
        return True
    elif marks["B1"] == marks["B2"] and marks["B1"] == marks["B3"] and marks["B1"] != " ":
        return True
    elif marks["C1"] == marks["C2"] and marks["C1"] == marks["C3"] and marks["C1"] != " ":
        return True
    elif marks["A1"] == marks["B1"] and marks["A1"] == marks["C1"] and marks["A1"] != " ":
        return True
    elif marks["A2"] == marks["B2"] and marks["A2"] == marks["C2"] and marks["A2"] != " ":
        return True
    elif marks["A3"] == marks["B3"] and marks["A3"] == marks["C3"] and marks["A3"] != " ":
        return True
    elif marks["A1"] == marks["B2"] and marks["A1"] == marks["C3"] and marks["A1"] != " ":
        return True
    elif marks["A3"] == marks["B2"] and marks["A3"] == marks["C1"] and marks["A3"] != " ":
        return True
    else:
        return False


game_on = True
side = 1
board()

while game_on:

    if side == 1:
        player = "X"
    else:
        player = "O"

    move = input(f"Player {player} move: ")

    if check():
        print("OK")
        marks[move.upper()] = player
        side *= -1

    board()

    if check_win():
        print(f"Player {player} wins!!!")
        game_on = False

    if " " not in marks.values():
        print("Draw")
        game_on = False
