import random

all = 100
while all > 0:
    number = input('Ваше число от 1 до 12? или stop ')
    if number == 'stop':
        print('Конец игры')
        break
    stavka = int(input('Ставка: '))
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    summa = num1 + num2


    number = int(number)
    if number < 7 and summa < 7:
        all += stavka
        print(f'Ты выиграл, общая сумма {all}')
    elif number > 7 and summa > 7:
        all += stavka
        print(f'Ты выиграл, общая сумма {all}')
    elif number == summa:
        all += (stavka *4)
        print(f'Ты выиграл {stavka *4}, общая сумма {all}')
    else:
        all -= stavka
        print(f'Ты проиграл, общая сумма {all}')

