import random
left = int(input('Min число: '))
right = int(input('Max число: '))
print(f'Привет загадай число от {left} до {right}, а я отгадаю его менее чем за 10 шагов')
curent = round((left + right)/2)

attemts = 0

while True:
    is_right = input(f'Ваше число {curent}? (да, >, <)')
    if is_right == '>':
        left = curent+1;
        print(left,right)
    elif is_right == '<':
        right = curent - 1
        print(left, right)
    else:
        print('Я угадал!!')
        print(f'попыток {attemts}')
        break
    curent = round((left + right)/2)
    attemts += 1


