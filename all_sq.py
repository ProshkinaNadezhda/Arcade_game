import arcade
from heroes import *


ROW_COUNT = COLUMN_COUNT = 7
WIDTH = HEIGHT = 80
MARGIN = 5
SCREEN_WIDTH = SCREEN_HEIGHT = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN


class Sq:
    def __init__(self, lb, rb):
        self.lb = lb
        self.rb = rb


class Button(Sq):
    def __init__(self, lb, rb, sz, color, sprite=NoHero, animal=NoHero):
        super().__init__(lb, rb)
        self.color = color
        self.sz = sz
        self.sprite = sprite
        self.animal = animal
        if animal != NoHero:
            self.animal_health = self.animal.health
        else:
            self.animal_health = 0

    def check(self, x, y):
        if (x > self.lb[0]) and (x < self.rb[0]) and (y > self.lb[1]) and (y < self.rb[1]):
            return True
        return False

    def check_click(self, x, y):
        if (x > self.lb[0]) and (x < self.rb[0]) and (y > self.lb[1]) and (y < self.rb[1]):
            return type(self.animal)
        return NoHero

    def print_text(self, text, sz):
        arcade.draw_text(text, self.lb[0] + self.sz[0] // 2, self.lb[1] + self.sz[1] // 2,
                         arcade.color.BLACK, font_size=sz, anchor_x="center", anchor_y="center")

    def draw_rect(self, c=(0, 0, 0)):
        if c == (0, 0, 0):
            c = self.color
        arcade.draw_rectangle_filled(self.lb[0] + self.sz[0] // 2, self.lb[1] + self.sz[1] // 2,
                                     self.sz[0], self.sz[1], c)

    def draw_heart(self):
        if self.animal != NoHero:
            arcade.Sprite(self.animal.heart, 0.03, center_x=self.lb[0] + self.sz[0] // 6,
                          center_y=self.lb[1] + self.sz[1] // 6).draw()
            arcade.draw_text(f'{self.animal.health}', self.lb[0] + self.sz[0] // 6, self.lb[1] + self.sz[1] // 6,
                             arcade.color.WHITE, font_size=17, anchor_x="center", anchor_y="center")

    def get_center(self, x):
        return self.lb[x] + self.sz[0] // 2

    def get_color(self):
        return self.color

    def draw_sprite(self):
        if self.sprite != NoHero:
            self.sprite.draw()

    def change_color(self, color):
        self.color = color

    def change_animal(self, animal):
        self.animal = animal()

    def change_sprite(self, kind):
        animal = kind()
        size = self.sz[0] / WIDTH * animal.size
        self.sprite = arcade.Sprite(animal.path, size, center_x=self.get_center(0), center_y=self.get_center(1))

    def change_sq(self, sq):
        if sq != NoHero:
            self.color = sq.color
            self.change_sprite(type(sq.animal))
            self.animal = sq.animal
            self.animal_health, sq.animal_health = sq.animal_health, self.animal_health
            sq.animal = NoHero
            sq.sprite = NoHero
            sq.color = (240, 220, 130)
        else:
            self.color = (240, 220, 130)
            self.animal = NoHero
            self.sprite = NoHero


class Field(Sq):
    def __init__(self, lb, rb, sz, color):
        super().__init__(lb, rb)
        self.sz = sz
        self.color = color

        sz_sq = ((self.rb[0] - self.lb[0]) - (MARGIN * (self.sz[0] + 1))) // self.sz[0]
        sp = sz_sq + MARGIN
        x0 = lb[0] + MARGIN
        y0 = lb[1] + MARGIN

        self.list_buttons = []
        for i in range(sz[0]):
            self.list_buttons.append([])
            for j in range(sz[1]):
                self.list_buttons[i].append(Button([x0 + i * sp, y0 + j * sp],
                                                   [x0 + i * sp + sz_sq, y0 + j * sp + sz_sq],
                                                   (sz_sq, sz_sq), self.color, NoHero, NoHero))

    def get_size(self, par):
        return self.sz[par]

    def check_click(self, x, y):
        for i in range(self.sz[0]):
            for j in range(self.sz[1]):
                a = self.list_buttons[i][j].check(x, y)
                if a:
                    return self.list_buttons[i][j]
        return NoHero

    def get_coordinate(self, x, y):
        for i in range(self.sz[0]):
            for j in range(self.sz[1]):
                a = self.list_buttons[i][j].check(x, y)
                if a:
                    return i, j
        return NoHero

    def change_buttons(self, x1, y1, x2, y2):
        self.list_buttons[x1][y1].change_sq(self.list_buttons[x2][y2])

    def draw_all(self):
        for j in range(self.sz[0]):
            for i in range(self.sz[1]):
                self.list_buttons[j][i].draw_rect()
                self.list_buttons[j][i].draw_sprite()
                self.list_buttons[j][i].draw_heart()