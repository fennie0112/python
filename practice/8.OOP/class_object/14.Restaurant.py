class Restaurant:
    def __init__(self, restaurant_id, name, location, cuisine, rating):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = location
        self.cuisine = cuisine
        self.rating = rating

    def display(self):
        print("Restaurant ID:", self.restaurant_id)
        print("Restaurant Name:", self.name)
        print("Location:", self.location)
        print("Cuisine:", self.cuisine)
        print("Rating:", self.rating)
        print("-------------------")


r1 = Restaurant(1, "Taj Restaurant", "Mumbai", "Indian", 5)
r2 = Restaurant(2, "Dominos", "Rajkot", "Pizza", 4)
r3 = Restaurant(3, "McDonalds", "Delhi", "Fast Food", 4)
r4 = Restaurant(4, "Subway", "Ahmedabad", "Sandwich", 5)
r5 = Restaurant(5, "Havmor", "Surat", "Ice Cream", 5)

r1.display()
r2.display()
r3.display()
r4.display()
r5.display()