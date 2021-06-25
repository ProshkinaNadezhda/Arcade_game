from all_sq import *

ROW_COUNT = COLUMN_COUNT = 7
WIDTH = HEIGHT = 80
MARGIN = 5
SCREEN_WIDTH = SCREEN_HEIGHT = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_TITLE = "The Last Hero"


class Team:
    def __init__(self, field, color):
        self.field = field
        self.color = color
        self.heroes = [Cat(), Kangaroo(), Leopard(), Shark(), Snake()]
        for i in range(len(self.field.list_buttons[0])):
            self.field.list_buttons[0][i].sprite = arcade.Sprite(self.heroes[i].path, self.heroes[i].size,
                                                                 center_x=self.field.list_buttons[0][i].get_center(0),
                                                                 center_y=self.field.list_buttons[0][i].get_center(1))
            self.field.list_buttons[0][i].animal = self.heroes[i]

    def draw_all(self):
        for i in range(len(self.field.list_buttons[0])):
            self.field.list_buttons[0][i].draw_rect(self.color)
            self.field.list_buttons[0][i].draw_sprite()
            self.field.list_buttons[0][i].draw_heart()

    def check_click(self, x, y):
        for i in range(len(self.field.list_buttons[0])):
            a = self.field.list_buttons[0][i].check_click(x, y)
            if a != NoHero:
                return a
        return NoHero

    def get_color(self):
        return self.color


class Menu(arcade.View):
    def __init__(self):
        super().__init__()
        s = SCREEN_WIDTH / 2
        h1 = 23 * SCREEN_HEIGHT / 40
        h2 = 17 * SCREEN_HEIGHT / 40
        self.rules = Rules(self)
        self.init_characters = InitCharacters(self)
        self.buttons = [(Button((s - 175.5, h2 - 22.5), (s + 175.5, h2 + 22.5), (350, 45), (240, 220, 130)),
                         self.rules),
                        (Button((s - 175.5, h1 - 22.5), (s + 175.5, h1 + 22.5), (350, 45), (240, 220, 130)),
                         self.init_characters)]

    def on_show(self):
        arcade.set_background_color((152, 119, 123))

    def on_draw(self):
        arcade.start_render()

        self.buttons[0][0].draw_rect()
        self.buttons[0][0].print_text("RULES", 40)
        self.buttons[1][0].draw_rect()
        self.buttons[1][0].print_text("PLAY", 40)

    def on_mouse_press(self, _x, _y, button, modifiers):
        for i in self.buttons:
            k = i[0].check(_x, _y)
            if k:
                self.window.show_view(i[1])


