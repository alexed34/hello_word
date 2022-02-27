import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Air Balloons'

# план
# создать прицел посередине
# прицел перемещается клавишами с стрелками нажатое состояние перемещается, отпускаем останавливается
# создать балон появляются снизу и идут вверх долетают до верха исчезают, жизнь уменьшается.
# жизни 3
# появление болонов реалиховать с частотностью 200
# игра перемещать курсор и стрелять по баллонам кнопкой пробел
# и ускорять балоны с четными очками скорость и частоту появления





class Cross(arcade.Sprite):
    def __init__(self):
        super().__init__("../P.2 Arcade/img/cross.png", 0.5)

        self.center_x = window.width / 2
        self.center_y = window.height / 2

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class Balloon(arcade.Sprite):
    def __init__(self):
        super().__init__("../P.2 Arcade/img/balloon.png", 0.5)

        self.center_x = random.randint(0, window.width)
        self.top = 0

    def update(self):
        self.center_y += self.change_y

        if self.top >= window.height:
            self.kill()
            window.lives -= 1


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.balloons = arcade.SpriteList()
        # self.cross = None

        self.score = 0
        self.lives = 3
        self.speed = 0.5
        self.frequency = 200

        self.status = True

    def setup(self):
        self.cross = Cross()

    def update(self, delta_time):
        if self.status:
            self.balloons.update()
            self.cross.update()

            if random.randint(0, self.frequency) == self.frequency:
                balloon = Balloon()
                balloon.change_y = self.speed
                self.balloons.append(balloon)
            if self.lives <= 0:
                self.status = False

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)

        self.balloons.draw()
        self.cross.draw()

        arcade.draw_text(f'Score: {self.score}', 10, self.height - 40, arcade.color.BLACK, font_size=30)
        arcade.draw_text(f'Lives: {self.lives}', self.width - 120, self.height - 40, arcade.color.BLACK, font_size=30)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if self.status:
                hits = arcade.check_for_collision_with_list(self.cross, self.balloons)
                for balloon in hits:
                    balloon.kill()
                    self.score += 1

                    if self.score % 2 == 0:
                        self.speed += 0.01
                        self.frequency -= 1
            else:
                for balloon in self.balloons:
                    balloon.kill()

                self.score = 0
                self.speed = 0.5
                self.frequency = 200

                self.status = True

        if key == arcade.key.ESCAPE:
            window.close()

        if key == arcade.key.UP:
            self.cross.change_y = 2
        if key == arcade.key.DOWN:
            self.cross.change_y = -2
        if key == arcade.key.RIGHT:
            self.cross.change_x = 2
        if key == arcade.key.LEFT:
            self.cross.change_x = -2

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.cross.change_y = 0
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.cross.change_x = 0


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
