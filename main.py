import arcade


ROW_COUNT = COLUMN_COUNT = 7
WIDTH = HEIGHT = 80
MARGIN = 5
SCREEN_WIDTH = SCREEN_HEIGHT = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_TITLE = "The Last Hero"


class MyHeros:
    def __init__(self):
        self.size = None
        self.path = None
        self.health = None
        self.radius = None


class Cat(MyHeros):
    def __init__(self):
        super().__init__()
        self.size = 0.065
        self.path = "cat.png"
        self.health = 3
        self.radius = 1


class Kangaroo(MyHeros):
    def __init__(self):
        super().__init__()
        self.size = 0.49
        self.path = "kangaroo.png"
        self.health = 3
        self.radius = 1


class Leopard(MyHeros):
    def __init__(self):
        super().__init__()
        self.size = 0.04
        self.path = "leopard.png"
        self.health = 3
        self.radius = 1


class Shark(MyHeros):
    def __init__(self):
        super().__init__()
        self.size = 0.06
        self.path = "shark.png"
        self.health = 3
        self.radius = 1


class Snake(MyHeros):
    def __init__(self):
        super().__init__()
        self.size = 0.2
        self.path = "snake.png"
        self.health = 3
        self.radius = 1


class Button:
    def __init__(self, lb, rb, action):
        self.lb = lb
        self.rb = rb
        self.action = action

    def check_click(self, x, y):
        if (x > self.lb[0]) and (x < self.rb[0]) and (y > self.lb[1]) and (y < self.rb[1]):
            return self.action


class Menu(arcade.View):
    def __init__(self):
        super().__init__()
        s = SCREEN_WIDTH / 2
        h1 = 23 * SCREEN_HEIGHT / 40
        h2 = 17 * SCREEN_HEIGHT / 40
        self.rules = Rules(self)
        self.init_characters = InitCharacters(self)
        self.buttons = [Button((s - 175.5, h2 - 22.5), (s + 175.5, h2 + 22.5), self.rules),
                        Button((s - 175.5, h1 - 22.5), (s + 175.5, h1 + 22.5), self.init_characters)]

    def on_show(self):
        arcade.set_background_color((152, 119, 123))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, 23 * SCREEN_HEIGHT / 40, 350, 45, (240, 220, 130))
        arcade.draw_text("PLAY", SCREEN_WIDTH / 2, 23 * SCREEN_HEIGHT / 40,
                         arcade.color.BLACK, font_size=40, anchor_x="center", anchor_y="center")
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, 17 * SCREEN_HEIGHT / 40, 350, 45, (240, 220, 130))
        arcade.draw_text("RULES", SCREEN_WIDTH / 2, 17 * SCREEN_HEIGHT / 40,
                         arcade.color.BLACK, font_size=40, anchor_x="center", anchor_y="center")

    def on_mouse_press(self, _x, _y, button, modifiers):
        for i in self.buttons:
            k = i.check_click(_x, _y)
            if k:
                self.window.show_view(k)


class Rules(arcade.View):
    def __init__(self, menu):
        super().__init__()
        h = SCREEN_HEIGHT / 30
        s = SCREEN_WIDTH / 10
        self.menu = menu
        self.button = Button((s - 505, h - 25), (s + 50, h + 25), self.menu)

    def on_show(self):
        arcade.set_background_color((152, 119, 123))

    def on_draw(self):
        arcade.start_render()
        f = open('instr.txt', 'r')
        info = f.read()
        arcade.draw_text(info, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 10, SCREEN_HEIGHT / 30, 100, 50, (240, 220, 130))
        arcade.draw_text("Back", SCREEN_WIDTH / 10, SCREEN_HEIGHT / 30,
                         arcade.color.BLACK, font_size=40, anchor_x="center", anchor_y="center")
        f.close()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        k = self.button.check_click(_x, _y)
        if k:
            self.window.show_view(k)


class InitCharacters(arcade.View):
    def __init__(self, menu):
        super().__init__()
        x = 6 * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
        y = HEIGHT / 2 + MARGIN
        c = HEIGHT // 2
        w = WIDTH / 2 + MARGIN
        self.menu = menu
        self.buttons = [Button((x - c, y - c), (x + c, y + c), MyGame(self.menu)),
                        Button((w - c, y - c), (w + c, y + c), menu)]

        arcade.set_background_color((152, 119, 123))

        self.heros_list = arcade.SpriteList()
        self.grid_sprite_list = arcade.SpriteList()

        self.grid_sprites = []
        self.heros = []

        new_w = WIDTH // 2
        new_h = HEIGHT // 2
        new_s = (new_w + MARGIN) * COLUMN_COUNT + MARGIN
        const = SCREEN_WIDTH // 2 - new_s // 2

        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(COLUMN_COUNT):
                x = column * (new_w + MARGIN) + (new_w / 2 + MARGIN) + const
                y = row * (new_h + MARGIN) + (new_h / 2 + MARGIN) + const
                if row == 3:
                    color = (240, 220, 130)
                else:
                    color = (191, 79, 81)
                sprite = arcade.SpriteSolidColor(new_w, new_h, color)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)

        self.grid_heros = []
        for row in range(7):
            self.grid_heros.append([])
            for column in range(2):
                x = 6 * column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, (240, 220, 130))
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_heros[row].append(sprite)
                animal = [Cat(), Kangaroo(), Leopard(), Shark(), Snake()]
                for i in range(2, 7):
                    if row == i:
                        self.heros_list.append(arcade.Sprite(animal[i - 2].path,
                                                             animal[i - 2].size,
                                                             center_x=x, center_y=y))

    def on_draw(self):
        arcade.start_render()
        self.grid_sprite_list.draw()
        self.heros_list.draw()
        arcade.draw_text("Back", SCREEN_WIDTH / 13, SCREEN_HEIGHT / 25,
                         arcade.color.BLACK, font_size=25, anchor_x="center")
        arcade.draw_text("Finish", 12 * SCREEN_WIDTH / 13, SCREEN_HEIGHT / 25,
                         arcade.color.BLACK, font_size=25, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        for i in self.buttons:
            k = i.check_click(_x, _y)
            if k:
                self.window.show_view(k)

        c_b = int(_x // (WIDTH + MARGIN))
        r_b = int(_y // (HEIGHT + MARGIN))

        if r_b in range(2, ROW_COUNT) and (c_b == 0 or c_b == 6):
            if c_b == 6:
                c_b = 1
            if self.grid_heros[r_b][c_b].color == arcade.color.WHITE:
                self.grid_heros[r_b][c_b].color = (255, 126, 0)
            else:
                self.grid_heros[r_b][c_b].color = arcade.color.WHITE


class MyGame(arcade.View):
    def __init__(self, menu):
        super().__init__()

        arcade.set_background_color((152, 119, 123))

        self.menu = menu
        self.button = Button((50, 25), (50, 25), self.menu)

        self.grid_sprite_list = arcade.SpriteList()

        self.grid_sprites = []

        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, (240, 220, 130))
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)

    def setup(self):
        # Настроить игру здесь
        pass

    def on_draw(self):
        arcade.start_render()
        self.grid_sprite_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        if row < ROW_COUNT and column < COLUMN_COUNT:
            if self.grid_sprites[row][column].color == arcade.color.WHITE:
                self.grid_sprites[row][column].color = (255, 126, 0)
            else:
                self.grid_sprites[row][column].color = arcade.color.WHITE


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu = Menu()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()
