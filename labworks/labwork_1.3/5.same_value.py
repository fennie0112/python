a = 10
b = 10

print("id(a):", id(a))
print("id(b):", id(b))
print("Same object?", a is b)

a = 20

print("After modifying a:")
print("id(a):", id(a))
print("id(b):", id(b))
print("Same object?", a is b)