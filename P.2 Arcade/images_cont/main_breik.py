import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Air Balloons'


class Cross(arcade.Sprite):
    def __init__(self):
        super().__init__("cross.png", 0.5)

        self.center_x = window.width / 2
        self.center_y = window.height / 2

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class Balloon(arcade.Sprite):
    def __init__(self):
        super().__init__("balloon.png", 0.5)

        self.center_x = random.randint(0, window.width)
        self.top = 0

    def update(self):
        self.center_y += self.change_y

        if self.top >= window.height:
            self.kill()
            window.lives += 1


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.balloons = arcade.SpriteList()
        self.cross = None

        self.score = 0
        self.lives = 100
        self.speed = 2 #200
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

        arcade.draw_text('Score: {self.score}', 110, self.height - 140, arcade.color.BLACK, font_size=100)
        arcade.draw_text('Lives: {self.lives}', self.width - 120, self.height - 40, arcade.color.BLACK, font_size=30)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LSHIFT:
            if self.status:
                hits = arcade.check_for_collision_with_list(self.cross, self.balloons)
                for balloon in hits:
                    balloon.kill()
                    self.score -= 1

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
            self.cross.change_y = 0
        if key == arcade.key.DOWN:
            self.cross.change_y = -4
        if key == arcade.key.RIGHT:
            self.cross.change_x = 0
        if key == arcade.key.LEFT:
            self.cross.change_x = 4

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.cross.change_y = 5
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.cross.change_x = 5


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
