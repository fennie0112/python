class LE_SSERAFIM:
    def __init__(self, name,age,role,nicckname,real_name):
        self.name = name
        self.age = age
        self.role = role
        self.nicckname = nicckname
        self.real_name = real_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Role:", self.role)
        print("Nickname:", self.nicckname)
        print("Real Name:", self.real_name)

i1= LE_SSERAFIM("Eunchae", 20, "Leader", "Eun", "Kim Eunchae\n")
i2= LE_SSERAFIM("Kazuha", 21, "Dancer", "Kazu", "Ahn Kazuha\n")
i3= LE_SSERAFIM("Sakura", 22, "Vocalist", "Saku", "Miyawaki Sakura\n")
i4= LE_SSERAFIM("Chaewon", 23, "Vocalist", "Chae", "Kim Chaewon\n")
i5= LE_SSERAFIM("Yunjin", 24, "Rapper", "Yun", "Jo Yunjin\n")

i1.display()
i2.display()
i3.display()
i4.display()
i5.display()