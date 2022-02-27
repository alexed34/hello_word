import random


class Enemy:
    def __init__(self, name, health, attack, ):
        self.health = health
        self.attack = attack
        self.name = name

    def be_attacked(self, attack):  # нанесение урона в размере attack
        self.health = self.health - attack  # уменьшение здоровья


class User(Enemy):
    def __init__(self, name, health, attack, armor=10):
        super(User, self).__init__(name, health, attack)
        self.max_health = health
        self.armor = armor

    def heal(self):
        if self.health < self.max_health:
            health = self.health//10
            self.health += health
            print('Ты восстановил', health, 'твое текущее здоровье', self.health)
        else:
            print('Невозможно восстановить здоровье')
    def be_attacked(self, attack):
        self.health = int(self.health - (attack - self.armor))
        if self.armor > 0:
            self.armor -= int(attack / 2)
        else:
            self.armor = 0


user = User(name='Edik', health=200, attack=16)

enemy_1 = Enemy('первый', health=330, attack=10)
enemy_2 = Enemy('второй', health=310, attack=11)
enemy_3 = Enemy('третий', health=300, attack=12)

eminems = [enemy_1, enemy_2, enemy_3]

enemy = random.choice(eminems)

print(f'Твой соперник {enemy.name}')

while True:
    print(f'Твое здоровье: {user.health}, твоя атака: {user.attack}, твоя броня {user.armor}')
    print(f'Здоровье противника: {enemy.health}, атака противника {enemy.attack}')



    user_input = input('Выберите действие:\n1 - увеличить здоровье\n2 -атаковать\nвведите число: ')
    if user_input == '1':
        user.heal()
    elif user_input == '2':
        enemy.be_attacked(user.attack)
        user.be_attacked(enemy.attack)
        print(f'Тебе нанесено {enemy.attack} урона')

    if user.health <= 0 and enemy.health <= 0:
        print('Игра окончена, Ничья')
        break
    elif user.health <= 0 or enemy.health <= 0:
        print('Игра окончена')
        break

# # enemy.be_attacked(10)
# print(enemy.health, enemy_2.health)
#
# hits = 0
# # win = False # проверка на победу
# while True:
#     if enemy.health <= 0 and enemy_2.health <= 0:  # если здоровье обоих  стало <= 0
#         print('Ничья')
#         break
#         # win = True
#     elif enemy.health <= 0:  # если здоровье 1 врага <= 0
#         print('Второй победил')
#         print("У него осталось здоровья", enemy_2.health)
#         break
#         # win = True
#     elif enemy_2.health <= 0:  # если здоровье 2 врага <= 0
#         print('Первый победил')
#         print("У него осталось здоровья", enemy.health)
#         break
#         # win = True
#
#     # if win is True:  # победа, это уже другой блок условий
#     #     print('Ударов совершено', hits)
#     #     break
#     enemy.be_attacked(enemy_2.attack)
#     enemy_2.be_attacked(enemy.attack)
#     hits += 1
#     enemy_2.attack = random.randint(1,20)
#     enemy.attack = random.randint(1,20)
#     print(enemy.health, enemy_2.health)
# print(hits, enemy.health, enemy_2.health)
