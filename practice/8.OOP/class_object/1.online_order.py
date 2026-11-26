class OnlineOrder:
    def __init__(self, order_id, customer, product, price):
        self.order_id = order_id
        self.customer = customer
        self.product = product
        self.price = price

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.customer)
        print("Product:", self.product)
        print("Price:", self.price)
        print("-------------------")


o1 = OnlineOrder(101, "Rahul", "Laptop", 50000)
o2 = OnlineOrder(102, "Priya", "Mobile", 20000)
o3 = OnlineOrder(103, "Aman", "Headphones", 2000)
o4 = OnlineOrder(104, "Neha", "Keyboard", 1500)
o5 = OnlineOrder(105, "Raj", "Mouse", 500)

o1.display()
o2.display()
o3.display()
o4.display()
o5.display()