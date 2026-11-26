class Wedding:
    def __init__(self, wedding_id, bride, groom, venue, guests):
        self.wedding_id = wedding_id
        self.bride = bride
        self.groom = groom
        self.venue = venue
        self.guests = guests

    def display(self):
        print("Wedding ID:", self.wedding_id)
        print("Bride:", self.bride)
        print("Groom:", self.groom)
        print("Venue:", self.venue)
        print("Guests:", self.guests)
        print("-------------------")


w1 = Wedding(1, "Priya", "Rahul", "Rajkot", 500)
w2 = Wedding(2, "Neha", "Aman", "Mumbai", 300)
w3 = Wedding(3, "Riya", "Raj", "Delhi", 400)
w4 = Wedding(4, "Kavya", "Jay", "Surat", 250)
w5 = Wedding(5, "Pooja", "Meet", "Ahmedabad", 600)

w1.display()
w2.display()
w3.display()
w4.display()
w5.display()