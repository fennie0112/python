


data = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

def summary(values):
        print("\nTotal elements:", sum(len(row) for row in values))
        print("Minimum value:", min(min(row) for row in values))
        print("Maximum value:", max(max(row) for row in values))
        print("Sum:", sum(sum(row) for row in values))

        total = sum(sum(row) for row in values)
        count = sum(len(row) for row in values)

        print("Average:", total / count)

summary(data)