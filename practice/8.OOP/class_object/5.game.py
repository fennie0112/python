class Game:
    def __init__(self, game_id, name, type, price):
        self.game_id = game_id
        self.name = name
        self.type = type
        self.price = price

    def display(self):
        print("Game ID:", self.game_id)
        print("Game Name:", self.name)
        print("Game Type:", self.type)
        print("Price:", self.price)
        print("-------------------")


g1 = Game(1, "Minecraft", "Adventure", 1000)
g2 = Game(2, "FIFA", "Sports", 2000)
g3 = Game(3, "Chess", "Strategy", 500)
g4 = Game(4, "Mario", "Arcade", 800)
g5 = Game(5, "GTA", "Action", 1500)

g1.display()
g2.display()
g3.display()
g4.display()
g5.display()