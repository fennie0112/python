class Cricket:

    def __init__(self, name,age,country,run,role):
        self.name = name
        self.age = age
        self.country = country
        self.run = run
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Country:", self.country)
        print("Run:", self.run)
        print("Role:", self.role)


c1= Cricket("Virat Kohli", 34, "India", 12000, "Batsman\n")
c2= Cricket("MS Dhoni", 39, "India", 10500, "Wicket Keeper\n")
c3= Cricket("Rashid Khan", 22, "Afghanistan", 2000, "Bowler\n")
c4= Cricket("Ben Stokes", 29, "England", 5000, "All Rounder\n")
c5= Cricket("Steve Smith", 31, "Australia", 8000, "Batsman\n")

c1.display()
c2.display()
c3.display()
c4.display()
c5.display()