import random

import arcade

WIDTH = 800
HEIGHT = 600
TITLE = "Star wars"


class Enemy(arcade.AnimatedTimeSprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.textures.append("arcade_8/tie fighter.png")
        self.textures.append("arcade_8/tie fighter2.png")
        self.change_y = 1

    def update(self):
        self.center_y -= self.change_y

class Bullet(arcade.Sprite):
    def __init__(self):
        super(Bullet, self).__init__("arcade_8/laser.png")
        self.change_y = 5
        self.laser_sound = arcade.load_sound("arcade_8/laser.wav")

    def update(self):
        self.center_y += self.change_y
        if self.center_y >= HEIGHT:
            self.kill()

class Space_ship(arcade.Sprite):
    def update(self):
        if self.right >= 800:
            self.right = 800
        if self.left <= 0:
            self.left = 0

class Our_game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.background = arcade.load_texture("arcade_8/space_background.png")
        self.space_ship = Space_ship("arcade_8/x-wing.png", 0.5)
        self.bullets = arcade.SpriteList()
        self.enemys = arcade.SpriteList()

    def setup(self):
        self.space_ship.center_x = 400
        self.space_ship.center_y = 50
        for i in range(50):
            enemy = Enemy()
            enemy.center_x = random.randint(0, 800)
            enemy.center_y = 600
            self.enemys.append(enemy)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(400,300, WIDTH, HEIGHT,self.background)
        self.space_ship.draw()
        self.bullets.draw()
        self.enemys.draw()

    def update(self, delta_time):
        self.space_ship.update()
        self.bullets.update()
        # self.enemys.update_animation()
        self.enemys.update()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.space_ship.center_x = x

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        bullet = Bullet()
        bullet.center_x = self.space_ship.center_x
        bullet.bottom = self.space_ship.top
        self.bullets.append(bullet)
        arcade.play_sound(bullet.laser_sound)


window = Our_game()
window.setup()
arcade.run()
