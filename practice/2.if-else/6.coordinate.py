x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("The coordinate point lies in the First quadrant.")
elif x < 0 and y > 0:
    print("The coordinate point lies in the Second quadrant.")
elif x < 0 and y < 0:
    print("The coordinate point lies in the Third quadrant.")
elif x > 0 and y < 0:
    print("The coordinate point lies in the Fourth quadrant.")
else:
    print("The coordinate point lies on an axis.")