class Rules(arcade.View):
    def __init__(self, menu):
        super().__init__()
        h = SCREEN_HEIGHT / 30
        s = SCREEN_WIDTH / 10
        self.menu = menu
        self.rules_next = RulesNextSlide(self)
        self.buttons = [(Button((s - 50, h - 25), (s + 50, h + 25), (100, 50), (240, 220, 130)), self.menu),
                        (Button((s * 9 - 50, h - 25), (s * 9 + 50, h + 25), (100, 50), (240, 220, 130)),
                         self.rules_next)]

    def on_show(self):
        arcade.set_background_color((152, 119, 123))

    def on_draw(self):
        arcade.start_render()
        f = open('instr.txt', 'r')
        info = f.read()
        arcade.draw_text(info, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")
        f.close()

        self.buttons[0][0].draw_rect()
        self.buttons[0][0].print_text("Back", 40)
        self.buttons[1][0].draw_rect()
        self.buttons[1][0].print_text("Next", 40)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        for i in self.buttons:
            k = i[0].check(_x, _y)
            if k:
                self.window.show_view(i[1])


class RulesNextSlide(arcade.View):
    def __init__(self, rules):
        super().__init__()
        h = SCREEN_HEIGHT / 30
        s = SCREEN_WIDTH / 10
        self.rules = rules
        self.button = (Button((s - 50, h - 25), (s + 50, h + 25), (100, 50), (240, 220, 130)), self.rules)

    def on_show(self):
        arcade.set_background_color((152, 119, 123))

    def on_draw(self):
        arcade.start_render()
        animal = [Cat(), Kangaroo(), Leopard(), Shark(), Snake()]
        for i in range(len(animal)):
            arcade.Sprite(animal[i].path, animal[i].size, center_x=WIDTH, center_y=SCREEN_WIDTH - 100 - 80 * i).draw()
            arcade.draw_text(f'имеет {animal[i].health} жизней, {animal[i].attack} мощность аттаки, '
                             f'радиус перемещения:{animal[i].radius}', WIDTH * 1.5, SCREEN_WIDTH - 100 - 80 * i,
                             arcade.color.BLACK, font_size=15)

        self.button[0].draw_rect()
        self.button[0].print_text("Prev", 40)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        k = self.button[0].check(_x, _y)
        if k:
            self.window.show_view(self.button[1])


class InitCharacters(arcade.View):
    def __init__(self, menu):
        super().__init__()
        arcade.set_background_color((152, 119, 123))

        x1, x2 = WIDTH // 2 + MARGIN, (COLUMN_COUNT - 1) * (WIDTH + MARGIN) + (WIDTH // 2 + MARGIN)
        self.menu, c = menu, HEIGHT // 2

        self.game_field = Field([2 * MARGIN + HEIGHT, 2 * MARGIN + HEIGHT],
                                [(MARGIN + HEIGHT) * 6, (MARGIN + HEIGHT) * 6], (7, 7), (240, 220, 130))
        self.change_game_field()
        self.red_team = Team(Field([0, (MARGIN + HEIGHT) * 2], [2 * MARGIN + HEIGHT, SCREEN_HEIGHT], (1, 5),
                                   (240, 220, 130)), (218, 97, 78))
        self.blue_team = Team(Field([(MARGIN + HEIGHT) * 6, (MARGIN + HEIGHT) * 2], [SCREEN_WIDTH, SCREEN_HEIGHT],
                                    (1, 5), (240, 220, 130)), (119, 158, 203))

        self.buttons = [(Button((x2 - c, MARGIN), (x2 + c, MARGIN + HEIGHT), (HEIGHT, HEIGHT), (240, 220, 130)),
                         MyGame(self.game_field)),
                        (Button((x1 - c, MARGIN), (x1 + c, MARGIN + HEIGHT), (HEIGHT, HEIGHT), (240, 220, 130)),
                         self.menu)]

        self.indicator, self.but_color = NoHero, 0

    def change_game_field(self):
        for i in range(7):
            for j in range(2):
                self.game_field.list_buttons[i][j].change_color((252, 194, 0))
                self.game_field.list_buttons[i][j + 5].change_color((252, 194, 0))

    def on_draw(self):
        arcade.start_render()

        self.red_team.draw_all()
        self.blue_team.draw_all()
        self.game_field.draw_all()

        self.buttons[0][0].draw_rect()
        self.buttons[0][0].print_text("Finish", 25)
        self.buttons[1][0].draw_rect()
        self.buttons[1][0].print_text("Back", 25)

        arcade.draw_text('Red team', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 10,
                         arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")
        arcade.draw_text('Blue team', SCREEN_WIDTH / 2, 9 * SCREEN_HEIGHT / 10,
                         arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        for i in range(len(self.buttons)):
            if self.buttons[i][0].check(_x, _y):
                if i == 1:
                    self.window.show_view(self.buttons[i][1])
                elif not(self.check_process('red')) and not(self.check_process('blue')):
                    self.window.show_view(self.buttons[i][1])

        p = [self.red_team, self.blue_team, 'red', 'blue']
        for i in range(2):
            if p[i].check_click(_x, _y) != NoHero:
                self.indicator = p[i].check_click(_x, _y)
                self.but_color = p[i].get_color()
                if self.check_process(p[i + 2]) == 0:
                    self.indicator = NoHero

        param = self.game_field.check_click(_x, _y)
        if param != NoHero and self.indicator != NoHero and \
                self.check_area(self.but_color, self.game_field.get_coordinate(_x, _y)):
            param.change_sprite(self.indicator)
            param.change_animal(self.indicator)
            param.change_color(self.but_color)
            self.indicator = NoHero
        self.check_process('red')
        self.check_process('blue')

    @staticmethod
    def check_area(color, y):
        if color == (218, 97, 78) and y[1] < 2:
            return True
        if color == (119, 158, 203) and y[1] > 4:
            return True

    def check_process(self, color):
        red, blue = 0, 0
        for i in range(self.game_field.get_size(0)):
            for j in range(self.game_field.get_size(1)):
                if self.game_field.list_buttons[i][j].get_color() == (218, 97, 78):
                    red += 1
                if self.game_field.list_buttons[i][j].get_color() == (119, 158, 203):
                    blue += 1
        if color == 'red' and red == 5:
            self.change_field_color()
            return False
        if color == 'blue' and blue == 5:
            self.change_field_color(5)
            return False
        return True

    def change_field_color(self, param=0):
        for i in range(7):
            for j in range(2):
                if self.game_field.list_buttons[i][j + param].get_color() == (252, 194, 0):
                    self.game_field.list_buttons[i][j + param].change_color((240, 220, 130))


class MyGame(arcade.View):
    def __init__(self, game_field):
        super().__init__()

        arcade.set_background_color((152, 119, 123))

        self.sq, self.c_x, self.c_y, self.team_color = NoHero, 0, 0, 0
        self.game_field = game_field

    def on_draw(self):
        arcade.start_render()
        self.game_field.draw_all()
        if self.check_process():
            arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                         SCREEN_WIDTH, SCREEN_HEIGHT, (152, 119, 123))
            arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                         WIDTH * 8, WIDTH * 1.2, (240, 220, 130))
            arcade.draw_text(f'{self.check_process()}', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.BLACK, font_size=45, anchor_x="center", anchor_y="center")
            arcade.draw_text("press SHIFT", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4,
                             arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")

    def on_key_press(self, symbol: int, modifiers: int):
        self.window.show_view(Menu())

    def on_mouse_press(self, x, y, button, modifiers):
        param = self.game_field.check_click(x, y)
        x, y = self.game_field.get_coordinate(x, y)
        if param == NoHero:
            return
        if param.animal != NoHero and self.sq == NoHero:
            self.sq, self.team_color, self.c_x, self.c_y = param, param.color, x, y
            self.make_backlight(x, y, param.animal.radius)
        elif param.animal == NoHero and self.sq != NoHero:
            if self.check_distance(self.sq.animal.radius, self.c_x, self.c_y, x, y):
                self.delete_backlight(self.c_x, self.c_y, self.sq.animal.radius)
                self.game_field.change_buttons(x, y, self.c_x, self.c_y)
            self.sq = NoHero
        elif param.animal != NoHero and self.sq != NoHero and param.color != self.team_color:
            if self.check_distance(self.sq.animal.radius, self.c_x, self.c_y, x, y):
                self.subtraction_health(x, y)
                self.delete_backlight(self.c_x, self.c_y, self.sq.animal.radius)
            self.check_health(x, y)
            self.sq = NoHero
        else:
            self.sq = NoHero
            self.delete_backlight(self.c_x, self.c_y, self.sq.animal.radius)

    def subtraction_health(self, x, y):
        self.game_field.list_buttons[x][y].animal.health -= \
            self.game_field.list_buttons[self.c_x][self.c_y].animal.attack

    def check_health(self, x, y):
        if self.game_field.list_buttons[x][y].animal.health <= 0:
            self.game_field.list_buttons[x][y].change_sq(NoHero)

    @staticmethod
    def check_distance(radius, x, y, xl, yl):
        if xl in range(x - radius, x + radius + 1) and yl in range(y - radius, y + radius + 1):
            return True
        return False

    def check_process(self):
        red, blue = 0, 0
        for i in range(self.game_field.get_size(0)):
            for j in range(self.game_field.get_size(1)):
                if self.game_field.list_buttons[i][j].get_color() == (218, 97, 78):
                    red += 1
                if self.game_field.list_buttons[i][j].get_color() == (119, 158, 203):
                    blue += 1
        if red == 0:
            return "Blue team is the winner!!!"
        if blue == 0:
            return "Red team is the winner!!!"
        return False

    def make_backlight(self, x, y, r):
        for i in range(self.game_field.get_size(0)):
            for j in range(self.game_field.get_size(1)):
                if i in range(x-r, x+r+1) and j in range(y-r, y+r+1) and \
                        self.game_field.list_buttons[i][j].get_color() == (240, 220, 130):
                    self.game_field.list_buttons[i][j].change_color((252, 194, 0))

    def delete_backlight(self, x, y, r):
        for i in range(self.game_field.get_size(0)):
            for j in range(self.game_field.get_size(1)):
                if i in range(x-r, x+r+1) and j in range(y-r, y+r+1) and \
                        self.game_field.list_buttons[i][j].get_color() == (252, 194, 0):
                    self.game_field.list_buttons[i][j].change_color((240, 220, 130))


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu = Menu()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()
