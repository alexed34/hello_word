import arcade
import random
from datetime import datetime


# константы
#
SCREEN_TITLE = "Minesweeper"  # название окна
ROW_COUNT = 7  # количество строк на игровом поле
COLUMN_COUNT = 7  # количество столбцов на игровом поле
CELL_WIDTH = 100  # ширина одной ячейки
CELL_HEIGHT = 100  # высота одной ячейки
MARGIN = 2  # толщина границы (то есть линий между ячейками)
# ширина и высота окна
SCREEN_WIDTH = (CELL_WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (CELL_HEIGHT + MARGIN) * ROW_COUNT + MARGIN
MINES_COUNT = 5  # количество мин на игровом поле
ATTEMPTS = 10  # число попыток


class Minesweeper(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.grid = []
        self.trophy = []
        self.mines_coordinates = []

    def setup(self):
        trophy_row = random.randint(0, ROW_COUNT - 1)
        trophy_column = random.randint(0, COLUMN_COUNT - 1)
        self.trophy = [trophy_row, trophy_column]
        mines = MINES_COUNT
        while mines > 0:
            row = random.randint(0, ROW_COUNT - 1)
            column = random.randint(0, COLUMN_COUNT - 1)
            if [row,column] not in self.mines_coordinates and [row,column] != self.trophy:
                self.mines_coordinates.append([row,column])
                mines -= 1
        print(self.mines_coordinates)



    def on_draw(self):
        """Отрисовка объектов"""
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                color = self.get_sell_color(row,column)
                x = (MARGIN+CELL_WIDTH) * column + MARGIN+CELL_WIDTH//2
                y = (MARGIN+CELL_HEIGHT) * row + MARGIN+CELL_HEIGHT//2
                arcade.draw_rectangle_filled(x,y, CELL_WIDTH, CELL_HEIGHT, color)
        print(datetime.now().strftime("%S - %f"))
        mines_exploded = MINES_COUNT - len(self.mines_coordinates)
        arcade.draw_text(f'Мины: {mines_exploded}', SCREEN_WIDTH//2-30, SCREEN_HEIGHT-30, arcade.color.WHITE,20)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        column = x // (CELL_WIDTH + MARGIN)
        row = y // (CELL_HEIGHT + MARGIN)
        if [row,column] in self.mines_coordinates:
            self.grid[row][column] = 1
            self.mines_coordinates.remove([row,column])
        if [row,column] == self.trophy:
            self.grid[row][column] = 4
        if self.grid[row][column] == 0:
            self.grid[row][column] = 3

    def on_mouse_motion(self, x, y, dx, dy):
        """
            Эта функция вызывается каждый раз при движении мышки
        """
        # см. док-стринг у метода выше
        mouse_column = x // (CELL_WIDTH + MARGIN)
        mouse_row = y // (CELL_HEIGHT + MARGIN)

        # эта проверка нужна, чтобы не было ошибки
        # так как мышка может выходить на границы окна
        if mouse_column < COLUMN_COUNT and mouse_row < ROW_COUNT:
            # если клетка на которой находится мышка в
            # состоянии 0 (на клетку можно кликнуть),
            # то меняем состояние клетки на 3 (клетка,
            # на которой находится мышка)
            if self.grid[mouse_row][mouse_column] == 0:
                self.grid[mouse_row][mouse_column] = 3

            # этот цикл нужен, чтобы создать
            # ощущение перемещения мышки по клеткам
            # клетки, на которых побывала мышка,
            # перекрашиваются обратно в изначальные цвета
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    if self.check_mouse_position(mouse_row, mouse_column, row, column):
                        self.grid[row][column] = 0

    def check_mouse_position(self, mouse_row, mouse_column, row, column):
        """
            Проверяет, что на клетке с состоянием 3 мышки нет
        """
        if row != mouse_row or column != mouse_column:
            if self.grid[row][column] == 3:
                return True





    def setup_gird(self):
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)
        print(self.grid)


    def get_sell_color(self, row,collumn):
        if self.grid[row][collumn] == 0:
            color = arcade.color.LIGHT_BLUE
        elif self.grid[row][collumn] == 1:
            color = arcade.color.RED
        elif self.grid[row][collumn] == 2:
            color = arcade.color.BLUE
        elif self.grid[row][collumn] == 3:
            color = arcade.color.GRAY_BLUE
        elif self.grid[row][collumn] == 4:
            color = arcade.color.GOLD
        return color








game = Minesweeper(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
game.setup_gird()
arcade.run()
