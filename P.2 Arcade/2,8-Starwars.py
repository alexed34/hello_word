import random

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = "Starwars"


class SpaceShip(arcade.Sprite):
    def update(self):
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0


class Bullet(arcade.Sprite):
    def __init__(self):
        super().__init__("arcade_8/laser.png", 0.8)
        self.change_y = 5
        self.laser_sound = arcade.load_sound("arcade_8/laser.wav")

    def update(self):
        self.center_y += self.change_y
        if self.center_y > SCREEN_HEIGHT:
            self.kill()


class Enemy(arcade.AnimatedTimeSprite):
    def __init__(self):
        super().__init__()
        self.textures.append(arcade.load_texture("arcade_8/tie fighter.png"))
        self.textures.append(arcade.load_texture("arcade_8/tie fighter2.png"))
        self.change_y = 1

    def update(self):
        self.center_y -= self.change_y
        if self.center_y < 0:
            window.fails += 1
            self.kill()

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background = arcade.load_texture("arcade_8/space_background.png")

        self.space_ship = SpaceShip("arcade_8/x-wing.png", 0.5)
        self.set_mouse_visible(False)

        self.bullets = arcade.SpriteList()

        self.enemies = arcade.SpriteList()

        self.score = 0
        self.fails = 0

        # ДЗ self.soundtrack = arcade.load_sound("star_wars.wav")

        self.game_state = True
        self.label = " "

    def setup(self):
        self.space_ship.center_x = SCREEN_WIDTH / 2
        self.space_ship.center_y = 70

        for i in range(50):
            enemy = Enemy()
            enemy.center_x = random.randint(0, SCREEN_WIDTH)
            enemy.center_y = 50 * i + SCREEN_HEIGHT
            self.enemies.append(enemy)

        # ДЗ arcade.play_sound(self.soundtrack)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.space_ship.draw()
        self.bullets.draw()
        self.enemies.draw()

        arcade.draw_text(f"Счет: {self.score}", 10, 20, arcade.color.WHITE, 14)
        arcade.draw_text(f"Неудачи: {self.fails}", 710, 20, arcade.color.WHITE, 14)
        arcade.draw_text(self.label, 300, SCREEN_HEIGHT / 2, arcade.color.WHITE, 44)

    def update(self, delta_time):
        self.space_ship.update()
        self.bullets.update()

        for bullet in self.bullets:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemies)
            if len(hit_list) > 0:
                bullet.kill()
                for enemy in hit_list:
                    enemy.kill()
                    self.score += 1

        self.enemies.update_animation()
        self.enemies.update()

        if len(self.enemies) == 0 and self.fails <= 3:
            self.label = "Победа!"
            self.game_state = False

        if len(arcade.check_for_collision_with_list(self.space_ship, self.enemies)) > 0 or self.fails>3:
            self.label = "Поражение"
            self.game_state = False

        if self.game_state == False:
            # ДЗ arcade.stop_sound(self.soundtrack)
            self.space_ship.stop()
            for bullet in self.bullets:
                bullet.stop()
                bullet.kill()
            for enemy in self.enemies:
                enemy.stop()

    def on_mouse_motion(self, x, y, dx, dy):
        if self.game_state:
            self.space_ship.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        if self.game_state:
            bullet = Bullet()
            bullet.center_x = self.space_ship.center_x
            bullet.bottom = self.space_ship.top
            self.bullets.append(bullet)
            arcade.play_sound(bullet.laser_sound)
            # arcade.stop_sound(bullet.laser_sound)


window = MyGame()
window.setup()
arcade.run()
