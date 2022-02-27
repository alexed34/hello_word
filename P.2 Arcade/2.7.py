import arcade
import random

# устанавливаем константы
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Шаблон"


class Penguin(arcade.AnimatedTimeSprite):
    def __init__(self):
        super(Penguin, self).__init__(1)
        self.textures.append(arcade.load_texture("img/7/penguin1.png"))
        self.textures.append(arcade.load_texture("img/7/penguin2.png"))
        self.textures.append(arcade.load_texture("img/7/penguin3.png"))

    def update(self):
        self.center_y += self.change_y
        self.angle += self.change_angle
        self.change_y -= 0.4
        if self.center_y < 0:
            self.center_y = 0
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = SCREEN_HEIGHT

        self.change_angle -= 0.4
        if self.angle >= 40:
            self.angle = 40
        if self.angle <= -30:
            self.angle = -30


class ColumnTop(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= 0:
            self.center_x = SCREEN_WIDTH
            self.center_y = random.randint(390, 480)


class ColumnBotton(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= 0:
            self.center_x = SCREEN_WIDTH
            self.center_y = random.randint(0, 70)
            window.score += 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture('img/7/space.png')
        self.penquin = Penguin()
        self.columns = arcade.SpriteList()
        self.score = 0
        self.stop = False

    # начальные значения
    def setup(self):
        self.penquin.center_x = 100
        self.penquin.center_y = 200
        # self.penquin.change_y = 0
        # self.penquin.change_angle = 0
        for i in range(5):
            column_top = ColumnTop("img/7/column_top.png", 1)
            column_top.center_x = 130 * i + SCREEN_WIDTH
            column_top.center_y = 400
            column_top.change_x = 4
            self.columns.append(column_top)

            column_botton = ColumnBotton("img/7/column_bottom.png", 1)
            column_botton.center_x = 130 * i + SCREEN_WIDTH
            column_botton.center_y = 70
            column_botton.change_x = 4
            self.columns.append(column_botton)

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.penquin.draw()
        self.columns.draw()

        arcade.draw_text(f"Счет:{self.score}", 30, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)


    # игровая логика
    def update(self, delta_time):
        self.penquin.update_animation()
        self.penquin.update()
        self.columns.update()

        hit_list = arcade.check_for_collision_with_list(self.penquin, self.columns)

        if len(hit_list) > 0:
            self.penquin.stop()
            for column in self.columns:
                column.stop()
                self.stop = True

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.stop == False:
            self.penquin.change_y = 7
            self.penquin.change_angle = 3



window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
