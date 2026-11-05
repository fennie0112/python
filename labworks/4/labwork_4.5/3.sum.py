matrix = [[1,2,3], [4,5,6], [7,8,9]]
s = 0

for row in matrix:
    print(row)

    for x in row:
        s = s + x

print("Sum =", s)