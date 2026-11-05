data = [[5, 2, 9], [1, 4, 7], [3, 6, 8]]

def statistics(values):
            minimum = min(min(row) for row in values)
            maximum = max(max(row) for row in values)
            total = sum(sum(row) for row in values)
            count = sum(len(row) for row in values)
            average = total / count

            return minimum, maximum, total, average

minimum, maximum, total, average = statistics(data)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", average)