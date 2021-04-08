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

class Menu(arcade.View):
    def on_show(self):
        arcade.set_background_color((152, 119, 123))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, 23 * SCREEN_HEIGHT / 40, 350, 45, (240, 220, 130))
        arcade.draw_text("PLAY", SCREEN_WIDTH / 2, 23 * SCREEN_HEIGHT / 40,
                         arcade.color.BLACK, font_size=40, anchor_x="center", anchor_y="center")
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, 17 * SCREEN_HEIGHT / 40, 350, 45, (240, 220, 130))
        arcade.draw_text("INSTRUCTIONS", SCREEN_WIDTH / 2, 17 * SCREEN_HEIGHT / 40,
                         arcade.color.BLACK, font_size=40, anchor_x="center", anchor_y="center")

    def on_mouse_press(self, _x, _y, button, modifiers):
        s = SCREEN_WIDTH / 2

        h1 = 23 * SCREEN_HEIGHT / 40
        if (_y < h1 + 22.5) and (_y > h1 - 22.5) and (_x < s + 175.5) and (_x > s - 175.5):
            sample = Sample()
            self.window.show_view(sample)

        h2 = 17 * SCREEN_HEIGHT / 40
        if (_y < h2 + 22.5) and (_y > h2 - 22.5) and (_x < s + 175.5) and (_x > s - 175.5):
            instruction = Instruction()
            self.window.show_view(instruction)

class Instruction(arcade.View):
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
        h = SCREEN_HEIGHT / 30
        s = SCREEN_WIDTH / 10
        if (_y < h + 25) and (_y > h - 25) and (_x < s + 50) and (_x > s - 50):
            menu = Menu()
            self.window.show_view(menu)

class Sample(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color((152, 119, 123))

        self.heros_list = arcade.SpriteList()
        self.grid_sprite_list = arcade.SpriteList()

        self.grid_sprites = []
        self.heros = []

        NEW_W = WIDTH // 2
        NEW_H = HEIGHT // 2
        NEW_S = (NEW_W + MARGIN) * COLUMN_COUNT + MARGIN
        CONST = SCREEN_WIDTH // 2 - NEW_S // 2

        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(COLUMN_COUNT):
                x = column * (NEW_W + MARGIN) + (NEW_W / 2 + MARGIN) + CONST
                y = row * (NEW_H + MARGIN) + (NEW_H / 2 + MARGIN) + CONST
                if (row == 3):
                    color = (240, 220, 130)
                else:
                    color = (191, 79, 81)
                sprite = arcade.SpriteSolidColor(NEW_W, NEW_H, color)
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
                if (row == 2):
                    self.cat = arcade.Sprite(Cat().path, Cat().size, center_x=x, center_y=y)
                    self.heros_list.append(self.cat)
                if (row == 3):
                    self.kangaroo = arcade.Sprite(Kangaroo().path, Kangaroo().size, center_x=x, center_y=y)
                    self.heros_list.append(self.kangaroo)
                if (row == 4):
                    self.leopard = arcade.Sprite(Leopard().path, Leopard().size, center_x=x, center_y=y)
                    self.heros_list.append(self.leopard)
                if (row == 5):
                    self.shark = arcade.Sprite(Shark().path, Shark().size, center_x=x, center_y=y)
                    self.heros_list.append(self.shark)
                if (row == 6):
                    self.snake = arcade.Sprite(Snake().path, Snake().size, center_x=x, center_y=y)
                    self.heros_list.append(self.snake)


    def on_draw(self):
        arcade.start_render()
        self.grid_sprite_list.draw()
        self.heros_list.draw()
        arcade.draw_text("Back", SCREEN_WIDTH / 13, SCREEN_HEIGHT / 25,
                         arcade.color.BLACK, font_size=25, anchor_x="center")
        arcade.draw_text("Finish", 12 * SCREEN_WIDTH / 13, SCREEN_HEIGHT / 25,
                         arcade.color.BLACK, font_size=25, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        x = 6 * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
        y = HEIGHT / 2 + MARGIN
        c = HEIGHT // 2
        if (_x < x + c) and (_x > x - c) and (_y < y + c) and (_y > y - c):
            my_game = MyGame()
            my_game.setup()
            self.window.show_view(my_game)
        x = WIDTH / 2 + MARGIN
        if (_x < x + c) and (_x > x - c) and (_y < y + c) and (_y > y - c):
            menu = Menu()
            self.window.show_view(menu)

        c_b = int(_x // (WIDTH + MARGIN))
        r_b = int(_y // (HEIGHT + MARGIN))

        if r_b < ROW_COUNT and r_b > 1 and ((c_b == 0) or (c_b == 6)):
            if c_b == 6:
                c_b = 1
            if self.grid_heros[r_b][c_b].color == arcade.color.WHITE:
                self.grid_heros[r_b][c_b].color = (255, 126, 0)
            else:
                self.grid_heros[r_b][c_b].color = arcade.color.WHITE


class MyGame(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color((152, 119, 123))

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