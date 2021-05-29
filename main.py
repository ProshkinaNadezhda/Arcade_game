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
        self.buttons = [(Button((s - 175.5, h2 - 22.5), (s + 175.5, h2 + 22.5), (350, 45), (240, 220, 130), NoHero()),
                         self.rules),
                        (Button((s - 175.5, h1 - 22.5), (s + 175.5, h1 + 22.5), (350, 45), (240, 220, 130), NoHero()),
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
        self.button = (Button((s - 50, h - 25), (s + 50, h + 25), (100, 50), (240, 220, 130), NoHero()), self.menu)

    def on_show(self):
        arcade.set_background_color((152, 119, 123))

    def on_draw(self):
        arcade.start_render()
        f = open('instr.txt', 'r')
        info = f.read()
        arcade.draw_text(info, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")
        f.close()

        self.button[0].draw_rect()
        self.button[0].print_text("Back", 40)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        k = self.button[0].check(_x, _y)
        if k:
            self.window.show_view(self.button[1])


class InitCharacters(arcade.View):
    def __init__(self, menu):
        super().__init__()

        arcade.set_background_color((152, 119, 123))

        x1 = WIDTH // 2 + MARGIN
        x2 = (COLUMN_COUNT - 1) * (WIDTH + MARGIN) + (WIDTH // 2 + MARGIN)
        c = HEIGHT // 2
        self.menu = menu

        self.game_field = Field((2 * MARGIN + HEIGHT, 2 * MARGIN + HEIGHT),
                                ((MARGIN + HEIGHT) * 6, (MARGIN + HEIGHT) * 6), (7, 7), (240, 220, 130))

        self.red_team = Team(Field((0, (MARGIN + HEIGHT) * 2), (2 * MARGIN + HEIGHT, SCREEN_HEIGHT), (1, 5),
                                   (240, 220, 130)), (218, 97, 78))

        self.blue_team = Team(Field((((MARGIN + HEIGHT) * 6), ((MARGIN + HEIGHT) * 2)), (SCREEN_WIDTH, SCREEN_HEIGHT),
                                    (1, 5), (240, 220, 130)), (119, 158, 203))

        self.buttons = [(Button((x2 - c, MARGIN), (x2 + c, MARGIN + HEIGHT), (HEIGHT, HEIGHT), (240, 220, 130),
                                NoHero(), NoHero), MyGame(self.menu, self.game_field)),
                        (Button((x1 - c, MARGIN), (x1 + c, MARGIN + HEIGHT), (HEIGHT, HEIGHT), (240, 220, 130),
                                NoHero(), NoHero), self.menu)]

        self.indicator = NoHero
        self.but_color = 0

    def on_draw(self):
        arcade.start_render()

        self.red_team.draw_all()
        self.blue_team.draw_all()
        self.game_field.draw_all()

        self.buttons[0][0].draw_rect()
        self.buttons[0][0].print_text("Finish", 25)
        self.buttons[1][0].draw_rect()
        self.buttons[1][0].print_text("Back", 25)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        for i in self.buttons:
            if i[0].check(_x, _y):
                self.window.show_view(i[1])

        if self.red_team.check_click(_x, _y) != NoHero:
            self.indicator = self.red_team.check_click(_x, _y)
            self.but_color = self.red_team.get_color()
            if self.check_process('red') == 0:
                self.indicator = NoHero

        if self.blue_team.check_click(_x, _y) != NoHero:
            self.indicator = self.blue_team.check_click(_x, _y)
            self.but_color = self.blue_team.get_color()
            if self.check_process('blue') == 0:
                self.indicator = NoHero

        param = self.game_field.check_click(_x, _y)
        if param != NoHero and self.indicator != NoHero:
            param.change_sprite(self.indicator)
            param.change_color(self.but_color)
            self.indicator = NoHero

    def check_process(self, color):
        red, blue = 0, 0
        for i in range(self.game_field.get_size(0)):
            for j in range(self.game_field.get_size(1)):
                if self.game_field.list_buttons[i][j].get_color() == (218, 97, 78):
                    red += 1
                if self.game_field.list_buttons[i][j].get_color() == (119, 158, 203):
                    blue += 1
        if color == 'red' and red == 5:
            return False
        if color == 'blue' and blue == 5:
            return False
        return True


class MyGame(arcade.View):
    def __init__(self, menu, game_field):
        super().__init__()

        arcade.set_background_color((152, 119, 123))

        self.menu = menu
        self.button = (Button((50, 25), (50, 25), HEIGHT, (240, 220, 130), NoHero()), self.menu)

        self.game_field = game_field

    def on_draw(self):
        arcade.start_render()

        self.game_field.draw_all()

    def on_mouse_press(self, x, y, button, modifiers):
        pass


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu = Menu()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()
