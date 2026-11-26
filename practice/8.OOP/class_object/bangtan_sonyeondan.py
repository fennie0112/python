class BTS:
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

b1= BTS("RM", 27, "Leader", "Rap Monster", "Kim Namjoon\n")
b2= BTS("Jin", 27, "Vocalist", "Worldwide Handsome", "Kim Seokjin\n")
b3= BTS("Suga", 27, "Rapper", "Agust D", "Min Yoongi\n")
b4= BTS("J-Hope", 27, "Dancer", "Hobi", "Jung Hoseok\n")
b5= BTS("Jimin", 27, "Vocalist", "Mochi", "Park Jimin\n")
b6= BTS("V", 27, "Vocalist", "TaeTae", "Kim Taehyung\n")
b7= BTS("Jungkook", 27, "Vocalist", "Golden Maknae", "Jeon Jungkook\n")

b1.display()
b2.display()
b3.display()
b4.display()
b5.display()
b6.display()
b7.display()