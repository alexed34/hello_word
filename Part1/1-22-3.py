import random


class Enemy:  # создаем класс врага
    def __init__(self, name, health, attack):  # создаем врага
        self.health = health  # присваиваем переданное здоровье объекту
        self.attack = attack
        self.name = name

    def be_attacked(self, attack):  # быть атакованным
        self.health = self.health - attack  # уменьшение здоровья


class User(Enemy):  # наследование класса
    def __init__(self, name, health, attack, armor=10):  # переопредление метода создания
        super().__init__(name, health, attack)
        self.armor = armor
        self.max_health = health

    def heal(self):  # восстановление здоровья
        if not self.health >= self.max_health:
            health = self.health // 10
            self.health += health
            print('Ты восстановил', health, 'твое текущее здоровье', self.health)
        else:
            print('Невозможно восстановить здоровье')

    def be_attacked(self, attack):
        self.health = int(self.health - (attack - self.armor))
        if self.armor > 0:
            self.armor -= int(attack / 2)
            if self.armor < 0:
                self.armor = 0


enemy_1 = Enemy(name='Рыцарь', health=330, attack=10)  # создаем объект класса
enemy_2 = Enemy(name='Боец', health=200, attack=18)
enemy_3 = Enemy(name='Убийца', health=150, attack=25)
enemies = [enemy_1, enemy_2, enemy_3]  # список с врагами
enemy = random.choice(enemies)  # случайный выбор врага
user = User(name='My_name', health=200, attack=16)  # создание персонажа пользователя

print('Твой соперник', enemy.name)  # вывод имени соперника

while True:
    print(f'Твое здоровье: {user.health}, твоя атака: {user.attack}, твоя броня {user.armor}')
    print(f'Здоровье противника: {enemy.health}, атака противника {enemy.attack}')
    userinput = input('\nВыберите действие:\n1 - увеличить здоровье\n2 - атаковать\n')
    if userinput == '1':
        user.heal()
    if userinput == '2':
        enemy.be_attacked(user.attack)
    user.be_attacked(enemy.attack)
    print('Тебе нанесено', enemy.attack, 'урона')
    if user.health <= 0 and enemy.health <= 0:
        print('Ничья')
        break
    elif user.health <= 0:
        print('Ты проиграл')
        break
    elif enemy.health <= 0:
        print('Ты выиграл')
        break
# игра с прошлого урока
# hits = 0
# win = False
# while True:
#     if enemy_1.health <= 0 and enemy_2.health <= 0:  # and - если оба условия верны, or - если одно из условий верно
#         print('Ничья')
#         win = True
#     elif enemy_1.health <= 0:
#         print('Второй победил')
#         print(enemy_2.health)  # здоровье второго врага
#         win = True
#     elif enemy_2.health <= 0:
#         print('Первый победил')
#         print(enemy_1.health)
#         win = True
#     if win is True:
#         print('hits', hits)
#         break
#     hits += 1
#     enemy_1.be_attacked(enemy_2.attack)  # вызываем метод "быть атакованным" и передаем ему атаку соперника
#     enemy_2.be_attacked(enemy_1.attack)
#
