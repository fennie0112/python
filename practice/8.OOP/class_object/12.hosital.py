class Hospital:
    def __init__(self, hospital_id, name, city, doctors, beds):
        self.hospital_id = hospital_id
        self.name = name
        self.city = city
        self.doctors = doctors
        self.beds = beds

    def display(self):
        print("Hospital ID:", self.hospital_id)
        print("Hospital Name:", self.name)
        print("City:", self.city)
        print("Doctors:", self.doctors)
        print("Beds:", self.beds)
        print("-------------------")


h1 = Hospital(1, "Apollo Hospital", "Ahmedabad", 50, 200)
h2 = Hospital(2, "Civil Hospital", "Rajkot", 40, 300)
h3 = Hospital(3, "Fortis Hospital", "Mumbai", 60, 250)
h4 = Hospital(4, "AIIMS", "Delhi", 100, 500)
h5 = Hospital(5, "Sterling Hospital", "Vadodara", 35, 150)

h1.display()
h2.display()
h3.display()
h4.display()
h5.display()