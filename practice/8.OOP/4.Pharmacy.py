class Pharmacy:
    def __init__(self, medicine_id, name, company, price):
        self.medicine_id = medicine_id
        self.name = name
        self.company = company
        self.price = price

    def display(self):
        print("Medicine ID:", self.medicine_id)
        print("Medicine Name:", self.name)
        print("Company:", self.company)
        print("Price:", self.price)
        print("-------------------")


m1 = Pharmacy(1, "Paracetamol", "Cipla", 20)
m2 = Pharmacy(2, "Vitamin C", "Abbott", 50)
m3 = Pharmacy(3, "Antacid", "Pfizer", 30)
m4 = Pharmacy(4, "Cough Syrup", "Dabur", 100)
m5 = Pharmacy(5, "Calcium", "Sun Pharma", 80)

m1.display()
m2.display()
m3.display()
m4.display()
m5.display()