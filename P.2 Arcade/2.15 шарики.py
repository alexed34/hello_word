import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Circle Game'


class Circle(arcade.Sprite):
    def __init__(self, scale):
        super().__init__('circle.png', scale)

        self.side = random.choice(['left', 'top', 'right', 'bottom'])
        self.color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))

        if self.side == 'left':
            self.right = 0
            self.center_y = random.randint(0, window.height)

            self.change_x = random.uniform(2, 5)
            self.change_y = random.uniform(-3, -2)

        elif self.side == 'top':
            self.bottom = window.height
            self.center_x = random.randint(0, window.width)

            self.change_y = random.uniform(-5, -2)
            self.change_x = random.uniform(-3, -2)

        elif self.side == 'right':
            self.left = window.width
            self.center_y = random.randint(0, window.height)

            self.change_x = random.uniform(-3, -2)
            self.change_y = random.uniform(-3, -2)

        else:
            self.top = 0
            self.center_x = random.randint(0, window.width)

            self.change_y = random.uniform(2, 3)
            self.change_x = random.uniform(-3, -2)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.side == 'left':
            if self.left >= window.width or self.top <= 0 or self.bottom >= window.height:
                self.kill()
        elif self.side == 'top':
            if self.top <= 0 or self.left >= window.width or self.right <= 0:
                self.kill()
        elif self.side == 'right':
            if self.right <= 0 or self.top <= 0 or self.bottom >= window.height:
                self.kill()
        else:
            if self.bottom >= window.height or self.left >= window.width or self.right <= 0:
                self.kill()


class Player(Circle):
    def __init__(self):
        super().__init__(0.3)

        self.center_x = window.width / 2
        self.center_y = window.height / 2

        self.change_x = 0
        self.change_y = 0

        self.color = arcade.color.WHITE


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super(Game, self).__init__(width, height, title, fullscreen=True)

        self.player = None
        self.circles = arcade.SpriteList()

        self.sound = arcade.load_sound('Drip Drop.wav')

        self.is_pause = True
        self.is_game = True

        self.text = ""

    def setup(self):
        self.player = Player()
        for i in range(30):
            self.circles.append(Circle(random.uniform(0.1, self.player.scale + 0.5)))

        play = arcade.play_sound(self.sound, looping=True)
        self.sound.set_volume(0.1, play)

    def on_draw(self):
        arcade.start_render()
        self.circles.draw()
        self.player.draw()

        arcade.draw_text("Pause: Mouse click", 50, self.height - 50, arcade.color.WHITE)
        arcade.draw_text("Exit: Esc", self.width - 100, self.height - 50, arcade.color.WHITE)

        arcade.draw_text(self.text, (self.width / 2) - 200, self.height / 2, arcade.color.WHITE, 80)

    def update(self, delta_time: float):
        if not self.is_pause and self.is_game:
            # if self.sound.get_stream_position() == 0:
            #     self.play = arcade.play_sound(self.sound)
            #     self.sound.set_volume(0.1)

            while len(self.circles) < 30:
                self.circles.append(Circle(random.uniform(0.1, self.player.scale + 0.5)))

            collisions = arcade.check_for_collision_with_list(self.player, self.circles)
            if len(collisions) > 0:
                for circle in collisions:
                    if circle.scale > self.player.scale:
                        self.is_game = False
                        self.text = "You Loose! ;("
                    else:
                        circle.kill()
                        self.player.scale += 0.01

            if self.player.scale >= 2:
                self.is_game = False
                self.text = "You Win!"

            self.circles.update()
            self.player.update()

        if not self.is_game:
            self.player.kill()
            for circle in self.circles:
                circle.kill()

    def on_mouse_motion(self, x, y, dx, dy):
        if not self.is_pause:
            self.player.center_x = x
            self.player.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if self.is_game:
            if self.is_pause:
                self.is_pause = False
                self.set_mouse_visible(False)
                self.text = ""

            else:
                self.is_pause = True
                self.set_mouse_visible(True)
                self.text = "Pause"

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            window.close()


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, 'Circles')
window.setup()
arcade.run()
