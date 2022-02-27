import arcade
import random

# устанавливаем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Гонки с препятствиями"


class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.left < 50:
            self.left = 50
        if self.right > SCREEN_WIDTH - 50:
            self.right = SCREEN_WIDTH - 50


class Wall(arcade.Sprite):
    def update(self):
        self.center_y -= self.change_y

        if self.center_y < -10:
            self.center_y = SCREEN_HEIGHT
            self.center_x = random.randint(130, SCREEN_WIDTH - 130)


# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("img/background.png")
        self.car = Car("img/car.png", 0.6)
        self.wall = Wall("img/wall.png", 0.3)
        self.wall2 = Wall("img/wall.png", 0.3)

        self.score = 0

    # начальные значения
    def setup(self):
        self.car.center_x = SCREEN_WIDTH / 2
        self.car.center_y = 100
        self.wall.center_x = SCREEN_WIDTH / 2  # ДЗ self.wall.center_x = random.randint(130, SCREEN_WIDTH - 130)
        self.wall.center_y = SCREEN_HEIGHT
        self.wall.change_y = 5
        self.wall2.center_x = random.randint(130, SCREEN_WIDTH - 130)
        self.wall2.center_y = SCREEN_HEIGHT+300
        self.wall2.change_y = 5

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.car.draw()
        self.wall.draw()
        self.wall2.draw()
        score_text = f"Счет: {self.score}"
        arcade.draw_text(score_text, 100, 560, arcade.color.RED, 20)

        '''
        if self.score == 15:
            arcade.draw_text("Победа", 240, 260, arcade.color.RED, 60)
        '''

    # игровая логика
    def update(self, delta_time):
        self.car.update()
        self.wall.update()
        self.wall2.update()

        if arcade.check_for_collision(self.wall, self.car):
            self.car.stop()
            self.wall.stop()
            self.wall2.stop()
        if self.score% 10 == 0:
            self.wall.change_y = 5 + self.score//10
            self.wall2.change_y = 5 + self.score//10
        print(self.wall.change_y)

        # if arcade.check_for_collision(self.wall2, self.car):
        #     self.car.stop()
        #     self.wall.stop()
            # self.wall2.stop()


        #
        # if self.wall.center_y <= 0 or self.wall2.center_y <= 0 :
        #     self.score += 1
        if self.wall.center_y <= 0 or self.wall2.center_y <= 0 :
            self.score += 1


        '''
        if self.score == 15:
            self.car.stop()
            self.wall.center_y = SCREEN_HEIGHT
            self.wall.stop()
        '''

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.car.change_x = 5
            self.car.angle = -20
        if key == arcade.key.LEFT:
            self.car.change_x = -5
            self.car.angle = 20


    # отпустить клавишу
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.car.change_x = 0
            self.car.angle = 0




window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
