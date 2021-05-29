class MyHeroes:
    def __init__(self):
        self.size = None
        self.path = None
        self.health = None
        self.radius = None


class NoHero(MyHeroes):
    pass


class Cat(MyHeroes):
    def __init__(self):
        super().__init__()
        self.size = 0.065
        self.path = "cat.png"
        self.health = 3
        self.radius = 1


class Kangaroo(MyHeroes):
    def __init__(self):
        super().__init__()
        self.size = 0.49
        self.path = "kangaroo.png"
        self.health = 3
        self.radius = 1


class Leopard(MyHeroes):
    def __init__(self):
        super().__init__()
        self.size = 0.04
        self.path = "leopard.png"
        self.health = 3
        self.radius = 1


class Shark(MyHeroes):
    def __init__(self):
        super().__init__()
        self.size = 0.06
        self.path = "shark.png"
        self.health = 3
        self.radius = 1


class Snake(MyHeroes):
    def __init__(self):
        super().__init__()
        self.size = 0.2
        self.path = "snake.png"
        self.health = 3
        self.radius = 1
