import arcade
import time
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Plants VS Zombies"


def lawn_x(x):  # определяем лужайку по оси x
    if 250 < x <= 326:
        column = 1
        center_x = 283
    elif 326 < x <= 400:
        column = 2
        center_x = 360
    elif 400 < x <= 485:
        column = 3
        center_x = 440
    elif 485 < x <= 560:
        column = 4
        center_x = 520
    elif 560 < x <= 640:
        column = 5
        center_x = 600
    elif 640 < x <= 715:
        column = 6
        center_x = 675
    elif 715 < x <= 785:
        column = 7
        center_x = 750
    elif 785 < x <= 870:
        column = 8
        center_x = 830
    elif 870 < x <= 960:
        column = 9
        center_x = 915
    return center_x, column  # возвращаем центр лужайки и номер столбца


def lawn_y(y):  # определяем лужайку по оси x
    if 29 < y <= 130:
        line = 1
        center_y = 80
    elif 130 < y <= 220:
        line = 2
        center_y = 170
    elif 220 < y <= 323:
        line = 3
        center_y = 270
    elif 323 < y <= 424:
        line = 4
        center_y = 370
    elif 424 < y <= 527:
       line = 5
       center_y = 470
    return center_y, line  # возвращаем центр лужайки и номер линии


class Plant(arcade.AnimatedTimeSprite):  # базовый класс Растений
    def __init__(self, health, cost):  # жизнь, цена - общие характеристики для всех растений
        super().__init__(0.12)
        self.health = health
        self.cost = cost
        self.line = 0  # номер линии, изначально нулевой, будет определяться в процессе игры
        self.column = 0  # номер столбца, изначально нулевой, будет определяться в процессе игры

    def plant(self, center_x, center_y, line, column):  # посадка растения
        self.center_x = center_x
        self.center_y = center_y
        self.line = line
        self.column = column

    def update(self):  # логика
        if self.health <= 0:  # если здоровье кончилось
            self.kill()  # удаляем растение
            window.lawns.remove((self.line, self.column))  # убираем "адрес" лужайки из списка занятых лужаек


class SunFlower(Plant):  # класс Подсолнух
    def __init__(self):
        super().__init__(health=80, cost=50)
        self.texture = arcade.load_texture("sun1.png")
        for i in range(3):
            self.textures.append(arcade.load_texture("sun1.png"))
        for i in range(3):
            self.textures.append(arcade.load_texture("sun2.png"))
        self.sun_spawn = time.time()  # время появления солнышка

    def update(self):
        super().update()  # используем логику родительского класса
        if time.time() - self.sun_spawn >= 15:  # если после последнего появляения солнышка прошло 15 секунд
            sun = Sun(self.center_x + 20, self.center_y + 30)  # создаем солнышко
            window.spawns_suns.append(sun)  # добавляем солнышко в список игрового класса
            self.sun_spawn = time.time()  # обновляем время появления солнышка, пока задаем текущее время


class Sun(arcade.Sprite):  # класс Солнышко
    def __init__(self, position_x, position_y):
        super().__init__("sun.png", 0.12)
        self.center_x = position_x
        self.center_y = position_y

    def update(self):
        self.angle += 1  # вращаем солнышко


class PeaShooter(Plant):  # класс Горохострел
    def __init__(self):
        super().__init__(health=100, cost=100)
        self.texture = arcade.load_texture("pea1.png")
        for i in range(2):
            self.textures.append(arcade.load_texture("pea1.png"))
        for i in range(2):
            self.textures.append(arcade.load_texture("pea2.png"))
        for i in range(2):
            self.textures.append(arcade.load_texture("pea3.png"))
        self.pea_spawn = time.time()  # время выпуска горошины, пока задаем текущее время

    def update(self):
        super().update()
        zombie_on_line = False  # нет зомби на линии
        for zombie in window.zombies:  # проверка для всех зомби
            if zombie.line == self.line:  # если линии зомби и растения совпадают
                zombie_on_line = True  # зомби на линии
        if time.time() - self.pea_spawn >= 2 and zombie_on_line:  # если после послденего выпуска горошины прошло 2 секунды и зомби на горизонте
            print("Pea!")
            pea = Pea(self.center_x + 10, self.center_y + 10)  # создаем горошину
            window.peas.append(pea)  # добавляем горошину в список игрового окна
            self.pea_spawn = time.time()  # обновляем вермя последнего выпуска пули
            arcade.play_sound(arcade.load_sound('peaspawn.mp3'))


