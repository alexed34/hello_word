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

    def planting(self, center_x, center_y, line, column):  # посадка растения
        self.center_x = center_x
        self.center_y = center_y
        self.line = line
        self.column = column

    def update(self):  # логика
        if self.health <= 0:  # если здоровье кончилось
            self.kill()  # удаляем растение

class SunFlower(Plant):
    def __init__(self):
        super().__init__(health=80, cost=50)
        self.texture = arcade.load_texture("sun1.png")
        for i in range(3):
            self.textures.append(arcade.load_texture("sun1.png"))
        for i in range(3):
            self.textures.append(arcade.load_texture("sun2.png"))

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game = True
        self.back = arcade.load_texture("background.jpg")
        self.menu = arcade.load_texture("menu_vertical.png")
        self.game = True  # состояние игры
        self.plants = arcade.SpriteList()  # список посаженных растений
        self.seed = None  # саженец
        self.lawns = []  # список засаженных лужаек

        # начальные значения
    def setup(self):
        pass

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.back)
        arcade.draw_texture_rectangle(60, 300, 130, 600, self.menu)

        self.plants.draw()
        if self.seed != None:
            self.seed.draw()

    # игровая логика
    def update(self, delta_time):
        if self.game:
            self.plants.update_animation()
            self.plants.update()

    # нажатить кнопку мыши
    def on_mouse_press(self, x, y, button, modifiers):
        if self.game:
            if 10 < x < 110 and 370 < y < 480:
                print("SunFlower") # саженец подсолнуха
                self.seed = SunFlower()
            if 10 < x < 110 and 255 < y < 365:
                print("PeaShooter")
            if 10 < x < 110 and 140 < y < 250:
                print("WallNut")
            if 10 < x < 110 and 25 < y < 135:
                print("Torchwood")

            if self.seed != None:  # если есть саженец
                self.seed.center_x = x  # саженец там где курсор
                self.seed.center_y = y  # саженец там где курсор
                self.seed.alpha = 150  # делаем изображение прозрачным

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
            if (line, column) not in self.lawns:  # если выбранная лужайка не занята
                self.lawns.append((line, column))  # добавляем лужайку в список занятых
                self.seed.planting(center_x, center_y, line, column)  # сажаем растение
                self.seed.alpha = 255  # убираем прозрачность
                self.plants.append(self.seed)  # добавляем растение в список растений
                self.seed = None  # удаляем саженец


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
