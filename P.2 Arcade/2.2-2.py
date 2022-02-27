import arcade

# задаем ширину, высоту и заголовок окна
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Анимация квадратов"


class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_x1 = 300
        self.center_y1 = 300
        self.center_x2 = 300
        self.center_y2 = 300

        self.side1 = 80
        self.side2 = 80

        self.change_x = 5
        self.change_y = 5

        # self.color1 = arcade.color.BLACK #ДЗ
        # self.color2 = arcade.color.PURPLE #ДЗ

    # отрисовка объектов
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_rectangle_filled(self.center_x1, self.center_y1, self.side1, self.side1, arcade.color.BLACK)
        #arcade.draw_rectangle_filled(self.center_x1, self.center_y1, self.side1, self.side1, self.color1) #ДЗ
        arcade.draw_rectangle_outline(self.center_x2, self.center_y2, self.side2, self.side2, arcade.color.PURPLE, 5)
        #arcade.draw_rectangle_outline(self.center_x2, self.center_y2, self.side2, self.side2, self.color2, 5) #ДЗ

    # логика
    def update(self, delta_time):
        self.center_x1 += self.change_x
        if self.center_x1 + self.side1/2 > SCREEN_WIDTH or self.center_x1 - self.side1/2 < 0:
            self.change_x = -self.change_x
            #self.color1 = arcade.color.SILVER #ДЗ

        self.center_y2 += self.change_y
        if self.center_y2 + self.side2/2 > SCREEN_HEIGHT or self.center_y2 - self.side2/2 < 0:
            self.change_y = -self.change_y
            #self.color2 = arcade.color.BLUE #ДЗ

        ''' ДЗ
        if self.center_x1 == self.center_x2 and self.center_y1 == self.center_y2:
            self.color1 = arcade.color.BLACK
            self.color2 = arcade.color.PURPLE
        '''


game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