class Pea(arcade.Sprite):  # класс Горошина
    def __init__(self, position_x, position_y):
        super().__init__("bul.png", 0.12)
        self.center_x = position_x
        self.center_y = position_y
        self.damage = 5  # урон
        self.change_x = 7  # скорость полета

    def update(self):
        self.center_x += self.change_x
        if self.center_x > SCREEN_WIDTH:  # если вылетела за экрна
            self.kill()  # удаляем горошину

        hits = arcade.check_for_collision_with_list(self,window.zombies)  # столкновение горошины с зомби
        if len(hits) > 0:  # если список не пустой, горошина попала в зомби
            for zombie in hits:  # для каждого зомби, пораженного горошиной
                zombie.health -= self.damage  # нанести урон здоровье зомби
                self.kill()  # удаляем горошину


class WallNut(Plant):
    def __init__(self):
        super().__init__(health=200, cost=50)
        self.texture = arcade.load_texture("nut1.png")
        for i in range(10):
            self.textures.append(arcade.load_texture("nut1.png"))
        self.textures.append(arcade.load_texture("nut2.png"))
        for i in range(2):
            self.textures.append(arcade.load_texture("nut3.png"))
        self.textures.append(arcade.load_texture("nut2.png"))


class Torchwood(Plant):  # класс Древофакел
    def __init__(self):
        super().__init__(health=120, cost=175)
        self.texture = arcade.load_texture("tree1.png")
        for i in range(2):
            self.textures.append(arcade.load_texture("tree1.png"))
        for i in range(2):
            self.textures.append(arcade.load_texture("tree2.png"))
        for i in range(2):
            self.textures.append(arcade.load_texture("tree3.png"))

    def update(self):
        super().update()
        fire_peas = arcade.check_for_collision_with_list(self, window.peas)  # горошины, пролетевшие через древофакел
        for pea in fire_peas:  #  для каждой пролетевшей горошины
            pea.texture = arcade.load_texture("firebul.png")  # заменяем на огненную
            pea.damage = 3  # урон горящей пули больше


class Zombie(arcade.AnimatedTimeSprite):  # базовый класс Зомби
    def __init__(self, health, line):  # общие характеристики - здоровье, линия
        super().__init__(0.09)
        self.health = health
        self.line = line
        self.center_x = SCREEN_WIDTH
        self.change_x = 0.2  # скорость передвижения

    def update(self):
        self.center_x -= self.change_x  # движется справа налево
        if self.health <= 0:  # если здоровье кончилось
            self.kill()  # удаялем зомби
            window.killed_zombies += 1  # плюс к побежденным зомби
            window.attack_time -= 1  # сокращаем время между появлением зомби

        eating = False # зомби не есть
        food = arcade.check_for_collision_with_list(self, window.plants)  # список растений, касающихся зомби
        for plant in food:  # для всех растений, касающихся зомби
            if self.line == plant.line:  # если растение на пути зомби
                plant.health -= 0.5  # отнимаем жизнь у растения
                eating = True  # зомби ест
        if eating:  # если зомби ест
            self.change_x = 0  # останавливаем зомби
            self.angle = 15  # наклоняемся
        else:  # если зомби не ест
            self.change_x = 0.2  # идем дальше
            self.angle = 0  # выпрямляемся

        if self.center_x < 200:  # если зомби дошел до дома
            window.game = False  # конец игры


class OrdinaryZombie(Zombie):  # класс Обычный Зомби
    def __init__(self, line):
        super().__init__(health=12, line=line)
        self.texture = arcade.load_texture("zom1.png")
        for i in range(5):
            self.textures.append(arcade.load_texture("zom1.png"))
        self.textures.append(arcade.load_texture("zom2.png"))


class ConehaedZombie(Zombie):  # класс Зомби с конусом
    def __init__(self, line):
        super().__init__(health=20, line=line)
        self.texture = arcade.load_texture("cone1.png")
        for i in range(5):
            self.textures.append(arcade.load_texture("cone1.png"))
        self.textures.append(arcade.load_texture("cone2.png"))


class BuckheadZombie(Zombie):  # класс Зомби с ведром
    def __init__(self, line):
        super().__init__(health=32, line=line)
        self.texture = arcade.load_texture("buck1.png")
        for i in range(5):
            self.textures.append(arcade.load_texture("buck1.png"))
        self.textures.append(arcade.load_texture("buck2.png"))

