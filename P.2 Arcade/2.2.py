import arcade
import random

# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Шаблон"

class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_x = 300
        self.center_y = 300
        self.radius = 50
        self.change_x = 2
        self.change_y = 3
        self.center_x1 = 300
        self.center_y1 = 300
        self.center_x2 = 350
        self.center_y2 = 350
        self.side1 = 60
        self.side2 = 60



        # отрисовка объектов
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius,
                                  arcade.color.BLUE)
        arcade.draw_rectangle_outline(self.center_x2, self.center_y2,
                                      self.side2, self.side2,
                                      arcade.color.RED, 5)
        arcade.draw_rectangle_outline(self.center_x1, self.center_y1,
                                      self.side2, self.side2,
                                      arcade.color.BABY_PINK, 5)

    # логика
    def update(self, delta_time):
        self.center_x += self.change_x
        if self.center_x + self.radius > SCREEN_WIDTH or self.center_x - \
                self.radius < 0:
            self.change_x = -self.change_x

        self.center_y += self.change_y
        if self.center_y + self.radius > SCREEN_WIDTH or self.center_y - \
                self.radius < 0:
            self.change_y = -self.change_y
        # self.center_x2 += self.change_x
        # if self.center_x2 + self.side2 / 2 > SCREEN_WIDTH or \
        #         self.center_x2 - self.side2 / 2 < 0:
        #     self.change_x = -self.change_x
        # self.center_y1 += self.change_y
        # if self.center_y1 + self.side1 / 2 > SCREEN_WIDTH or \
        #         self.center_y1 - self.side1 / 2 < 0:
        #     self.change_y = -self.change_y


game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()

