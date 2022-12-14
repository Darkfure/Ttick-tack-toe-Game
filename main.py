def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():
    print(f"  | 0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        row = " | ".join(field[i])
        print(f"{i} | {row} |")
        print("---------------")


def request():
    while True:
        crds = input("Ваш ход: ").split()

        if len(crds) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = crds

        if not (x.isdigit()) or not (y.isdigit()):
            print("Координаты должны быть в формате чисел")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона")
            continue

        if field[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
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
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        break

    if num == 9:
        print("Ничья")
        break
