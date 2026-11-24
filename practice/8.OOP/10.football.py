class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.name)
        print("Category:", self.category)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("-------------------")


p1 = Product(1, "Laptop", "Electronics", 50000, 5)
p2 = Product(2, "Shirt", "Clothing", 1500, 10)
p3 = Product(3, "Shoes", "Footwear", 3000, 8)
p4 = Product(4, "Watch", "Accessories", 5000, 4)
p5 = Product(5, "Bag", "Fashion", 2000, 6)

p1.display()
p2.display()
p3.display()
p4.display()
p5.display()