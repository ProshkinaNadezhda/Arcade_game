from all_sq import *


class Rules(arcade.View):
    def __init__(self, menu):
        super().__init__()
        self.menu = menu

    def move_on_page_one(self):
        self.window.show_view(PageOne(self.menu))


class Page(arcade.View):
    def __init__(self):
        super().__init__()
        h = SCREEN_HEIGHT / 15
        s = SCREEN_WIDTH / 10
        self.buttons = [Button((s - 50, h - 25), (s + 50, h + 25), (100, 50), (240, 220, 130)),
                        Button((s * 9 - 50, h - 25), (s * 9 + 50, h + 25), (100, 50), (240, 220, 130))]

    def on_draw(self, but=2):
        arcade.start_render()
        arcade.set_background_color((152, 119, 123))

        for i in range(but):
            self.buttons[i].draw_rect()

    def mouse_press(self, x, y, list_of_pages, but=2):
        for i in range(but):
            if self.buttons[i].check(x, y):
                self.window.show_view(list_of_pages[i])


class PageOne(Page):
    def __init__(self, prev_slide):
        super().__init__()
        self.prev_slide = prev_slide
        self.draw()

    def draw(self):
        super().on_draw()

        f = open('instr.txt', 'r')
        info = f.read()
        arcade.draw_text(info, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")
        f.close()

        self.buttons[0].print_text("Back", 40)
        self.buttons[1].print_text("Next", 40)

    def on_mouse_press(self, _x, _y, button, modifiers):
        super().mouse_press(_x, _y, [self.prev_slide, PageTwo(self)])


class PageTwo(Page):
    def __init__(self, prev_slide):
        super().__init__()
        self.prev_slide = prev_slide

    def draw(self):
        super().on_draw(1)
        arcade.start_render()

        animal = [Cat(), Kangaroo(), Leopard(), Shark(), Snake()]
        for i in range(len(animal)):
            arcade.Sprite(animal[i].path, animal[i].size, center_x=WIDTH, center_y=SCREEN_WIDTH - 100 - 80 * i).draw()
            arcade.draw_text(f'имеет {animal[i].health} жизней, {animal[i].attack} мощность аттаки, '
                             f'радиус перемещения:{animal[i].radius}', WIDTH * 1.5, SCREEN_WIDTH - 100 - 80 * i,
                             arcade.color.BLACK, font_size=15)

        self.buttons[0].print_text("Prev", 40)

    def on_mouse_press(self, _x, _y, button, modifiers):
        super().mouse_press(_x, _y, [self.prev_slide], 1)