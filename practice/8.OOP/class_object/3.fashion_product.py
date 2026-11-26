class FashionProduct:
    def __init__(self, product_id, name, brand, price):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.price = price

    def display(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.name)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("-------------------")


p1 = FashionProduct(1, "Shirt", "Zara", 2000)
p2 = FashionProduct(2, "Jeans", "Levis", 3000)
p3 = FashionProduct(3, "Shoes", "Nike", 5000)
p4 = FashionProduct(4, "Handbag", "Gucci", 15000)
p5 = FashionProduct(5, "Watch", "Fossil", 7000)

p1.display()
p2.display()
p3.display()
p4.display()
p5.display()