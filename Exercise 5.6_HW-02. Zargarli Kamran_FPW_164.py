print("")
print("TIC TIC TOE GAME")
print("")
field = list(range(1, 10))

wins_set = [(1, 2, 3), (4, 5, 6), (7, 8, 9,), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def play_field():
    print("-------------")
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
    print("-------------")


def play_move(game_chip):
    while True:
        print("")
        value = input("Where to put: " + game_chip + " ? ")
        if not (value in "123456789"):
            print("Wrong move. Go again!")
            continue
        value = int(value)
        if str(field[value - 1]) in "XO":
            print("Busy!")
            continue
        field[value - 1] = game_chip
        break


def win_comb():
    for a in wins_set:
        if (field[a[0] - 1]) == (field[a[1] - 1]) == (field[a[2] - 1]):
            return field[a[1] - 1]
    else:
        return False


def xo_game():
    counter = 0
    while True:
        play_field()
        if counter % 2 == 0:
            play_move("X")
        else:
            play_move("O")
        if counter > 3:
            champ = win_comb()
            if champ:
                play_field()
                print("")
                print(champ, "Won!")
                break
        counter += 1
        if counter > 8:
            play_field()
            print("")
            print("There is no winner")
            break


xo_game()
