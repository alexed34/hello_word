import copy, random, sys, time

WITH = 10
HIGHT = 10
LIFE = "0"
DIED = " "

next_cells = {}
for i in range(WITH):
    for j in range(HIGHT):
        microb = random.randint(0, 1)
        if microb == 0:
            next_cells[(i, j)] = LIFE
        else:
            next_cells[(i, j)] = DIED
    #     print(microb, end=" ")
    # print()
# print(next_cells)

while True:
    print("\n" * 5)
    cells = copy.deepcopy(next_cells)
    for x in range(WITH):
        for y in range(HIGHT):
            print(cells[(x, y)], end=" ")
        print()
    print('Press Ctrl-C to quit.')

    for x in range(WITH):
        for y in range(HIGHT):
            left = (x - 1) % WITH
            right = (x + 1) % WITH
            up = (y - 1) % HIGHT
            down = (y + 1) % HIGHT
            life_num = random.randint(1, 5)
            #         if cells[(left,up)] == LIFE:
            #             life_num += 1
            #         if cells[(x,up)] == LIFE:
            #             life_num += 1
            #         if cells[(right,up)] == LIFE:
            #             life_num += 1
            #         if cells[(left,y)] == LIFE:
            #             life_num += 1
            #         if cells[(right,y)] == LIFE:
            #             life_num += 1
            #         if cells[(left,down)] == LIFE:
            #             life_num += 1
            #         if cells[(x,down)] == LIFE:
            #             life_num += 1
            #         if cells[(right,down)] == LIFE:
            #             life_num += 1
            if cells[(x, y)] == LIFE and (life_num == 2 or life_num == 3):
                next_cells[(x, y)] = LIFE
            elif cells[(x, y)] == DIED and life_num == 3:
                next_cells[(x, y)] = LIFE
            else:
                next_cells[(x, y)] = DIED
    time.sleep(1)
    # print(life_num)
