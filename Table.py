field = [[" "]*3 for i in range(3)]

def show():
    print(f"  | 0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        row = " | ".join(field[i])
        print(f"{i} | {row} |")
        print("---------------")

show()