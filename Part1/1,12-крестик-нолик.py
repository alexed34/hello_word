

def check_winner():
    if area[0][0] == "x" and area[0][1] == "x" and area[0][2] == "x":
        return "x"
    if area[1][0] == "x" and area[1][1] == "x" and area[1][2] == "x":
        return "x"
    if area[2][0] == "x" and area[2][1] == "x" and area[2][2] == "x":
        return "x"
    if area[0][0] == "x" and area[1][0] == "x" and area[2][0] == "x":
        return "x"
    if area[0][1] == "x" and area[1][1] == "x" and area[2][1] == "x":
        return "x"
    if area[0][2] == "x" and area[1][2] == "x" and area[2][2] == "x":
        return "x"
    if area[0][0] == "x" and area[1][1] == "x" and area[2][2] == "x":
        return "x"
    if area[0][2] == "x" and area[1][1] == "x" and area[2][0] == "x":
        return "x"
    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":
        return "0"
    if area[1][0] == "0" and area[1][1] == "0" and area[1][2] == "0":
        return "0"
    if area[2][0] == "0" and area[2][1] == "0" and area[2][2] == "0":
        return "0"
    if area[0][0] == "0" and area[1][0] == "0" and area[2][0] == "0":
        return "0"
    if area[0][1] == "0" and area[1][1] == "0" and area[2][1] == "0":
        return "0"
    if area[0][2] == "0" and area[1][2] == "0" and area[2][2] == "0":
        return "0"
    if area[0][0] == "0" and area[1][1] == "0" and area[2][2] == "0":
        return "0"
    if area[0][2] == "0" and area[1][1] == "0" and area[2][0] == "0":
        return "0"
    return "*"

area = [["*","*","*"],["*","*","*"],["*","*","*"]]
turn_char = '0'
for turn in range(1,10):
    if turn % 2 == 0:
        turn_char = "0"
        print("Ходят нолики")
    else:
        turn_char = "x"
        print("Ходят крестики")
    # turn_char = 'x' if turn_char == '0' else '0'
    row = int(input("Введите номер строки(0,1 или 2): "))
    column = int(input("Введите номер столбца(0,1 или 2): "))
    area[row-1][column-1] = turn_char

    for cell in area:
        print(*cell)

    if check_winner() == "x":
        print("Победа крестиков")
        break
    if check_winner() == "0":
        print("Победа ноликов")
        break
    if turn == 9 and check_winner() == "*":
        print("Ничья")