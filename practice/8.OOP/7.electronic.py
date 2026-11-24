class ElectronicDevice:
    def __init__(self, device_id, name, brand, price):
        self.device_id = device_id
        self.name = name
        self.brand = brand
        self.price = price

    def display(self):
        print("Device ID:", self.device_id)
        print("Device Name:", self.name)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("-------------------")


d1 = ElectronicDevice(1, "Laptop", "HP", 50000)
d2 = ElectronicDevice(2, "Mobile", "Samsung", 25000)
d3 = ElectronicDevice(3, "Tablet", "Apple", 40000)
d4 = ElectronicDevice(4, "Television", "Sony", 60000)
d5 = ElectronicDevice(5, "Headphones", "Boat", 2000)

d1.display()
d2.display()
d3.display()
d4.display()
d5.display()