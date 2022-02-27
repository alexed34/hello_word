import arcade
import random

# устанавливаем константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Динозаврик"


class Cactus(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= 0:
            self.center_x = SCREEN_WIDTH
            game.score += 1
            self.change_x = random.randint(4, 12)


class Duno(arcade.AnimatedTimeSprite):
    def update(self):
        self.center_y += self.change_y
        self.change_y -= 0.5

        if self.center_y <= 200:
            self.center_y = 200
            self.jump = False


class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture('img/desert.png')
        self.duno = Duno(0.5)
        self.duno.textures = [arcade.load_texture('img/dino1.png'), arcade.load_texture('img/dino2.png'),
                              arcade.load_texture('img/dino3.png')]
        # self.duno.textures.append(arcade.load_texture('img/dino1.png'))
        # self.duno.textures.append(arcade.load_texture('img/dino2.png'))
        # self.duno.textures.append(arcade.load_texture('img/dino3.png'))
        self.cactus = Cactus('img/cactus2.png', 0.5)
        self.score = 0

    # начальные значения
    def setup(self):
        self.duno.center_x = 100
        self.duno.center_y = 200
        self.cactus.center_x = SCREEN_WIDTH
        self.cactus.center_y = 200
        self.cactus.change_x = 4

    # отрисовка обьектов
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.duno.draw()
        self.cactus.draw()
        score_text = f"Счет: {self.score}"
        arcade.draw_text(score_text, 330, 550, arcade.color.BLACK, 30)

        # логика

    def update(self, delta_time: float):
        self.duno.update_animation()
        self.duno.update()
        self.cactus.update()
        if arcade.check_for_collision(self.duno, self.cactus):
            self.duno.stop()
            self.cactus.stop()
        # if self.cactus.center_x <= 0:
        #     self.cactus.center_x = SCREEN_WIDTH
        #     self.score +=1

    # нажать на клавишу
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE and self.duno.jump == False:
            self.duno.change_y = 12
            self.duno.jump = True

    # отпустить клавишу
    def on_key_release(self, symbol: int, modifiers: int):
        pass


game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
