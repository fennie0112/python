class Flight:
    def __init__(self, flight_no, airline, source, destination, price):
        self.flight_no = flight_no
        self.airline = airline
        self.source = source
        self.destination = destination
        self.price = price

    def display(self):
        print("Flight Number:", self.flight_no)
        print("Airline:", self.airline)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("Price:", self.price)
        print("-------------------")


f1 = Flight(101, "IndiGo", "Mumbai", "Delhi", 5000)
f2 = Flight(102, "Air India", "Ahmedabad", "Mumbai", 4000)
f3 = Flight(103, "Emirates", "Delhi", "Dubai", 15000)
f4 = Flight(104, "Vistara", "Surat", "Goa", 6000)
f5 = Flight(105, "SpiceJet", "Rajkot", "Bangalore", 7000)

f1.display()
f2.display()
f3.display()
f4.display()
f5.display()