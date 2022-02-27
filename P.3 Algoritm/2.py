left = 1
right = 100
number  = 37
lin_attempts = 0
bin_atempts = 0
def linear():
    global lin_attempts
    print(f'Линейный поиск от {left} до {right}')
    current = left
    while True:
        lin_attempts += 1
        #print(f'Я думаю это число {current}')
        if number != current:
            #print((f' Не то увеличу на 1'))
            current +=1
        else:
            print('Нашел')
            break
    print(f"Мне понадобилось {lin_attempts} попыток.")


def binar():
    global  bin_atempts
    global right
    global left
    bin_atempts += 1

    while True:
        bin_atempts += 1
        print(f'Бинарный поиск, ')
        current = ((right + left) // 2)
        print(current)

        if current < number:
            left = current +1
        elif current > number:
            right = current -1
        elif current == number:
            print(f'Бинарный поиск, колличество попыток {bin_atempts}')
            break
        print(left, right, current)





linear()
binar()