class MyGame(arcade.Window):  # класс Игрового окна
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.back = arcade.load_texture("background.jpg")  # фон
        self.menu = arcade.load_texture("menu_vertical.png")  # меню
        self.end_game = arcade.load_texture("end.png") # заставка завершения игры
        self.game = True   # состояние игры
        self.plants = arcade.SpriteList()   # список посаженных растений
        self.seed = None   # саженец
        self.lawns = []  # список засаженных лужаек
        self.sun = 300  # солнышки
        self.spawns_suns = arcade.SpriteList()  # список солнышек
        self.peas = arcade.SpriteList()  # список горошин
        self.zombies = arcade.SpriteList()  # список зомби
        self.zombie_spawn = time.time()  # время появления зомби
        self.killed_zombies = 0  # количество убитых зомби
        self.attack_time = 20  # время между появлением зомби, изначально 20 секунд

    # начальные значения
    def setup(self):
        self.music = arcade.load_sound("grasswalk.mp3")
        arcade.play_sound(self.music)

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.back)
        arcade.draw_texture_rectangle(60, 300, 130, 600, self.menu)
        arcade.draw_text(f"{self.sun}", 30, 490, arcade.color.BROWN, 30)
        self.plants.draw()
        if self.seed != None:
            self.seed.draw()
        self.spawns_suns.draw()
        self.peas.draw()
        self.zombies.draw()
        if self.game == False: # если конец игры
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 600, 400, self.end_game)  # отрисовка картинки конца игры

    # игровая логика
    def update(self, delta_time):
        if self.game:  # если идет игра
            self.plants.update_animation()
            self.plants.update()
            self.spawns_suns.update()
            self.peas.update()
            self.zombies.update()
            self.zombies.update_animation()

            if time.time() - self.zombie_spawn > self.attack_time and self.killed_zombies < 20:  # если со времени последней атаки прошло достаточно времени и еще не убито 20 зомби
                center_y, line = lawn_y(random.randint(30, 520))  # выбираем случайную линию и координату по высоте
                zombie_type = random.randint(1, 3)  # случайный тип зомби
                if zombie_type == 1:
                    zombie = OrdinaryZombie(line)
                elif zombie_type == 2:
                    zombie = ConehaedZombie(line)
                else:
                    zombie = BuckheadZombie(line)
                zombie.center_y = center_y
                self.zombies.append(zombie)  # добавляем зомби в список
                self.zombie_spawn = time.time()  # обновляем время появления зомби

            if self.killed_zombies >= 20 and len(self.zombies) == 0:  # если победили больше 20 зомби и больше зомби не осталось
                self.end_game = arcade.load_texture("logo.png")  # загружаем победную картинку
                self.game = False  # конец игры

    # нажать кнопку мыши
    def on_mouse_press(self, x, y, button, modifiers):
        if self.game:  # если идет игра
            # проверка нажати на область меню
            if 10 < x < 110 and 370 < y < 480:
                print("SunFlower")
                self.seed = SunFlower()  # саженец подсолнуха
            if 10 < x < 110 and 255 < y < 365:
                print("PeaShooter")
                self.seed = PeaShooter()  # саженец горохострела
            if 10 < x < 110 and 140 < y < 250:
                print("WallNut")
                self.seed = WallNut()  # саженец стенореха
            if 10 < x < 110 and 25 < y < 135:
                print("Torchwood")
                self.seed = Torchwood()  # саженец древофакела

            if self.seed != None:  # если есть саженец
                self.seed.center_x = x  # саженец там где курсор
                self.seed.center_y = y  # саженец там где курсор
                self.seed.alpha = 150  # делаем изображение прозрачным
            for sun in self.spawns_suns:  # для каждого выпавшего солнышка
                if sun.left < x < sun.right and sun.bottom < y < sun.top:  # если на выпавшее солнышко нажали
                    sun.kill()  # удаляем выпавшее солнышко
                    self.sun += 25  # прибавляем солнышки к счету

    # движение мыши
    def on_mouse_motion(self, x, y, dx, dy):
        if self.seed != None:  # если есть саженец
            self.seed.center_x = x  # саженец там где курсор
            self.seed.center_y = y  # саженец там где курсор

    # отпустить кнопку мыши
    def on_mouse_release(self, x, y, button, modifiers):
        if self.seed is not None and 250 < x < 960 and 30 < y < 526:  # если есть саженец и курсор в области лужаек
            center_x, column = lawn_x(x)  # получаем значения лужайки по оси х, на которой находится курсор - ее центр и номер
            center_y, line = lawn_y(y)  # получаем значения лужайки по оси у, на которой находится курсор - ее центр и номер
            cost = self.seed.cost  # определяем стоимость покупки
            if (line, column) not in self.lawns and self.sun >= cost:  # если выбранная лужайка не занята и хватает солнышек на покупку
                self.sun -= cost  # тратим солнышки
                self.lawns.append((line, column))  # добавляем лужайку в список занятых
                self.seed.plant(center_x, center_y, line, column)  # сажаем растение
                self.seed.alpha = 255  # убираем прозрачность
                self.plants.append(self.seed)  # добавляем растение в список растений
                self.seed = None  # удаляем саженец
        elif self.seed is not None and 0 < x < 130:  # если есть саженец и курсор в области меню
            self.seed = None  # сбрасываем саженец


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
