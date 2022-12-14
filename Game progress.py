num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print("Ходит X")
    else:
        print("Ходит 0")

    x, y = request()

    if num % 2 == 1:
        feeld[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        break

    if num == 9:
        print("Ничья")
        break


