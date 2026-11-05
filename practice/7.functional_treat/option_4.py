
uservalue = int(input("Enter the value to filter: "))

my_list = []

for row in data:
    temp = list(filter(lambda x: x >= uservalue, row))
    my_list.append(temp)

print("Filtered data:", my_list)