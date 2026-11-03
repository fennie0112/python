matrix = [[1,2,3], [4,5,6], [7,8,9]]
print("Max =", max(max(row) for row in matrix))
print("Min =", min(min(row) for row in matrix))