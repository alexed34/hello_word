import arcade
import random
import time


# константы
SCREEN_TITLE = 'Minesweeper'
ROW_COUNT = 7  # количество строк
COLUMN_COUNT = 7  # количество столбцов
CELL_WIDTH = 100  # ширина одной ячейки
CELL_HEIGHT = 100  # высота одной ячейки
MARGIN = 2  # толщина границы (то есть линий между ячейками)
# Ширина и высота окна высчитываются в зависимости от ширины и высоты ячеек
SCREEN_WIDTH = (CELL_WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (CELL_HEIGHT + MARGIN) * ROW_COUNT + MARGIN
# число мин
MINES_COUNT = 10
# число попыток
ATTEMPTS = 10
# картинка подорванной мины
MINE_IMAGE = 'attack.png'


class Minesweeper(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # сетка, хранит списки с количеством ячеек. см. метод setup_grid
        self.grid = []
        # содержит списки вида [row, column] -- расставленные мины
        self.mines_coordinates = []
        # список подорванных мин. Для них будем загружать картинку
        self.mines_exploded = arcade.SpriteList()
        # попытки
        self.attempts = ATTEMPTS
        # координаты трофея
        self.trophy = []
        # индикаторы победы и поражения
        self.defeat = False
        self.victory = False

    def get_cell_color(self, row, column):
        """
            Возварщает цвет клетки, в зависимости от ее состояние
            Клетка может быть в следующих состояниях: 0, 1, 2, 3, 4
        """
        if self.grid[row][column] == 0:
            color = arcade.color.LIGHT_BLUE
        elif self.grid[row][column] == 1:
            color = arcade.color.RED
        elif self.grid[row][column] == 2:
            color = arcade.color.BLUE
        elif self.grid[row][column] == 3:
            color = arcade.color.GRAY_BLUE
        elif self.grid[row][column] == 4:
            color = arcade.color.GOLD

        return color

    def check_mouse_position(self, mouse_row, mouse_column, row, column):
        """
            Проверяет, что на клетке с состоянием 3 мышки нет
        """
        if row != mouse_row or column != mouse_column:
            if self.grid[row][column] == 3:
                return True

    def setup_grid(self):
        """
            Инициализация сетки
            Сетка хранится в виде списка self.grid.
            Каждый элемент этого списка, в свою очередь, -- это список,
            содержащий ROW_COUNT чисел от 0 до 4 -- состояние,
            котором находится ячейка:
            0 -- клетка, на которую можно кликать
            1 -- клетка, на которой взорванная мина
            2 -- клетка, на которой нет мины и трофея, но на нее кликнули
            3 -- клетка, на которой находится мышка
            4 -- нажатая клетка с трофеем
            В начале игры кликать можно на все клетки,
            поэтому каждый список состоит из 0.
        """
        # заполняем вложенные списки списки, означающие строки, нулями
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

    def setup(self):
        """
            Инициализация мин на клетке.
            Случайным образом располагаем мины,
            сохраняя их координаты в виде [row, column]
            в списке self.mines_coordinates
        """
        # координаты клетки с призом
        trophy_row = random.randint(0, ROW_COUNT - 1)
        trophy_column = random.randint(0, COLUMN_COUNT - 1)
        self.trophy = [trophy_row, trophy_column]

        # расстановка мин на поле
        mines = MINES_COUNT
        while mines > 0:
            row = random.randint(0, ROW_COUNT - 1)
            column = random.randint(0, COLUMN_COUNT - 1)

            if [row, column] not in self.mines_coordinates and [row, column] != self.trophy:
                self.mines_coordinates.append([row, column])
                mines -= 1

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK)
        # рисуем сетку
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # состояние (цвет) клетки на очередном повторении
                color = self.get_cell_color(row, column)
                # Умножаем ширину ячейки с границей на номер ячейки в столбце
                # и получаем координаты левого края ячейки. Чтобы получить координаты
                # центра нужно к левому краю ячейки прибавить толщину гранциы
                # и половину ширины ячейки
                x = (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
                # Также как и для икса
                y = (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2
                arcade.draw_rectangle_filled(x, y, CELL_WIDTH, CELL_HEIGHT, color)

        # отрисовываем подорванные мины
        self.mines_exploded.draw()

        # рисуем на экране число попыток
        arcade.draw_text(f"Попыток: {self.attempts}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

        # проверяем количество попыток
        if self.attempts == 0:
            # рисуем текст
            arcade.draw_text("Ты проиграл:(", 50, SCREEN_HEIGHT // 2, arcade.color.BLACK, 50)
            # задаем переменной-индикатору проигрыша True
            self.defeat = True

        # проверяем победу
        if self.victory:
            # рисуем текст
            arcade.draw_text("Ты нашел трофей!:)", 50, SCREEN_HEIGHT // 2, arcade.color.BLACK, 50)

        # домашнее задание:
        mines_exploded = MINES_COUNT - len(self.mines_coordinates)
        arcade.draw_text(f"Мины: {mines_exploded}", SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        # проверяем переменные-индикаторы проигрыша и выигрыша
        # и если хотя бы одна из них равна True,
        # ждем 4 секунды, чтобы текст успел показаться и выходим из игры
        if self.defeat or self.victory:
            time.sleep(4)
            exit()

    def on_mouse_press(self, x, y, button, modifiers):
        """
            Эта функция вызывается, когда пользователь кликает на мышку
        """
        # чтобы получить номер ячейки в строке,
        # нужно координату икс разделить на ширину ячейки + толщина границы
        column = x // (CELL_WIDTH + MARGIN)
        # чтобы получить номер ячейки в столбце,
        # нуджно координату игрек разделить на высоту ячейки + толщину границы
        row = y // (CELL_HEIGHT + MARGIN)
        # если пользователь кликнул на
        # клетку с миной,
        # то есть [row, column] есть в списке кораблей,
        # то меняем состояние этой клетка на 1 (подорванная мина),
        # а если клетка в состоянии 0 (можно кликать),
        # то переводим клетку в состояние 2 (нажатая клетка)
        if [row, column] in self.mines_coordinates:
            self.grid[row][column] = 1
            mine_exploded = arcade.Sprite(MINE_IMAGE, 0.2)
            # высчитываем координаты центра ячейки
            # см. метод on_draw
            mine_exploded.center_x = (MARGIN + CELL_WIDTH) * column + MARGIN + CELL_WIDTH // 2
            mine_exploded.center_y = (MARGIN + CELL_HEIGHT) * row + MARGIN + CELL_HEIGHT // 2
            # добавляем спрайт корабля в список подорванных мин
            self.mines_exploded.append(mine_exploded)
            # убираем подорванную мину из списка мин
            self.mines_coordinates.remove([row, column])
            # уменьшаем количество попыток
            self.attempts -= 1
        if self.grid[row][column] == 3:
            self.grid[row][column] = 2

        # провереям, не кликнул ли игрок на клетку с трофеем
        if [row, column] == self.trophy:
            self.grid[row][column] = 4
            self.victory = True

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


Minesweeper = Minesweeper()
Minesweeper.setup_grid()
Minesweeper.setup()

arcade.run()
