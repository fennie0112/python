def product(**item):
    print("Name = ", item["name"])
    print("Quantity =", item["quantity"])
    print("Price = ", item["price"])

    total = item["price"] * item["quantity"]

    return total

print("Total:", product(name="Pen", price=10, quantity=5))