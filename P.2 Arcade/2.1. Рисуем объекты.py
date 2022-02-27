import arcade
import random

class OurPicture(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        arcade.draw_circle_filled(300, 300, 200, arcade.color.YELLOW)
        arcade.draw_circle_filled(380, 350, 20, arcade.color.BLACK)
        arcade.draw_circle_filled(220, 350, 20, arcade.color.BLACK)
        center_x = 300
        center_y = 230
        width = 150
        height = 200
        start_angle = 0
        end_angle = 180
        line_width = 30
        arcade.draw_arc_outline(center_x, center_y, width, height,
                                arcade.color.BLACK, start_angle, end_angle,
                                line_width)

class Landscape(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def bird(self, x, y):
        arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)  # левое крыло
        arcade.draw_arc_outline(x + 20, y, 20, 20, arcade.color.BLACK, 90, 180)  # правое крыло

    def tree(self, x, y):
        arcade.draw_rectangle_filled(x, y, 20, 90, arcade.color.DARK_BROWN)
        arcade.draw_circle_filled(x, y + 40, 40, arcade.color.DARK_GREEN)


    def house(self, x, y):
        arcade.draw_rectangle_filled(x, y, 100, 80, arcade.color.CORN)  # стена
        arcade.draw_rectangle_filled(x, y, 30, 30, arcade.color.LIGHT_BLUE)  # окно
        arcade.draw_triangle_filled(x1=x, y1=y+80, x2=x-50, y2=y+40, x3=x+50, y3=y+40, color=arcade.color.RED_BROWN)  # крыша

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BABY_BLUE)
        arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.color.GREEN)
        arcade.draw_circle_filled(100, 350, 20, arcade.color.YELLOW)

        self.bird(300, 300)
        self.bird(400, 350)
        self.tree(500, 120)
        self.tree(120, 100)
        self.house(330, 125)
landscape = Landscape(600, 400, "Пейзаж")

# window = OurPicture(600,600,"Смайлик")

arcade.run()