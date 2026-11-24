class FootballPlayer:
    def __init__(self, player_id, name, country, age, goals):
        self.player_id = player_id
        self.name = name
        self.country = country
        self.age = age
        self.goals = goals

    def display(self):
        print("Player ID:", self.player_id)
        print("Player Name:", self.name)
        print("Country:", self.country)
        print("Age:", self.age)
        print("Goals:", self.goals)
        print("-------------------")


p1 = FootballPlayer(1, "Messi", "Argentina", 39, 850)
p2 = FootballPlayer(2, "Ronaldo", "Portugal", 41, 900)
p3 = FootballPlayer(3, "Neymar", "Brazil", 34, 450)
p4 = FootballPlayer(4, "Mbappe", "France", 27, 300)
p5 = FootballPlayer(5, "Haaland", "Norway", 26, 200)

p1.display()
p2.display()
p3.display()
p4.display()
p5.display()