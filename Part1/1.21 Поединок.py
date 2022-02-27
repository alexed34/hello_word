import random


class Enemy:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def be_attacked(self, attack):  # нанесение урона в размере attack
        self.health = self.health - attack  # уменьшение здоровья



enemy = Enemy(health=330, attack=10)
enemy_2 = Enemy(health=330, attack=10)
# enemy.be_attacked(10)
print(enemy.health, enemy_2.health)

hits = 0
# win = False # проверка на победу
while True:
    if enemy.health <= 0 and enemy_2.health <= 0:  # если здоровье обоих  стало <= 0
        print('Ничья')
        break
        # win = True
    elif enemy.health <= 0:  # если здоровье 1 врага <= 0
        print('Второй победил')
        print("У него осталось здоровья", enemy_2.health)
        break
        # win = True
    elif enemy_2.health <= 0:  # если здоровье 2 врага <= 0
        print('Первый победил')
        print("У него осталось здоровья", enemy.health)
        break
        # win = True

    # if win is True:  # победа, это уже другой блок условий
    #     print('Ударов совершено', hits)
    #     break
    enemy.be_attacked(enemy_2.attack)
    enemy_2.be_attacked(enemy.attack)
    hits += 1
    enemy_2.attack = random.randint(1,20)
    enemy.attack = random.randint(1,20)
    print(enemy.health, enemy_2.health)
print(hits, enemy.health, enemy_2.health)