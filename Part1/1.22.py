import random


class Enemy:
    def __init__(self, name,  health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def be_attacked(self, attack):  # нанесение урона в размере attack
        self.health = self.health - attack  # уменьшение здоровья


class User(Enemy):
    def __init__(self, name, health, attack,armor = 10):
        super().__init__(name, health, attack)  # это мы наследуем от родителя
        self.max_health = health
        self.armor = armor

    def heal(self):
        if not self.health >= self.max_health:
            health = 20
            health = self.health // 10
            print('Ты восстановил', health, 'твое текущее здоровье', self.health)
        else:
            print('Невозможно восстановить здоровье')

        def be_attacked(self, attack):
            self.health = int(self.health - (attack - self.armor))
            if self.armor > 0:
                self.armor -= int(attack / 2)
                if self.armor < 0:
                    self.armor = 0






enemy_1 = Enemy(name='Рыцарь', health=330, attack=10)
enemy_2 = Enemy(name='Боец', health=200, attack=18)
enemy_3 = Enemy(name='Убийца', health=150, attack=25)
user = User(name='Edik', health=200, attack=16)

enemies = [enemy_1, enemy_2, enemy_3]
enemy = random.choice(enemies)
print('Твой соперник', enemy.name)


while True:
    print(f'Твое здоровье: {user.health}, твоя атака: {user.attack}, твоя броня {user.armor}')
    print(f'Здоровье противника: {enemy.health}, атака противника {enemy.attack}')
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
    userinput = input(
        '\nВыберите действие:\n1 - увеличить здоровье\n2 - атаковать\n')

    if userinput == '1':
        user.heal()
    if userinput == '2':
        enemy.be_attacked(user.attack)

    enemy.be_attacked(user.attack)  # мы атакуем врага
    user.be_attacked(enemy.attack)  # враг атакует нас
    print('Тебе нанесено', enemy.attack, 'урона')
