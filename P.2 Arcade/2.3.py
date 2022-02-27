import arcade

# устанавливаем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Играем в пинг понг"


# объявляем класс с игрой
class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('img/ball.png', 0.7)
        self.bar = Bar('img/bar.png', 0.5)
        arcade.set_background_color(arcade.color.AMAZON)
        self.score = 0
        self.attempts = 3

    def setup(self):
        self.ball.center_x = 300
        self.ball.center_y = 300
        self.ball.change_y = -5
        self.ball.change_x = 5
        self.bar.center_x = 300
        self.bar.center_y = 20
        self.bar.change_x = 0
        self.ball.alpha = 150

    # здесь вызываются методы для отрисовки
    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        self.bar.draw()
        text_score = f'Счет {self.score}'
        arcade.draw_text(text_score, 10, 570, arcade.color.BLACK,20)
        text_attempts = f'Проигрыш {self.attempts}'
        arcade.draw_text(text_attempts, 10, 550, arcade.color.BLACK,20)


    # игровая логика будет здесь
    def update(self, delta_time):
        self.ball.update()
        self.bar.update()
        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.bottom = self.bar.top
            self.ball.change_y = -self.ball.change_y
            self.score += 1
        if self.ball.bottom <= 0:
            self.attempts -= 1
            self.ball.center_y = 500
        if self.attempts == 0:
            self.ball.stop()
            self.bar.stop()

    def on_key_press(self, key, modifieres):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifieres):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x = - self.change_x
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.left < 0:
            self.left = 0
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH


window = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()

arcade.run()
