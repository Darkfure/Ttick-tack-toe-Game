def request():
    while True:
        crds = input("Ваш ход: ").split()

        if len(crds) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = crds

        if not(x.isdigit()) or not(y.isdigit()):
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


request()